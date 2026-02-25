from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "<h1>Hello, DevSecOps World!</h1>", 200

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)


**Les dépendances (app/requirements.txt) :**

flask==3.0.3
