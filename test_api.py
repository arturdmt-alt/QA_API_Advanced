import requests

# Test 1: Get all users
response = requests.get("https://jsonplaceholder.typicode.com/users")
print("=== TEST 1: Get All Users ===")
print(f"Status: {response.status_code}")
print(f"Total users: {len(response.json())}")
print(f"First user: {response.json()[0]}")
print()

# Test 2: Get single user
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print("=== TEST 2: Get Single User ===")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
print()

# Test 3: Get posts
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
print("=== TEST 3: Get User Posts ===")
print(f"Status: {response.status_code}")
print(f"Total posts: {len(response.json())}")
print()

# Test 4: Create post
new_post = {
    "title": "Test Post",
    "body": "This is a test",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print("=== TEST 4: Create Post ===")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
