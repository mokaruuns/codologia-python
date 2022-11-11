from flask import Flask

app = Flask(__name__)


@app.route("/")
def showName():
    return "Steve from Minecraft"


app.run()
