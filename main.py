from celery import Celery
import config
def create_celery():
  app = Celery("celery_demo",backend=config.CELERY_RESULT_BACKEND,broker=config.CELERY_BROKER_URL)
  app.config_from_object(config)
  return app

app = create_celery()