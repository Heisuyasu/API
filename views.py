from django.shortcuts import render
import requests
from django.http import JsonResponse


def home(request):
    return render(request, 'display.html')

def fetch_quotes(request):
    num = request.GET.get('num')
    try:
        if not num or not num.isdigit():
            response = requests.get('https://stoic-quotes.com/api/quote')
        else:
            response = requests.get(f'https://stoic-quotes.com/api/quotes?=num=2{num}')
        response.raise_for_status()
        quotes = response.json()
        return JsonResponse({'quotes': quotes})
    except requests.RequestException:
        return JsonResponse({'error': 'Unable to retrieve quotes at the moment. Please try again later.'}, status=500)


