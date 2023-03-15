from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('Home.html') # This will return this template in the templates directory

if __name__ == "__main__":
    app.run(debug=True)