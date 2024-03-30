# Import Flask Webserver, and Liquid Templating
from flask import Flask
from liquid import Template, Environment, FileSystemLoader

# Create a new Flask Application
app = Flask(__name__)

# Create a Environment for the Templates, and load Them
env = Environment(loader=FileSystemLoader("templates/"))
card = env.get_template("card.html")
structure = env.get_template("structure.html")

# TODO: Fetch a List with all Games and Their Statuses
# Create a List for the Templates
games = [
	{
		"name": "Visual Studio Code",
		"description": "Code editing. Redefined. A simple yet powerful code editor for almost all languages",
		"icon": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Firefox_logo%2C_2019.svg",
		"color": "#03bafc",
	},
	{
		"name": "Visual Studio Code",
		"description": "Code editing. Redefined. A simple yet powerful code editor for almost all languages",
		"icon": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Firefox_logo%2C_2019.svg",
		"color": "#03bafc",
	},
]

@app.route('/')
def index_page():
	return structure.render(games=games)

if __name__ == '__main__':
	app.run()