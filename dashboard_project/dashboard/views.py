from django.shortcuts import render
import requests
import json

def landing_page(request):
    return render(request, 'dashboard/landing_page.html')

def select_country(request):
    countries = [
        {'code': 'USA', 'name': 'United States'},
        {'code': 'IND', 'name': 'India'}
    ]
    return render(request, 'dashboard/select_country.html', {'countries': countries})

def dashboard(request):
    country = request.GET.get('country')
    response = requests.get(f'https://us-central1-projectexperiment-420611.cloudfunctions.net/assignApi?countryName={country}')
    data = response.json()
    
    # Prepare the data for charts and details display
    car_types = set(driver['car_type'] for driver in data)
    pie_labels = list(car_types)
    pie_values = [sum(driver['average_earnings_per_month'] for driver in data if driver['car_type'] == car_type) for car_type in car_types]
    line_labels = [driver['name'] for driver in data]
    line_values = [driver['age'] for driver in data]

    context = {
        'country': country,
        'data': json.dumps({
            'country': country,
            'drivers': data,
            'pie_labels': pie_labels,
            'pie_values': pie_values,
            'line_labels': line_labels,
            'line_values': line_values,
        })
    }
    return render(request, 'dashboard/dashboard.html', context)
