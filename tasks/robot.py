from main import app

@app.task
def test():
  print(1)
  