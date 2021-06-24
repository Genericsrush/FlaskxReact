from app_backend import app

@app.route("/")
def index():
    return {"name": "Hello world!!"}