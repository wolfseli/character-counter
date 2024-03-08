from flask import Flask, request, jsonify
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
     return send_file("web/index.html")  
   
@app.route("/sum")
def counter():
     # flask parameters with type and default
     n = request.args.get('n', default=1, type=str)
     # number of words
     words = len(n.split())
     # number of characters
     characters = len(n)
     # number of numbers
     numbers = sum(c.isdigit() for c in n)
     # number of punctuations
     punctuations = sum(c in "!@#$%^&*()_+{}[]|\\:;\"'<>?,./" for c in n)
     # combine all the results
     result = {"words": words, "characters": characters, "numbers": numbers, "punctuations": punctuations} 
     # return result as json
     return jsonify(result)
