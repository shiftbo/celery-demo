# coding=utf-8
from celery.schedules import crontab
from datetime import timedelta

# CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_ENABLE_UTC = False
#BROKER中间人(任务队列)
CELERY_BROKER_URL = "redis://localhost:6379/0"
#RESULT_BACKEND(存放处)
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"

CELERY_IMPORTS = ["tasks.robot"]
CELERY_DEFAULT_QUEUE = 'robot'
CELERY_DEFAULT_EXCHANGE = 'robot'
CELERY_DEFAULT_ROUTING_KEY = 'robot'
CELERYBEAT_SCHEDULE = {
    "robot":{
        "task":"tasks.robot.test",
        "schedule":timedelta(seconds=1)
    }
}
