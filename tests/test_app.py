
import os
import sys
import pytest
from flask import Flask
from app import create_app, init_db
from app.routes.routes import configure_routes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def start_app():
    app = Flask(__name__)
    app = create_app()
    db = init_db(app)
    configure_routes(app, db)
    return app

@pytest.fixture
def client():
    app = start_app()
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_ask_question(client):
    """Test the ask question route"""

    response = client.post("/ask", json={"question": "What is the capital of France?"})
    assert response.status_code == 200
    data = response.get_json()
    assert data['answer'] == 'The capital of France is Paris.'