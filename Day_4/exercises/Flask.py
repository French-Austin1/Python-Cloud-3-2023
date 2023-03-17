from flask import Flask, render_template


def exercise_1():
    '''Create a Flask application that returns "Hello, World!"
    when the root URL is requested (/). Use the @app.route decorator to define the route.'''
    app = Flask(__name__)

    @app.route('/')
    def method_name():
        return "<h1>Hello, World!</h1>"
    
    return app
    

def exercise_2():
    '''Create a Flask application that uses an HTML template to render a simple webpage.
    The webpage should include a header, a paragraph of text, and an image.
    You can use the render_template function to render the HTML template.'''
    app = Flask(__name__)
    @app.route('/')
    @app.route('/home')
    def method_name():
        return render_template("home.html")
    
    return app

def exercise_3():
    '''Create a Flask application that includes API endpoints for retrieving and updating data. The application should 
    use the Flask-RESTful extension to define the endpoints.
    You can use a simple data structure like a dictionary to store the data.
    '''
    pass


if __name__ == "__main__":
    app = exercise_1()
    app.run()