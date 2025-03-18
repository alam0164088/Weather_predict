from django.shortcuts import render
import requests

def weather_view(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        location = request.POST.get('city')  # Make sure to use the correct input name from the form
        api_key = '97148b51b52d8e4d9bb5b238e330a429'  # Replace with your OpenWeather API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = "City not found or error in the request."

    # Handle rendering the data
    if weather_data:
        context = {
            'city': location,
            'temperature': weather_data['main']['temp'],
            'condition': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'error_message': error_message
        }
    else:
        context = {
            'error_message': error_message
        }

    return render(request, 'weather.html', context)
