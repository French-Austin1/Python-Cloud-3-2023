from website import create_app
# Importing the website module

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
