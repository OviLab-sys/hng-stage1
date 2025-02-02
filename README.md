# Number Classification API

This is a Django-based API that classifies a given number and returns its mathematical properties along with a fun fact.

## Features
- Checks if a number is prime, perfect, or an Armstrong number.
- Calculates the sum of the digits of the number.
- Fetches a fun fact about the number from an external API.
- Handles invalid inputs gracefully.
- Supports CORS for cross-origin requests.

## Endpoint
- **GET** `/api/classify-number/?number=<number>`

## Example Request
```bash
GET /api/classify-number/?number=371

EXAMPLE RESPONCE 

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

DEPLOYMENT

The API is deployed at: <your-deployed-url>

Technologies Used
Django

Django REST Framework

Requests (for external API calls)

Django CORS Headers