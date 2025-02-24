# Postcode Verification and Formatting

This project provides functionality to format and verify UK postcodes. It includes a Flask API for interacting with the postcode functions and a command-line interface (CLI) for direct usage.

**Only validates postcode formats. Does not ensure that a postcode legitimately exists.**

## Prerequisites

- Python 3.11 or higher
- `pip` (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/m-krasikov/scurri_coding_test.git
    cd scurri_coding_test
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    ```sh
    source venv/bin/activate
    ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Flask API

1. Set the `FLASK_APP` environment variable:
    ```sh
    export FLASK_APP=api.py
    ```

2. Run the Flask development server:
    ```sh
    flask run
    ```

3. The API will be available at `http://127.0.0.1:5100`.

## Using the CLI

1. To format a postcode:
    ```sh
    python main.py -p "EC1A-1BB" -f
    ```

2. To verify a postcode:
    ```sh
    python main.py -p "EC1A 1BB"
    ```
3. To print the sequence:
    ```sh
    python main.py -s
    ```
    **Print the numbers from 1 to 100 with Three instead of multiples of 3, Five instead of multiples of 5, and ThreeFive instead of multiples of both**

    

## Running Tests

1. Ensure the virtual environment is activated.

2. Run the tests using `unittest`:
    ```sh
    python -m unittest discover
    ```
## Docker Compose

### Prerequisites

- Docker
- Docker Compose

### Building and Running the Application

1. Build the Docker images:
    ```sh
    docker compose build
    ```

2. Run the application:
    ```sh
    docker compose up -d
    ```

3. The API will be available at `http://127.0.0.1:5100`.

### Running Tests

1. Run the tests using Docker Compose:
    ```sh
    docker compose run web python -m unittest discover
    ```

## API Endpoints

### Format Postcode

- **URL:** `/format/<postcode>`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "status": "success",
        "formatted_postcode": "EC1A 1BB"
    }
    ```

### Verify Postcode

- **URL:** `/verify/<postcode>`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "status": "success",
        "message": "Postcode is valid"
    }
    ```
- **Error Response:**
    ```json
    {
        "status": "error",
        "message": "Error message"
    }
    ```