"""
Response Validators
Reusable validation functions for API responses
"""

from jsonschema import validate, ValidationError
import requests

class ResponseValidator:
    """
    Utility class for validating API responses
    
    Purpose:
    - Centralizes common validations
    - Makes tests more readable
    - Provides clear error messages
    - Reduces code duplication
    
    Usage:
    Use in all test assertions to validate:
    - Status codes
    - Response schemas
    - Response times
    - Data types
    
    Example:
        ResponseValidator.validate_status_code(response, 200)
        ResponseValidator.validate_response_time(response, 2000)
    """
    
    @staticmethod
    def validate_status_code(response: requests.Response, expected_code: int):
        """
        Validate HTTP status code
        
        Args:
            response: Response object from requests
            expected_code: Expected status code (e.g., 200, 201, 404)
            
        Raises:
            AssertionError: If status code doesn't match
            
        Example:
            ResponseValidator.validate_status_code(response, 200)
        """
        assert response.status_code == expected_code, \
            f"Expected status {expected_code}, got {response.status_code}. Response: {response.text}"
    
    @staticmethod
    def validate_json_schema(response_json: dict, schema: dict) -> bool:
        """
        Validate response JSON against a schema
        
        Args:
            response_json: JSON response as dict
            schema: JSON schema to validate against
            
        Returns:
            True if valid, False otherwise
            
        Purpose:
        - Ensures API returns expected structure
        - Catches API changes early
        - Documents expected response format
        
        Example:
            schema = {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
                "required": ["id", "name"]
            }
            ResponseValidator.validate_json_schema(response.json(), schema)
        """
        try:
            validate(instance=response_json, schema=schema)
            return True
        except ValidationError as e:
            print(f"Schema validation failed: {e.message}")
            print(f"Failed at path: {list(e.path)}")
            return False
    
    @staticmethod
    def validate_response_time(response: requests.Response, max_time_ms: int):
        """
        Validate response time is within acceptable limit
        
        Args:
            response: Response object
            max_time_ms: Maximum acceptable time in milliseconds
            
        Raises:
            AssertionError: If response time exceeds limit
            
        Purpose:
        - Performance testing
        - Ensures API meets SLA requirements
        - Catches performance regressions
        
        Example:
            ResponseValidator.validate_response_time(response, 2000)  # Max 2 seconds
        """
        response_time_ms = response.elapsed.total_seconds() * 1000
        assert response_time_ms < max_time_ms, \
            f"Response time {response_time_ms:.2f}ms exceeds limit of {max_time_ms}ms"
    
    @staticmethod
    def validate_content_type(response: requests.Response, expected_type: str = "application/json"):
        """
        Validate response Content-Type header
        
        Args:
            response: Response object
            expected_type: Expected content type (default: "application/json")
            
        Raises:
            AssertionError: If content type doesn't match
            
        Purpose:
        - Ensures API returns correct format
        - Important for integration with frontend
        """
        content_type = response.headers.get("Content-Type", "")
        assert expected_type in content_type, \
            f"Expected Content-Type '{expected_type}', got '{content_type}'"
    
    @staticmethod
    def validate_field_exists(response_json: dict, field_name: str):
        """
        Validate that a field exists in response
        
        Args:
            response_json: JSON response as dict
            field_name: Name of field to check
            
        Raises:
            AssertionError: If field doesn't exist
            
        Example:
            ResponseValidator.validate_field_exists(response.json(), "id")
        """
        assert field_name in response_json, \
            f"Field '{field_name}' not found in response. Available fields: {list(response_json.keys())}"
    
    @staticmethod
    def validate_field_type(response_json: dict, field_name: str, expected_type: type):
        """
        Validate field type in response
        
        Args:
            response_json: JSON response as dict
            field_name: Name of field to check
            expected_type: Expected Python type (int, str, list, dict, etc.)
            
        Raises:
            AssertionError: If field type doesn't match
            
        Example:
            ResponseValidator.validate_field_type(response.json(), "id", int)
            ResponseValidator.validate_field_type(response.json(), "users", list)
        """
        ResponseValidator.validate_field_exists(response_json, field_name)
        actual_type = type(response_json[field_name])
        assert actual_type == expected_type, \
            f"Field '{field_name}' expected type {expected_type.__name__}, got {actual_type.__name__}"
    
    @staticmethod
    def validate_not_empty(response_json: dict, field_name: str):
        """
        Validate that a field is not empty
        
        Args:
            response_json: JSON response as dict
            field_name: Name of field to check
            
        Raises:
            AssertionError: If field is empty (empty string, list, dict, or None)
            
        Purpose:
        - Ensures API returns actual data
        - Catches null/empty responses
        
        Example:
            ResponseValidator.validate_not_empty(response.json(), "name")
        """
        ResponseValidator.validate_field_exists(response_json, field_name)
        value = response_json[field_name]
        assert value not in [None, "", [], {}], \
            f"Field '{field_name}' is empty: {value}"
            