from website.models import User, Post, Comment

def test_new_user():
    '''
    GIVEN a user model
    WHEN a new user is created
    THEN check the email, password, and username fields are defined appropriately
    '''
    
    user = User(email='Austin3@gmail.com',password='abc123',username='Austin3')
    assert user.email == 'Austin3@gmail.com'
    assert user.password == 'abc123'
    assert user.username == 'Austin3'
    
def test_new_post():
    '''
    GIVEN a post model
    WHEN a new post is created by a user
    THEN check the post and user id are defined appropriately
    '''
    
    post = Post(text='hello world', author='4')
    
    assert post.author == '4'
    assert post.text == 'hello world'

def test_new_comment():
    '''
    GIVEN a post model
    WHEN a new post is created by a user
    THEN check the post and user id are defined appropriately
    '''
    
    comment = Comment(text='hello world', author='4', post_id='1')
    
    assert comment.author == '4'
    assert comment.text == 'hello world'
    assert comment.post_id == '1'