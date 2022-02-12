import pytest

from main import app

client = app.test_client()

def test_main_page():
    response = client.get("/", content_type='application/json')
    assert(response.status_code, 200)
    assert(response.data, "Welcome to the Docker-ecr-kubernetes app")
