from celery import Celery

redis_host = "192.168.1.42"
redis_port = 6379
redis_password = ""


BROKER_URL = 'redis://192.168.1.42:6379/0'
app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):
    return x + y
