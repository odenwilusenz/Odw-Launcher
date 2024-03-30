# Documentation
welcome to the documentation, the api is hosted on the 5000 port of the host device and it isnt acessible from any other devices


## /getgame?game=[gamename]
Function: GET
This action has 1 parameter its "game" you need to set this to the game name you got from /gamelist or /localgameslist it will get the game from the ODW server


## /gamelist
Function: GET
This action gets all availible games and their config in a json format like
<ul>
  <li>name: the name of the game/application</li>
  <li>version: the version of the distro</li>
  <li>runfile: the location of the file required to run the game</li>
  <li>icon: the path of the icon</li>
  <li>color: the color of the game page</li>
  <li>tags: the tags of the application (unused)</li>
  <li>modifyFiles: unused will be added later</li>
  
</ul>
