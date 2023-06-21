# Django API Measurement

This Django project provides a simple API endpoint to measure the response time and status code of a specified domain or IP.

## Setup

1. Clone the repository:

   ```shell
    git clone <repository_url>
   ```

2. Install the required dependencies:

```shell
    pip install -r requirements.txt
```
3. Start the Django development server:

```shell
    python manage.py runserver
```
4. The server will start running at http://localhost:8000/.

## API Endpoint
    Measure Response
    This endpoint measures the response time and status code of a specified domain or IP.

    URL: api/measure/measure_response/
    Method: GET
### Parameters
    dominio (string): The domain to measure the response time for.
    ip (string, optional): The IP address to make the request to instead of resolving the domain.
    
### Example
    To measure the response time for a domain, make a GET request to the following URL:

    http://localhost:8000/measure/measure_response/?dominio=www.example.com
    To measure the response time for an IP address, include the ip parameter:

    http://localhost:8000/measure/measure_response/?dominio=www.example.com&ip=203.0.113.0
    The response will be a JSON object containing the measured response time (in milliseconds) and the status code:

    {
        "status": 301,
        "time": "150ms"
    }
