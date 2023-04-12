import pytest
import flask_app
from flask_login import login_user

@pytest.mark.parametrize('username, password, password_verif, expected',
[
    ('test', 'test', 'test', b'success'),
    ('test', 'test', 'test', b'taken'),
    ('ADCDEFG', 'test', 'test', b'success'),
    ('abcdefg', 'test', 'test', b'success'),
    ('ADCDEFG', 'test', 'test', b'taken')
    ('Veri','Veri','verification',b'not match')
])
def test_error_register(app, test_client, username, password, password_verif, expected) :

    """ GIVEN register is functional
        WHEN username is not unique 
        THEN return error message that the username is not unique
        WHEN the password verification does not match
        THEN return error message that the password does not match """

    with app.app_context():
        test_client.post('/register',data=dict
        (
            username=username,
            password=password,
            password_verif=password_verif
        ))
        response = test_client.get('/register', content_type='html/text')
        assert expected in response.data.decode()

