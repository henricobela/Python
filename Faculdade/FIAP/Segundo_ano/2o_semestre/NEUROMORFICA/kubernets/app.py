from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello, this is a simple Flask app!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)