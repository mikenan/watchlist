from flask import Flask,render_template
app = Flask(__name__)

name = 'nan'
movies = [
	{'title':'play game','year':1988},
]

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)
