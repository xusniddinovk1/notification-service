from config.celery import app

@app.task
def test_task():
    print("Celery is working")
    return "Ok"