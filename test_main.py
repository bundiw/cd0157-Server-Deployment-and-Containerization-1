'''
Tests for jwt flask app.
'''
import os
import json
from dotenv import load_dotenv
import pytest

import main
load_dotenv()
SECRET = os.getenv('SECRET')
TOKEN = os.getenv('TOKEN')
EMAIL = os.getenv('EMAIL')
PASSWORD =os.getenv('PASSWORD')


@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
