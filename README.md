# Number Classification API

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/REST_API-FF6F61?style=for-the-badge&logo=rest&logoColor=white" alt="REST API">
</p>

<p align="center">
  <strong>A Django-based API to classify numbers and retrieve their mathematical properties along with fun facts.</strong>
</p>

---

## 📖 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Documentation](#-api-documentation)
  - [Endpoint](#endpoint)
  - [Example Request](#example-request)
  - [Example Response](#example-response)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Features
- **Number Classification**: Checks if a number is prime, perfect, or an Armstrong number.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches a math-related fun fact about the number from the [Numbers API](http://numbersapi.com).
- **Error Handling**: Gracefully handles invalid inputs and returns appropriate error messages.
- **CORS Support**: Allows cross-origin requests for seamless integration with frontend applications.

---

## 🛠 Technologies Used
- **Backend**: Django, Django REST Framework
- **External API**: [Numbers API](http://numbersapi.com)
- **Dependencies**:
  - `requests`: For making HTTP requests to the Numbers API.
  - `django-cors-headers`: For handling Cross-Origin Resource Sharing (CORS).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/OviLab-sys/hng-stage1
   cd number-api
2. install the required dependencies:
   pip install -r requirements.txt

3. Access the API locally at:
   http://127.0.0.1:8000/api/number_classifier/?number=<your-number>

### 📚 API Documentation
1. Endpoint:
    GET /api/number_classifier/?number=<number>

2. Parameters:
    number (required): The number to classify. Must be a valid integer.

3. Example Request:
    GET /api/number_classifier/?number=371

4. Example Response:
    {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is the sum of the cubes of its digits.
    }

5. Example Response (400 Bad Request):
    {
    "number": "abc",
    "error": true
    }


### 🌐 Deployment
To deploy this project, follow the instructions for your preferred hosting platforme.g., Render

1. Steps for Deployment:
    -Create a requirements.txt file 
    -Ensure all dependencies are listed in the requirements.txt file, as in below.
        Django==4.2
        djangorestframework==3.14.0
        requests==2.31.0
        django-cors-headers==4.3.1

### 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/YourFeatureName).

3. Commit your changes (git commit -m 'Add some feature').

4. Push to the branch (git push origin feature/YourFeatureName).

5. Open a pull request.

### 🙏 Acknowledgments

Numbers API for providing fun facts about numbers.

Django and Django REST Framework for making API development easy.

Shields.io for the awesome badges.

<p align="center"> Made with ❤️ by <strong>Victor Oduor(OVI)</strong> </p> 