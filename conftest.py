"""
Pytest Configuration and Fixtures
Shared test setup and teardown logic
"""

import pytest
from utils.api_client import APIClient
from utils.api_endpoints import APIEndpoints

@pytest.fixture(scope="session")
def api_client():
    """
    Create API client for entire test session
    
    Scope: session - created once for all tests
    
    Purpose:
    - Provides configured API client to all tests
    - Reuses HTTP session for performance
    - Auto-cleanup after tests complete
    
    Usage in test:
        def test_something(api_client):
            response = api_client.get("/users")
    """
    client = APIClient(APIEndpoints.BASE_URL)
    yield client
    client.close()

@pytest.fixture(scope="function")
def created_resources():
    """
    Track created resources for cleanup
    
    Scope: function - new list for each test
    
    Purpose:
    - Store IDs of created resources during test
    - Auto-cleanup after test completes
    - Keeps test environment clean
    
    Usage:
        def test_create_user(api_client, created_resources):
            response = api_client.post("/users", json=data)
            user_id = response.json()["id"]
            created_resources.append(("user", user_id))
    """
    resources = []
    yield resources
    # Cleanup happens here (though JSONPlaceholder doesn't persist)
    # In real API, you'd delete created resources
    