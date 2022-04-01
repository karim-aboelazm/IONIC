from flask_cors import cross_origin
from flask import Flask,render_template,request
from assistant import assistant,Listen_name

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        Listen_name()
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
