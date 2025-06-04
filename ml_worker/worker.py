from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery = Celery("ml_worker", broker=REDIS_URL, backend=REDIS_URL)

from tasks import training, inference
#celery.autodiscover_tasks(['tasks.training', 'tasks.inference'])
