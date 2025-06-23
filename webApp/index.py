from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask'

@app.route('/sub1')
def sub1():
    return 'SUB1 Page'

@app.route('/demoHtml')
def index():
    return render_template('index_html.html')

@app.route('/methodGet', methods = ['GET'])
def method_get():
    return render_template('method_get.html')

@app.route('/method_get_act', methods = ['GET'])
def method_get_act():
    if request.method == 'GET':
        id = request.args["id"]
        password = request.args.get("password")
        return render_template('method_get.html', id = id, password = password)

if __name__ == '__main__':
    app.run(debug = True, port = 80, host = '0.0.0.0')