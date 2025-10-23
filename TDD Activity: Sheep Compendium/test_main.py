import sys
import os

# Fix for "ModuleNotFoundError: No module named 'main'"
# Adds the project root directory to the Python path so Pytest can find main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import TestClient to simulate API requests
from fastapi.testclient import TestClient
# Import the FastAPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app) 

# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response JSON matches the expected data
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

# Define a test function for adding a new sheep
def test_add_sheep():
    # Prepare the new sheep data in a dictionary format.
    new_sheep_data = {
        "id": 8, 
        "name": "Dolly",
        "breed": "Babydoll",
        "sex": "ewe"
    }

    # Send a POST request to the endpoint "/sheep" with the new sheep data.
    response = client.post("/sheep", json=new_sheep_data) 

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201 

    # Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep_data

    # Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    # Send a GET request to verify the addition
    verification_response = client.get("/sheep/8") 
    
    # Assert that the new sheep data can be retrieved successfully
    assert verification_response.json() == new_sheep_data