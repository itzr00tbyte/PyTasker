from django.shortcuts import render
from forex_python.converter import CurrencyRates

# Create your views here.

def home(request):
    return render(request,'index.html',)

import asyncio
from django.shortcuts import render
from forex_python.converter import CurrencyRates

async def perform_conversion(from_currency, to_currency, amount):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return result

async def currency(request):
    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = float(request.POST.get('amount'))
        
        result = await perform_conversion(from_currency, to_currency, amount)

        context = {
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount,
            'result': result
        }
        return render(request, 'CurrencyConerter.html', context)

    return render(request, 'CurrencyConerter.html')
