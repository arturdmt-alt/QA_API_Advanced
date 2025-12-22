"""
Posts Tests
Tests for blog post endpoints
"""

import pytest
from utils.validators import ResponseValidator
from utils.api_endpoints import APIEndpoints
from data.test_data import TestData

class TestPosts:
    """
    Test suite for posts operations
    
    Coverage:
    - GET all posts
    - GET posts by user ID
    - GET single post
    - POST create post
    - Nested resources (comments)
    """
    
    def test_get_all_posts(self, api_client):
        """Test: GET all posts returns list"""
        response = api_client.get(APIEndpoints.POSTS)
        
        ResponseValidator.validate_status_code(response, 200)
        ResponseValidator.validate_response_time(response, TestData.MAX_RESPONSE_TIME_GET)
        
        data = response.json()
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "Posts list should not be empty"
        
        # Validate first post structure
        first_post = data[0]
        ResponseValidator.validate_field_exists(first_post, "id")
        ResponseValidator.validate_field_exists(first_post, "userId")
        ResponseValidator.validate_field_exists(first_post, "title")
        ResponseValidator.validate_field_exists(first_post, "body")
    
    def test_get_single_post(self, api_client):
        """Test: GET single post by ID"""
        post_id = TestData.VALID_POST_ID
        endpoint = APIEndpoints.POST_BY_ID.format(post_id=post_id)
        
        response = api_client.get(endpoint)
        
        ResponseValidator.validate_status_code(response, 200)
        
        data = response.json()
        assert ResponseValidator.validate_json_schema(data, TestData.POST_SCHEMA)
        assert data["id"] == post_id
    
    def test_get_posts_by_user(self, api_client):
        """Test: GET posts filtered by user ID"""
        user_id = TestData.VALID_USER_ID
        endpoint = APIEndpoints.USER_POSTS.format(user_id=user_id)
        
        response = api_client.get(endpoint)
        
        ResponseValidator.validate_status_code(response, 200)
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0, f"User {user_id} should have posts"
        
        # All posts should belong to requested user
        for post in data:
            assert post["userId"] == user_id, \
                f"Post {post['id']} belongs to user {post['userId']}, not {user_id}"
    
    def test_get_post_comments(self, api_client):
        """Test: GET comments for a post (nested resource)"""
        post_id = TestData.VALID_POST_ID
        endpoint = APIEndpoints.POST_COMMENTS.format(post_id=post_id)
        
        response = api_client.get(endpoint)
        
        ResponseValidator.validate_status_code(response, 200)
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0, f"Post {post_id} should have comments"
        
        # Validate comment structure
        first_comment = data[0]
        ResponseValidator.validate_field_exists(first_comment, "postId")
        ResponseValidator.validate_field_exists(first_comment, "email")
        ResponseValidator.validate_field_exists(first_comment, "body")
        
        # All comments should belong to requested post
        for comment in data:
            assert comment["postId"] == post_id
    
    def test_create_post(self, api_client, created_resources):
        """Test: POST create new post"""
        response = api_client.post(APIEndpoints.POSTS, json=TestData.VALID_POST_CREATE)
        
        ResponseValidator.validate_status_code(response, 201)
        ResponseValidator.validate_response_time(response, TestData.MAX_RESPONSE_TIME_POST)
        
        data = response.json()
        
        ResponseValidator.validate_field_exists(data, "id")
        assert data["title"] == TestData.VALID_POST_CREATE["title"]
        assert data["body"] == TestData.VALID_POST_CREATE["body"]
        assert data["userId"] == TestData.VALID_POST_CREATE["userId"]
        
        created_resources.append(("post", data["id"]))
    
    def test_get_post_not_found(self, api_client):
        """Test: GET post with invalid ID returns 404"""
        invalid_id = TestData.INVALID_POST_ID
        endpoint = APIEndpoints.POST_BY_ID.format(post_id=invalid_id)
        
        response = api_client.get(endpoint)
        
        ResponseValidator.validate_status_code(response, 404)
        