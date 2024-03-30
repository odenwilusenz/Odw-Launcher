# Import Flask Webserver
from flask import Flask, render_template

# Create a new Flask Application
app = Flask(__name__)


@app.route('/')
def index_page():
	return render_template("interface-template.html")

if __name__ == '__main__':
	app.run()