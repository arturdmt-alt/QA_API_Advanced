# Advanced API Testing Framework

[![API Tests](https://github.com/arturdmt-alt/QA_API_Advanced/actions/workflows/tests.yml/badge.svg)](https://github.com/arturdmt-alt/QA_API_Advanced/actions/workflows/tests.yml)

Professional API testing framework using Python, Pytest, and JSONPlaceholder API. Demonstrates advanced testing concepts including layered validation, schema validation, and performance testing.

---

## Technology Stack

* Python 3.11+
* Pytest - Testing framework
* Requests - HTTP client library
* JSONSchema - Schema validation
* Pytest-HTML - Test reporting

---

## Features

* Centralized API client with session management
* Reusable validation utilities
* JSON schema validation
* Response time assertions
* Layered validation approach (status → structure → content)
* Comprehensive test data management
* HTML test reporting
* Clear separation of concerns (utils, tests, data)
* CI/CD pipeline with GitHub Actions

---

## Test Coverage

**Users CRUD Operations:**
* GET all users with pagination validation
* GET single user by ID with schema validation
* POST create new user
* PUT update existing user
* DELETE user
* Negative test: 404 for non-existent user

**Posts Operations:**
* GET all posts
* GET posts filtered by user ID
* GET single post with schema validation
* GET post comments (nested resources)
* POST create new post
* Negative test: 404 for invalid post ID

**Total:** 12 automated tests

---

## Project Structure
```
QA_API_Advanced/
├── data/
│   └── test_data.py           # Test data and JSON schemas
├── reports/
│   └── test_report.html       # Generated HTML test report
├── screenshots/
│   ├── test_report_summary.png
│   └── test_report_details.png
├── tests/
│   ├── test_users_crud.py     # User endpoint tests
│   └── test_posts.py          # Post endpoint tests
├── utils/
│   ├── api_client.py          # HTTP client wrapper
│   ├── api_endpoints.py       # Endpoint configuration
│   └── validators.py          # Response validation utilities
├── conftest.py                # Pytest fixtures
├── requirements.txt           # Python dependencies
└── README.md
```

---

## Setup Instructions

**Prerequisites:**
* Python 3.11 or higher
* pip (Python package manager)
* Git

**Installation:**

1. Clone the repository:
```bash
git clone https://github.com/arturdmt-alt/QA_API_Advanced.git
cd QA_API_Advanced
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run specific test file:
```bash
pytest tests/test_users_crud.py -v
```

Generate HTML report:
```bash
pytest tests/ --html=reports/test_report.html --self-contained-html
```

Run with verbose output:
```bash
pytest tests/ -v -s
```

---

## Test Results

![Test Report Summary](screenshots/test_report_summary.png)

![Test Report Details](screenshots/test_report_details.png)

All tests passing with response times under 3 seconds.

---

## Technical Approach

### Layered Validation Strategy

Tests follow a defensive validation pattern:

1. **Status Code** - Verify HTTP status before processing response
2. **Response Time** - Ensure API meets performance requirements
3. **Content Type** - Validate response format (JSON)
4. **Structure** - Verify expected fields exist
5. **Data Types** - Validate field types (int, str, list)
6. **Content** - Verify actual values

This approach provides clear error messages and catches issues early.

### API Client Pattern

Centralized HTTP client provides:
* Consistent headers across all requests
* Session reuse for performance
* Timeout handling to prevent hanging tests
* Context manager support for proper cleanup

### Schema Validation

JSON Schema validation ensures:
* API contract compliance
* Early detection of breaking changes
* Documentation of expected response structure

---

## Challenges and Solutions

### Challenge 1: Response Time Variability

**Problem:** Initial tests failed due to network latency causing response times to exceed 2000ms limit.

**Solution:** Adjusted timeout threshold to 3000ms for public API testing. In production environment with internal APIs, lower thresholds (500-1000ms) would be more appropriate.

### Challenge 2: Mock API Limitations

**Problem:** JSONPlaceholder is a fake API that doesn't persist data, limiting certain test scenarios.

**Solution:** Documented limitation and focused on testing API contract and response validation rather than data persistence. For real-world projects, would use test database with proper cleanup.

### Challenge 3: Test Data Management

**Problem:** Hardcoded test data scattered across test files made maintenance difficult.

**Solution:** Centralized all test data in `data/test_data.py` including valid data, invalid data, edge cases, and JSON schemas. Single source of truth for test data.

---

## API Used

This project uses **JSONPlaceholder** - a free fake REST API for testing and prototyping.

**Endpoints tested:**
* `/users` - User management
* `/posts` - Blog posts
* `/comments` - Post comments

---

## Author

**Artur Dmytriyev**  
QA Automation Engineer

* GitHub: [github.com/arturdmt-alt](https://github.com/arturdmt-alt)
* LinkedIn: [linkedin.com/in/arturdmytriyev](https://www.linkedin.com/in/arturdmytriyev)
