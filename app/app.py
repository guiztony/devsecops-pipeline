from flask import Flask

app = Flask(__name__)

# FAILLE 1 : Clé API en dur dans le code
SECRET_API_KEY = "sk-prod-1234567890abcdef"
DB_PASSWORD = "admin123"

@app.route('/')
def home():
    return "<h1>Hello, DevSecOps World!</h1>", 200

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
