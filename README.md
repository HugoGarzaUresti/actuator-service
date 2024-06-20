# Actuator Service

This guide demonstrates how to add operational endpoints to a Flask application similar to Spring Boot Actuator using `pyctuator`. It includes endpoints for health checks, application info, and metrics.

## Requirements

- Python 3.x
- `Flask` library (version 2.0.3)
- `pyctuator` library (version 0.15.0)
- `psutil` library

## Setup

1. Install dependencies:
    ```sh
    pip uninstall Flask pyctuator
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

3. Access the Actuator Endpoints:
    - Health: `http://127.0.0.1:5000/actuator/health`
    - Info: `http://127.0.0.1:5000/actuator/info`
    - Metrics: `http://127.0.0.1:5000/actuator/metrics`

## Code Explanation

### `views.py`

This module contains a simple API endpoint.

- **`/api`**: Returns a JSON message.

### `__init__.py`

This module initializes the Flask application and sets up pyctuator.

- Registers a simple health check for disk space usage.
- Collects custom CPU usage metrics every 10 seconds.

### `run.py`

This script serves as the entry point for the application.

## Additional Information

- You can customize the health checks and metrics as needed.
- This setup provides a basic starting point for adding operational endpoints to your Flask application using pyctuator.
