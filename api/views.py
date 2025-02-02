from django.http import JsonResponse
from rest_framework.decorators import api_view
from math import sqrt
import requests

def is_prime(n):
    """checks if number is prime."""
    if n < 2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """checks if number is perfect."""
    if n < 2:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0) 

def is_armstrong(n):
    """checks if number is armstrong."""
    digits = [int(i) for i in str(abs(n))]
    power = len(digits)
    return abs(n) == sum(i ** power for i in digits)

def get_fun_fact(n):
    """get fun fact about the number."""
    try:
        response = requests.get(f'http://numbersapi.com/{n}')
        if response.status_code == 200:
            return response.text.strip()
    except requests.RequestException:
        pass
    return "No fun fact available"

@api_view(['GET'])
def number_classifier(request):
    """API endpoint to classify a number and return it's properties."""
    number = request.GET.get('number')

    if not number or not number.lstrip('-').isdigit():
        return JsonResponse({"number":number, "error": True}, status=400)
    
    number = int(number)
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.append("armstrong")

    response_data = {
        "number":number,
        "is_prime":is_prime(number),
        "is_perfect":is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(i) for i in str(abs(number))),
        "fun_fact":get_fun_fact(number)
    }

    return JsonResponse(response_data)