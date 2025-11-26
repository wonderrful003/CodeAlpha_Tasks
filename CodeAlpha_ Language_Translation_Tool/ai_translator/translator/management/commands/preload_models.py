import os
import time
import psutil
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Pre-load all available translation models for faster performance'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-large',
            action='store_true',
            help='Skip large models to save memory',
        )
        parser.add_argument(
            '--priority-only',
            action='store_true',
            help='Load only priority models (most common languages)',
        )

    def handle(self, *args, **options):
        # Import here to avoid circular imports
        from translator.services.translation_service import translation_service
        
        self.stdout.write('🚀 Starting model pre-loading process...')
        self.stdout.write('=' * 60)
        
        # Get memory info before loading
        initial_memory = self.get_memory_usage()
        
        # Initialize translation service
        if not translation_service._initialized:
            translation_service.initialize()
        
        # Define model loading strategies
        if options['priority_only']:
            models_to_load = self.get_priority_models()
            self.stdout.write(self.style.WARNING('📋 Loading PRIORITY models only'))
        elif options['skip_large']:
            models_to_load = self.get_standard_models()
            self.stdout.write(self.style.WARNING('📋 Loading STANDARD models (skipping large ones)'))
        else:
            models_to_load = self.get_all_models()
            self.stdout.write(self.style.SUCCESS('📋 Loading ALL available models'))
        
        total_models = len(models_to_load)
        successful_loads = 0
        failed_loads = 0
        start_time = time.time()
        
        self.stdout.write(f'📊 Total models to load: {total_models}')
        self.stdout.write(f'💾 Initial memory: {initial_memory} MB')
        self.stdout.write('-' * 60)
        
        # Load models with progress tracking
        for i, (source, target) in enumerate(models_to_load, 1):
            model_name = translation_service.get_model_name(source, target)
            if not model_name:
                self.stdout.write(self.style.WARNING(f'[{i}/{total_models}] ❌ No model for {source}->{target}'))
                failed_loads += 1
                continue
            
            self.stdout.write(f'[{i}/{total_models}] 🔄 Loading {source}->{target}...')
            
            try:
                load_start = time.time()
                
                # Check if model is already loaded
                model_key = f"{source}_{target}"
                if model_key in translation_service.models:
                    self.stdout.write(self.style.WARNING(f'     ⚡ Already loaded (cached)'))
                    successful_loads += 1
                    continue
                
                # Load the model
                model, tokenizer = translation_service.load_model(source, target)
                load_time = time.time() - load_start
                
                # Get model info
                param_count = sum(p.numel() for p in model.parameters())
                self.stdout.write(
                    self.style.SUCCESS(
                        f'     ✅ Loaded in {load_time:.1f}s | '
                        f'Params: {param_count:,}'
                    )
                )
                successful_loads += 1
                
            except Exception as e:
                error_msg = str(e)
                if 'not a local folder' in error_msg:
                    self.stdout.write(self.style.ERROR(f'     ❌ Model not available: {model_name}'))
                else:
                    self.stdout.write(self.style.ERROR(f'     ❌ Failed: {error_msg}'))
                failed_loads += 1
        
        # Summary
        total_time = time.time() - start_time
        final_memory = self.get_memory_usage()
        memory_used = final_memory - initial_memory
        
        self.stdout.write('=' * 60)
        self.stdout.write(self.style.SUCCESS('🎉 MODEL PRE-LOADING COMPLETED!'))
        self.stdout.write(f'📊 Summary:')
        self.stdout.write(f'   ✅ Successful: {successful_loads}')
        self.stdout.write(f'   ❌ Failed: {failed_loads}')
        self.stdout.write(f'   ⏱️ Total time: {total_time:.1f}s')
        self.stdout.write(f'   💾 Memory used: {memory_used} MB')
        self.stdout.write(f'   💾 Final memory: {final_memory} MB')
        self.stdout.write(f'   🔥 Loaded models: {len(translation_service.models)}')
        
        # Show loaded models
        if translation_service.models:
            self.stdout.write('\n📋 Successfully Loaded Models:')
            for model_key in sorted(translation_service.models.keys()):
                self.stdout.write(f'   • {model_key}')
        
        # Show failed models
        if failed_loads > 0:
            self.stdout.write('\n⚠️ Models that failed to load:')
            for i, (source, target) in enumerate(models_to_load, 1):
                model_key = f"{source}_{target}"
                if model_key not in translation_service.models:
                    model_name = translation_service.get_model_name(source, target)
                    if model_name:
                        self.stdout.write(f'   • {source}->{target} ({model_name})')
    
    def get_priority_models(self):
        """Get most commonly used models"""
        return [
            # English pairs (most important)
            ('en', 'es'), ('es', 'en'),
            ('en', 'fr'), ('fr', 'en'),
            ('en', 'de'), ('de', 'en'),
            ('en', 'it'), ('it', 'en'),
            ('en', 'pt'), ('pt', 'en'),
            ('en', 'ru'), ('ru', 'en'),
            
            # Key African languages
            ('en', 'sw'), ('sw', 'en'),
            ('en', 'yo'), ('yo', 'en'),
            ('en', 'ig'), ('ig', 'en'),
            ('en', 'ha'), ('ha', 'en'),
            ('en', 'ny'), ('ny', 'en'),
            
            # Asian languages
            ('en', 'zh'), ('zh', 'en'),
            ('en', 'ja'), ('ja', 'en'),
            ('en', 'ko'), ('ko', 'en'),
            ('en', 'ar'), ('ar', 'en'),
        ]
    
    def get_standard_models(self):
        """Get all standard models"""
        priority_models = self.get_priority_models()
        
        # Add other available models
        additional_models = [
            ('en', 'xh'), ('xh', 'en'),
            ('en', 'rw'), ('rw', 'en'),
            ('en', 'mg'), ('mg', 'en'),
            ('en', 'ln'), ('ln', 'en'),
            ('en', 'am'), ('am', 'en'),
            ('en', 'so'), ('so', 'en'),
            
            # Some direct European pairs
            ('es', 'fr'), ('fr', 'es'),
            ('de', 'fr'), ('fr', 'de'),
            ('es', 'pt'), ('pt', 'es'),
        ]
        
        return priority_models + additional_models
    
    def get_all_models(self):
        """Get all models from the mapping"""
        from translator.services.translation_service import translation_service
        return list(translation_service.model_mapping.keys())
    
    def get_memory_usage(self):
        """Get current memory usage in MB"""
        process = psutil.Process()
        return round(process.memory_info().rss / 1024 / 1024, 1)