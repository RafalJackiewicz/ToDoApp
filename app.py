from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello {escape (name)}</p>"

if __name__ == "__main__":
    app.run(debug=True)
