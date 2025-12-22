"""
Test Data Management
Centralized test data for API tests
"""

class TestData:
    """
    Test data storage for JSONPlaceholder API tests
    
    Purpose:
    - Single source of truth for test data
    - Easy to update across all tests
    - Separates data from test logic
    - Makes tests more readable
    
    Usage:
        new_user = TestData.VALID_USER_CREATE
        response = client.post("/users", json=new_user)
    """
    
    # Valid user data for creation
    VALID_USER_CREATE = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com",
        "phone": "1-234-567-8901",
        "website": "johndoe.com"
    }
    
    # Valid user data for update
    VALID_USER_UPDATE = {
        "name": "Jane Smith",
        "username": "janesmith",
        "email": "jane.smith@example.com"
    }
    
    # Valid post data
    VALID_POST_CREATE = {
        "title": "Test Post Title",
        "body": "This is a test post body with some content.",
        "userId": 1
    }
    
    # Valid comment data
    VALID_COMMENT_CREATE = {
        "name": "Test Comment",
        "email": "commenter@example.com",
        "body": "This is a test comment."
    }
    
    # Invalid data for negative testing
    INVALID_USER_MISSING_NAME = {
        "username": "testuser",
        "email": "test@example.com"
    }
    
    INVALID_USER_EMPTY_EMAIL = {
        "name": "Test User",
        "username": "testuser",
        "email": ""
    }
    
    # Edge case data
    USER_WITH_SPECIAL_CHARS = {
        "name": "José María O'Brien",
        "username": "jose_maria",
        "email": "jose.maria@example.com"
    }
    
    USER_WITH_LONG_NAME = {
        "name": "A" * 100,  # 100 character name
        "username": "longname",
        "email": "long@example.com"
    }
    
    # JSON Schemas for validation
    USER_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string", "format": "email"},
            "phone": {"type": "string"},
            "website": {"type": "string"}
        },
        "required": ["id", "name", "username", "email"]
    }
    
    POST_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "userId": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["id", "userId", "title", "body"]
    }
    
    COMMENT_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "postId": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["id", "postId", "name", "email", "body"]
    }
    
    USERS_LIST_SCHEMA = {
        "type": "array",
        "items": USER_SCHEMA,
        "minItems": 1
    }
    
    # Test IDs for different scenarios
    VALID_USER_ID = 1
    VALID_POST_ID = 1
    INVALID_USER_ID = 99999
    INVALID_POST_ID = 99999
    
    # Expected response times (milliseconds)
    MAX_RESPONSE_TIME_GET = 3000  # 3 seconds
    MAX_RESPONSE_TIME_POST = 3000  # 3 seconds
    
    