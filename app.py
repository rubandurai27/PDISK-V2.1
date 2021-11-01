#from flask import Flask, request, jsonify,send_file,send_from_directory
import os

from flask import Flask, request, abort, jsonify, send_from_directory

UPLOAD_DIRECTORY = "templates/download"
from pynpm import NPMPackage
#import os

#from flask import Flask, request, abort, jsonify, send_from_directory

#UPLOAD_DIRECTORY = "/project/api_uploaded_files"

import subprocess
import requests

from bs4 import BeautifulSoup as BS

app = Flask(__name__)
subprocess.Popen('python3 bot.py', shell=True)

    
    #os.makedirs('/node_modules')
#subprocess.Popen('node index.js', shell=True)
#@app.route('/ni',methods=['GET'])
#@app.route('/ni',methods=['GET'])

#def indeegx():

   # w = request.args.get('url')
   # subprocess.Popen(f'npm start', shell=True)
@app.route("/files")

def list_files():

    """Endpoint to list files on the server."""

    files = []

    for filename in os.listdir(UPLOAD_DIRECTORY):

        path = os.path.join(UPLOAD_DIRECTORY, filename)

        if os.path.isfile(path):

            files.append(filename)

    return jsonify(files)

@app.route("/files/<path:path>")

def get_file(path):

    """Download a file."""

    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@app.route("/files/<filename>", methods=["POST"])

def post_file(filename):

    """Upload a file."""

    if "/" in filename:

        # Return 400 BAD REQUEST

        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:

        fp.write(request.data)

    # Return 201 CREATED

    return "", 201


@app.route('/getmsg/', methods=['GET'])

def respond():

    # Retrieve the name from url parameter

    name = request.args.get("name", None)

    # For debugging

    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all

    if not name:

        response["ERROR"] = "no name found, please send a name."

    # Check if the user entered a number not a name

    elif str(name).isdigit():

        response["ERROR"] = "name can't be numeric."

    # Now the user entered a valid name

    else:

        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format

    return jsonify(response)
@app.route('/u',methods=['GET'])

def indeegx():

    w = request.args.get('url')
    subprocess.Popen('node index.js', shell=True)
#@app.route('/ni',methods=['GET'])
    return send_from_directory(f"templates/download/{w}",filename=w)

@app.route('/post/', methods=['POST'])

def post_something():

    param = request.form.get('name')

    print(param)

    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality

    if param:

        return jsonify({

            "Message": f"Welcome {name} to our awesome platform!!",

            # Add this option to distinct the POST request

            "METHOD" : "POST"

        })

    else:

        return jsonify({

            "ERROR": "no name found, please send a name."

        })

# A welcome message to test our server


@app.route('/')

def index():
   # c = subprocess.getoutput(f"python3 bot.py")
    return "<h1>Telegram link Generator !!</h1> <!-- Bidvertiser2051838 -->"

@app.route('/index.page')

def indeeeex():

    return "<h1>Telegram link Generator !!</h1> <!-- Bidvertiser2051838 -->"

@app.route('/e')

def indeex():

    w = request.args.get('url')

    e = f"http://m.pdisk.net/share-video?videoid={w}"

    r = requests.get(e)

    page = requests.get(e)

    v = page.text

    soup = BS(page.text)

    video = soup.find("video")

    SRC = soup.find("video").get("src")

    return f'''

    <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <!-- Compiled and minified CSS -->

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->

    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

            

    <nav>

    <div class="nav-wrapper">

      <a href="#" class="brand-logo" style="width:100%">Telegram linkGenerator</a>

    </div>

  </nav>

    <div>

    <a href="{SRC}" target="_parent"><button>Download Now !</button></a>

    <video src='{SRC}' width="320" height="240" controls ></video>

    </div>

    

    
    <!-- Bidvertiser2051838 -->
    <script type="text/javascript" src="https://uprimp.com/bnr.php?section=General&pub=938314&format=120x600&ga=g"></script>

<noscript><a href="https://yllix.com/publishers/938314" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub/120x600.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" alt="ylliX - Online Advertising Network" /></a></noscript>

    <script type="text/javascript" src="https://uprimp.com/bnr.php?section=General&pub=938314&format=468x60&ga=g"></script>

<noscript><a href="https://yllix.com/publishers/938314" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub/468x60.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" alt="ylliX - Online Advertising Network" /></a></noscript>
<a style="color:red"> No copyright issues this link are owned pdisk this website is only generating direct link</p>'''

if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support

    app.run(threaded=True, port=5000)
