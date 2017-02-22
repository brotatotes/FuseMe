
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return Flask.render_template('test.html')

if __name__ == "__main__":
    app.run()