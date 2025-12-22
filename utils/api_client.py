"""
API Client - Wrapper for HTTP requests
Simplifies making API calls with consistent error handling
"""

import requests
from typing import Optional, Dict, Any

class APIClient:
    """
    HTTP client wrapper for API testing
    
    Purpose:
    - Centralizes all HTTP calls (GET, POST, PUT, DELETE)
    - Manages sessions (cookies, persistent headers)
    - Simplifies test code
    - Facilitates logging and debugging
    
    Usage:
    - Use in ALL API tests
    - Replaces direct requests.get() calls in tests
    
    Notes:
    - Always close session after use
    - Handle timeouts to avoid hanging tests
    """
    
    def __init__(self, base_url: str, timeout: int = 10):
        """
        Initialize API client
        
        Args:
            base_url: API base URL (e.g., "https://jsonplaceholder.typicode.com")
            timeout: Request timeout in seconds (default: 10s)
        """
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        
        # Default headers for all requests
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        """
        Send GET request
        
        Args:
            endpoint: Relative endpoint (e.g., "/users/1")
            params: Optional query parameters (e.g., {"page": 2})
            
        Returns:
            Response object with status_code, json(), etc.
            
        Example:
            response = client.get("/users", params={"page": 2})
            users = response.json()
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        return response
    
    def post(self, endpoint: str, json: Optional[Dict] = None) -> requests.Response:
        """
        Send POST request (create resources)
        
        Args:
            endpoint: Relative endpoint
            json: JSON payload to send
            
        Returns:
            Response object
            
        Example:
            new_user = {"name": "John", "email": "john@test.com"}
            response = client.post("/users", json=new_user)
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=json, timeout=self.timeout)
        return response
    
    def put(self, endpoint: str, json: Optional[Dict] = None) -> requests.Response:
        """
        Send PUT request (update resources)
        
        Args:
            endpoint: Relative endpoint
            json: JSON payload to update
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=json, timeout=self.timeout)
        return response
    
    def patch(self, endpoint: str, json: Optional[Dict] = None) -> requests.Response:
        """
        Send PATCH request (partial update)
        
        Args:
            endpoint: Relative endpoint
            json: JSON payload with fields to update
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, json=json, timeout=self.timeout)
        return response
    
    def delete(self, endpoint: str) -> requests.Response:
        """
        Send DELETE request (remove resources)
        
        Args:
            endpoint: Relative endpoint
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=self.timeout)
        return response
    
    def close(self):
        """
        Close HTTP session
        
        Usage:
        - Call at end of each test
        - Better: use as context manager (with statement)
        """
        self.session.close()
    
    def __enter__(self):
        """Context manager support"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Auto-close session when using 'with' statement"""
        self.close()
        
        