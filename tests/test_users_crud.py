"""
User CRUD Operations Tests
Tests for basic user management endpoints
"""

import pytest
from utils.validators import ResponseValidator
from utils.api_endpoints import APIEndpoints
from data.test_data import TestData

class TestUsersCRUD:
    """
    Test suite for user CRUD operations
    
    Coverage:
    - GET all users
    - GET single user by ID
    - POST create user
    - PUT update user
    - PATCH partial update
    - DELETE user
    """
    
    def test_get_all_users(self, api_client):
        """
        Test: GET all users returns list
        
        Validates:
        - Status code 200
        - Response is list
        - List contains users
        - Response time under 2s
        """
        response = api_client.get(APIEndpoints.USERS)
        
        # Layer 1: Status code
        ResponseValidator.validate_status_code(response, 200)
        
        # Layer 2: Response time
        ResponseValidator.validate_response_time(response, TestData.MAX_RESPONSE_TIME_GET)
        
        # Layer 3: Content type
        ResponseValidator.validate_content_type(response)
        
        # Layer 4: Data structure
        data = response.json()
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "User list should not be empty"
        
        # Layer 5: First user has required fields
        first_user = data[0]
        ResponseValidator.validate_field_exists(first_user, "id")
        ResponseValidator.validate_field_exists(first_user, "name")
        ResponseValidator.validate_field_exists(first_user, "email")
    
    def test_get_single_user(self, api_client):
        """
        Test: GET single user by valid ID
        
        Validates:
        - Status code 200
        - Returns single user object
        - Schema validation
        - User ID matches requested ID
        """
        user_id = TestData.VALID_USER_ID
        endpoint = APIEndpoints.USER_BY_ID.format(user_id=user_id)
        
        response = api_client.get(endpoint)
        
        ResponseValidator.validate_status_code(response, 200)
        ResponseValidator.validate_response_time(response, TestData.MAX_RESPONSE_TIME_GET)
        
        data = response.json()
        
        # Validate schema
        assert ResponseValidator.validate_json_schema(data, TestData.USER_SCHEMA), \
            "Response doesn't match user schema"
        
        # Validate specific user
        assert data["id"] == user_id, f"Expected user ID {user_id}, got {data['id']}"
        ResponseValidator.validate_not_empty(data, "name")
        ResponseValidator.validate_not_empty(data, "email")
    
    def test_get_user_not_found(self, api_client):
        """
        Test: GET user with invalid ID returns 404
        
        Negative test case
        """
        invalid_id = TestData.INVALID_USER_ID
        endpoint = APIEndpoints.USER_BY_ID.format(user_id=invalid_id)
        
        response = api_client.get(endpoint)
        
        ResponseValidator.validate_status_code(response, 404)
    
    def test_create_user(self, api_client, created_resources):
        """
        Test: POST create new user
        
        Validates:
        - Status code 201 (Created)
        - Response contains created user data
        - User has generated ID
        """
        response = api_client.post(APIEndpoints.USERS, json=TestData.VALID_USER_CREATE)
        
        ResponseValidator.validate_status_code(response, 201)
        ResponseValidator.validate_response_time(response, TestData.MAX_RESPONSE_TIME_POST)
        
        data = response.json()
        
        # Validate created data
        ResponseValidator.validate_field_exists(data, "id")
        ResponseValidator.validate_field_type(data, "id", int)
        
        # Validate request data is in response
        assert data["name"] == TestData.VALID_USER_CREATE["name"]
        assert data["email"] == TestData.VALID_USER_CREATE["email"]
        
        # Track for cleanup (though JSONPlaceholder doesn't persist)
        created_resources.append(("user", data["id"]))
    
    def test_update_user(self, api_client):
        """
        Test: PUT update existing user
        
        Validates:
        - Status code 200
        - Updated data returned
        """
        user_id = TestData.VALID_USER_ID
        endpoint = APIEndpoints.USER_BY_ID.format(user_id=user_id)
        
        response = api_client.put(endpoint, json=TestData.VALID_USER_UPDATE)
        
        ResponseValidator.validate_status_code(response, 200)
        
        data = response.json()
        assert data["name"] == TestData.VALID_USER_UPDATE["name"]
    
    def test_delete_user(self, api_client):
        """
        Test: DELETE user
        
        Validates:
        - Status code 200 (JSONPlaceholder returns 200, not 204)
        """
        user_id = TestData.VALID_USER_ID
        endpoint = APIEndpoints.USER_BY_ID.format(user_id=user_id)
        
        response = api_client.delete(endpoint)
        
        ResponseValidator.validate_status_code(response, 200)
        