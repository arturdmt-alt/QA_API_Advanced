"""
API Endpoints Configuration
JSONPlaceholder API - Fake REST API for testing and prototyping
Base URL: https://jsonplaceholder.typicode.com
"""

class APIEndpoints:
    """
    Centralized endpoint definitions for JSONPlaceholder API
    
    Why this matters:
    - Single source of truth for all URLs
    - Easy to update if API changes
    - Prevents typos in test files
    - Makes tests more readable
    """
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # User endpoints
    USERS = "/users"
    USER_BY_ID = "/users/{user_id}"
    
    # Post endpoints
    POSTS = "/posts"
    POST_BY_ID = "/posts/{post_id}"
    USER_POSTS = "/posts?userId={user_id}"
    
    # Comment endpoints
    COMMENTS = "/comments"
    COMMENT_BY_ID = "/comments/{comment_id}"
    POST_COMMENTS = "/posts/{post_id}/comments"
    
    # Album endpoints
    ALBUMS = "/albums"
    ALBUM_BY_ID = "/albums/{album_id}"
    USER_ALBUMS = "/albums?userId={user_id}"
    
    # Photo endpoints
    PHOTOS = "/photos"
    PHOTO_BY_ID = "/photos/{photo_id}"
    
    @staticmethod
    def get_full_url(endpoint):
        """
        Build complete URL
        
        Example:
        get_full_url("/users") → "https://jsonplaceholder.typicode.com/users"
        """
        return f"{APIEndpoints.BASE_URL}{endpoint}"
    
    