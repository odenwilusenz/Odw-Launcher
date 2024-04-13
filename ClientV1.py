from flask import Flask, jsonify, request, send_file, abort, send_from_directory
import os
import subprocess
import json
import random
from distutils.dir_util import copy_tree

# rootDir = "C:\\Users\myros\Desktop"
# rootDir = "\\\\ODW-Master-01\public\odwLauncher_games"
app = Flask(__name__)

try:
    os.mkdir(os.path.expanduser('~') + "\\odwlauncher")  # Create tmp directory if
except:
    pass
homedir = os.path.expanduser('~') + "\\odwlauncher"

try:
    os.mkdir(os.path.expanduser('~') + "\\odwlauncher\\Games")
except:
    pass

try:
    os.mkdir(os.path.expanduser('~') + "\\odwlauncher\\Memes")
except:
    pass

try:
    os.mkdir(os.path.expanduser('~') + "\\odwlauncher\\Pictures")
except:
    pass


@app.before_request
def limit_remote_addr():
    if request.remote_addr != '127.0.0.1':
        return("Not Allowed", 401)  # Forbidden


@app.route('/', methods=['GET'])
def index():
    html_file = open("index.html", "r")
    return html_file.read()


@app.route('/favicon.ico')  # TODO fix
def favicon():
    print(os.path.join(app.root_path, 'favicon.ico'))
    return send_from_directory(os.path.join(app.root_path, ''), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# @app.route('/gameIsLocal/<gameName>', methods=['GET'])
# def isGameLocal(gameName):
#    return random.choice([True, False])


@app.route('/gameIsLocal', methods=['GET'])
def isGameLocal():
    rbool = random.choice([True, False])
    if rbool:
        return f"true"
    return f"false"


@app.route('/getGame', methods=['GET'])
def get_game():
    gameName = request.args.get('game')
    print(f"Downloading Game with the name {gameName}")
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            if file == "odw_config.json":
                f = open(os.path.join(subdir, file))
                data = json.load(f)
                print(data["name"])
                print(subdir)
                if data["name"] == gameName:
                    copy_tree(subdir, os.path.expanduser('~') + f"\\odwlauncher\\games\\{gameName}")
                    return f"downloading game at {subdir}"

                f.close


@app.route('/startGame', methods=['GET'])
def start_game():
    gameName = request.args.get('game')
    print(f"Playing Game with the name {gameName}")
    for subdir, dirs, files in os.walk(homedir + "\\games"):
        for file in files:
            if file == "odw_config.json":
                f = open(os.path.join(subdir, file))
                data = json.load(f)
                print(data["runfile"])
                print(subdir)
                if data["name"] == gameName:
                    print(subdir + "\\" + data["runfile"])
                    try:
                        subprocess.run(subdir + "\\" + data["runfile"], check=True)
                    except subprocess.CalledProcessError as e:
                        return f"Error Running Game {e}"
                    return f"running game at {subdir}"
                    f.close


@app.route('/gameList', methods=['GET'])
def list_games():
    listOfGames = []
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            if file == "odw_config.json":
                f = open(os.path.join(subdir, file))
                data = json.load(f)
                listOfGames += [data]
                f.close
    return (listOfGames)


app.run()
