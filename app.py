import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '</h1>'
    page += '</br>Greetings from Christian</br>'
    page += '</body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))