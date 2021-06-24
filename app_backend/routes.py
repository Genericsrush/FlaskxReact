from app_backend import app

@app.route("/")
def index():
    return "Welcome to flask"