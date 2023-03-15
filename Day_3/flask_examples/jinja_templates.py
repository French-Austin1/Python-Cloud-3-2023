from flask import Flask, render_template

app = Flask(__name__)
names = ["Austin", "Tyler", "Bryan"] 

@app.route('/')
def render():
    return render_template('extension.html', names = names) # passing the name var into the template for jinja2 to use.

if __name__ == "__main__":
    app.run(debug=True)