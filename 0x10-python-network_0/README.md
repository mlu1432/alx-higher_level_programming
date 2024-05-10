# 0x10 Python Network 0

This repository contains practical scripts that demonstrate how to interact with a web server using the `curl` command in Bash. Each script is tailored to handle different HTTP methods and responses.

## Scripts

### 0. cURL Body Size

**Filename**: `0-body_size.sh`

- **Description**: This script takes a URL as input, sends a request to that URL, and displays the size of the body of the response in bytes.
- **Usage**: `./0-body_size.sh 0.0.0.0:5000`
- **Example Output**: `10`

### 1. cURL to the End

**Filename**: `1-body.sh`

- **Description**: Sends a GET request to a URL and displays the body of a 200 status code response.
- **Usage**: `./1-body.sh 0.0.0.0:5000/route_1`
- **Example Output**: `Route 2`

### 2. cURL Method

**Filename**: `2-delete.sh`

- **Description**: Sends a DELETE request to the URL passed as the first argument and displays the body of the response.
- **Usage**: `./2-delete.sh 0.0.0.0:5000/route_3`
- **Example Output**: `I'm a DELETE request`

### 3. cURL Only Methods

**Filename**: `3-methods.sh`

- **Description**: Takes in a URL and displays all HTTP methods the server will accept.
- **Usage**: `./3-methods.sh 0.0.0.0:5000/route_4`
- **Example Output**: `OPTIONS, HEAD, PUT`

### 4. cURL Headers

**Filename**: `4-header.sh`

- **Description**: Sends a GET request to the URL and displays the body of the response, including a custom header.
- **Usage**: `./4-header.sh 0.0.0.0:5000/route_5`
- **Example Output**: `Hello School!`

### 5. cURL POST Parameters

**Filename**: `5-post_params.sh`

- **Description**: Sends a POST request with email and subject parameters and displays the body of the response.
- **Usage**: `./5-post_params.sh 0.0.0.0:5000/route_6`
- **Example Output**: `POST params: email: test@gmail.com subject: I will always be here for PLD`

### 6. Find a Peak

**Filename**: `6-peak.py`, `6-peak.txt`

- **Description**: Python function to find a peak in a list of unsorted integers.
- **Complexity**: The complexity of the algorithm is O(log(n)).
- **Usage**: Run `./6-main.py` to execute the tests.

### 7. Only Status Code

**Filename**: `100-status_code.sh`

- **Description**: Sends a request to a URL and displays only the status code of the response.
- **Usage**: `./100-status_code.sh 0.0.0.0:5000`
- **Example Output**: `200` or `404` for not found routes.

### 8. cURL a JSON File

**Filename**: `101-post_json.sh`

- **Description**: Sends a JSON POST request to a URL using the contents of a file.
- **Usage**: `./101-post_json.sh 0.0.0.0:5000/route_json my_json_0`
- **Example Output**: `Valid JSON`

### 9. Catch Me If You Can!

**Filename**: `102-catch_me.sh`

- **Description**: Makes a request to catch a specific server response.
- **Usage**: `./102-catch_me.sh`
- **Example Output**: `You got me!`

## Testing

All scripts should be tested in the provided sandbox environment, running on port 5000, to ensure correct functionality.
