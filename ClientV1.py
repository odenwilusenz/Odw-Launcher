from flask import Flask, jsonify, request,send_file,abort
import os
import subprocess
import json
from distutils.dir_util import copy_tree

rootdir = "\\\\ODW-Master-01\public\odwLauncher_games"


app = Flask(__name__)



try:
    os.mkdir(os.path.expanduser('~') + "\\odwlauncher")  # Create tmp directory if
except: pass
homedir = os.path.expanduser('~') + "\\odwlauncher"

try:
    os.mkdir(os.path.expanduser('~') + "\\odwlauncher\\games")
except: pass


@app.before_request
def limit_remote_addr():
    if request.remote_addr != '127.0.0.1':
        app.abort(403)  # Forbidden




@app.route('/getgame', methods = ['GET'])
def get_game():
    gamename = request.args.get('game')
    print(f"Downloading Game with the name {gamename}")
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == "odw_config.json":
                f = open(os.path.join(subdir, file))
                data = json.load(f)
                print(data["name"])
                print(subdir)
                if  data["name"] == gamename:
                    copy_tree(subdir, os.path.expanduser('~') + f"\\odwlauncher\\games\\{gamename}")
                    return(f"downloading game at {subdir}")
                    
                
                f.close
    

@app.route('/startgame', methods = ['GET'])
def start_game():
    gamename = request.args.get('game')
    print(f"Playing Game with the name {gamename}")
    for subdir, dirs, files in os.walk(homedir + "\\games"):
        for file in files:
            if file == "odw_config.json":
                f = open(os.path.join(subdir, file))
                data = json.load(f)
                print(data["runfile"])
                print(subdir)
                if  data["name"] == gamename:
                    print(subdir + "\\" + data["runfile"])
                    try:
                        subprocess.run(subdir + "\\" + data["runfile"], check=True)
                    except subprocess.CalledProcessError as e:
                        return(f"Error Running Game {e}")
                    return(f"running game at {subdir}")
                    f.close
                
                    
        
    
    



@app.route('/gamelist', methods = ['GET'])
def list_games():
    listofgames = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == "odw_config.json":
                f = open(os.path.join(subdir, file))
                data = json.load(f)
                listofgames += [data]
                f.close
    return(listofgames)
                    
                
    


        


app.run()