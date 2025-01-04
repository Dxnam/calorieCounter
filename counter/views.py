from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':
        # Retrieve the 'query' parameter from the POST data
        query = request.POST.get('query', '')  # Use .get() to avoid KeyError if 'query' is missing
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        
        try:
            # Make a GET request to the API
            api_request = requests.get(api_url + query, headers={'X-Api-Key': 'MWNNmW+CxTiKuq/yrh877A==KUZOmpUeAh7ruOGA'})
            api = api_request.json().get('items', [])  # Convert the response to JSON
            print(api_request.content)
        except Exception as e:
            api = "Oops! There was an error"
            print(e)
        
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
