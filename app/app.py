from flask import Flask
import os

app = Flask(_name_)

# CORRECTION : utilisation de variables d environnement
SECRET_API_KEY = os.environ.get("SECRET_API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

@app.route('/')
def home():
    return "<h1>Hello, DevSecOps World!</h1>", 200

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)


