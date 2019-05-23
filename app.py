
# https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Python"

    return "Hello ali bhai !"



app.run(debug=True)