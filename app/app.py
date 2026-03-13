from flask import Flask

app = Flask(_name_)

# FAILLE : Clé API en dur dans le code
SECRET_API_KEY = "sk-prod-1234567890abcdef"
DB_PASSWORD = "admin123"

@app.route('/')
def home():
    return "<h1>Hello, DevSecOps World!</h1>", 200

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
