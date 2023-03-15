from website import create_app

def test_home_page():
    '''
    GIVEN a flask application
    WHEN the '/' page is requested
    THEN check that the response is valid
    '''
    
    flask_app = create_app()
    
    with flask_app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Posts" in response.data
        assert b"Login" in response.data
        assert b"Sign up" in response.data
        
def test_home_page_post():
    '''
    GIVEN a flask application
    WHEN the '/' page is requested as POST
    THEN check that the response is invalid
    '''
    
    flask_app = create_app()
    
    with flask_app.test_client() as client:
        response = client.post('/')
        assert response.status_code == 405

def test_login_page():
    '''
    GIVEN a flask application
    WHEN the '/login' page is requested
    THEN check that the response is valid
    '''

    flask_app = create_app()

    with flask_app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200
        assert b"Login" in response.data
        assert b"Email" in response.data
        assert b"Password" in response.data

def test_about_page():
    '''
    GIVEN a flask application
    WHEN the '/about' page is requested
    THEN check that the response is valid
    '''

    flask_app = create_app()

    with flask_app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
        assert b"Welcome to the about page" in response.data
        assert b"The Flask Blog" in response.data
        assert b"Login" in response.data

def test_sign_up_page():
    '''
    GIVEN a flask application
    WHEN the '/sign-up' page is requested
    THEN check that the response is valid
    '''

    flask_app = create_app()

    with flask_app.test_client() as client:
        response = client.get('/sign-up')
        assert response.status_code == 200
        assert b"Email" in response.data
        assert b"Password" in response.data
        assert b"Username" in response.data
        assert b"Confirm Password" in response.data

def test_admin_page():
    '''
    GIVEN a flask application
    WHEN the '/admin' page is requested and User is Admin
    THEN check that the response is valid
    '''

    flask_app = create_app()

    with flask_app.test_client() as client:
        client.post('/login', data={'email': 'admin@mysite.com', 'password': 'ab12cd'})
        response = client.get('/admin')
        assert response.status_code == 200
        assert b"Email" in response.data
        assert b"Username" in response.data
        assert b"admin" in response.data
        assert b"admin@mysite.com" in response.data
        assert b"Admin-page" in response.data