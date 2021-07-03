from flask import Flask
app = Flask(__name__)

@app.route('/lightning', methods = ['POST'])
def hello_world():
    return '----------->'


if __name__ == '__main__':
    app.run()