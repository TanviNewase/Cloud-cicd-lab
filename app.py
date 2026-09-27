from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Automatic CI/CD Deployment is Working!"

@app.route("/student")
def student():
    return "Student Service is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)