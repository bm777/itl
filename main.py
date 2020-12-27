from flask import Flask, render_template

app = Flask(__name__)

# home page for 127.0.0.1:5000
# 127.0.0.1 Local ip address
# 5000 is default port adress
@app.route('/')
def main():
    return render_template('index.html')


# home page for 127.0.0.1:5000/cours
# 127.0.0.1 Local ip address
# 5000 is default port adress
@app.route('/cours/<name>')
def cours(name=None):

	tmp = name if name is not None else "None"
	return render_template("cours.html", name=tmp)
