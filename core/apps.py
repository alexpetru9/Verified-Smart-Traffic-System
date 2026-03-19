from django.apps import AppConfig
import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':
            return
            
        from django_apscheduler.jobstores import DjangoJobStore
        from apscheduler.schedulers.background import BackgroundScheduler
        from . import scheduler
        
        print("Starting Scheduler... (ONCE)")
        scheduler_instance = BackgroundScheduler()
        scheduler_instance.add_jobstore(DjangoJobStore(), "default")
        
        scheduler_instance.add_job(
            scheduler.simulation_tick_job,
            trigger='interval',
            seconds=1,
            id='simulation_tick_job',
            replace_existing=True
        )
        try:
            scheduler_instance.start()
        except Exception as e:
            print(f"Error starting scheduler: {e}")