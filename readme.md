#启动
celery -A main.app beat -l info
celery worker main.app -A -l info
