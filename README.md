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
- [License](#-license)
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
   git clone https://github.com/your-username/number-api.git
   cd number-api

<p align="center"> Made with ❤️ by <strong>Victor Oduor(OVI)</strong> </p> 