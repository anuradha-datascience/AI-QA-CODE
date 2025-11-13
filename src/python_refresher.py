#Python Basics for QA Context
#Variables & Data Types 

# Used to store test data, API responses, config paths.

test_name = "Login API"
status_code = 200
is_passed = True
response_time = 0.45

# Lists and Dictionaries

#Commonly used for datasets, configurations, and JSON structures.

test_cases = ["login", "logout", "create_user"]
api_response = {"status": "success", "code": 200, "message": "OK"}

print(test_cases[0])
print(api_response["status"])


# Use cases:

# Managing multiple test inputs

# Storing JSON API responses

# Validating structured data

#Loops

# Execute multiple API calls, verify test cases, or read CSV data.

for case in test_cases:
    print(f"Running test: {case}")


# Example in QA:

api_endpoints = ["/login", "/logout", "/users"]
for endpoint in api_endpoints:
    print(f"Testing {endpoint}")

#Functions

# Encapsulate reusable test logic.

def check_status(response_code):
    if response_code == 200:
        return "PASS"
    else:
        return "FAIL"

print(check_status(200))

# Exception Handling

# Essential for API and data tests where requests may fail.

import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("API call failed:", e)

#Working with JSON

# Used in API responses and test data files.

import json

# Convert dict to JSON
data = {"test": "Login", "result": "Pass"}
json_str = json.dumps(data)

# Parse JSON string
parsed = json.loads(json_str)
print(parsed["test"])

#File Handling

#Reading test data or writing logs.

with open("data/sample.txt", "w") as file:
    file.write("Test log created successfully.")

with open("data/sample.txt", "r") as file:
    print(file.read())

#Logging (Light Intro before Pytest)

# Used for debugging automation.

import logging
logging.basicConfig(filename="reports/logs/demo.log", level=logging.INFO)
logging.info("Test started")
logging.warning("API response delayed")
logging.error("Assertion failed")

# 4️⃣ Mini QA Exercises
# Exercise	Description	Expected Output
# 1	Write a function to compare two response codes	PASS/FAIL message
# 2	Read a CSV of test cases and print all failed ones	CSV parsing
# 3	Fetch a fake API and print titles of posts	Successful GET request
# 4	Log start and end time of each test	Timestamps in logs
# 5	Handle an invalid API call gracefully	Exception message logged