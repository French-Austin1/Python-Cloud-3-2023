from flask import Flask

# Creates a Flask object
app = Flask(__name__)

# Use the route decorator to change the functionality of this method.
@app.route('/')
def method_name():
    return '<h1>Hello</h1>'

if __name__ == "__main__":
    app.run(debug = True)
