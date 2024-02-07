from django.shortcuts import render
from django.http import HttpResponse
import requests

# def read_view(request):
#     # Make a request to the producer microservice to get the message
#     producer_url = 'http://127.0.0.1:8000/'  # Replace with the actual URL of your producer microservice
#     response = requests.get(producer_url)

#     if response.status_code == 200:
#         message = response.text
#         return HttpResponse(f"Received message: {message}")
#     else:
#         return HttpResponse("Failed to retrieve the message from the producer microservice.")



def read_view(request, object_id):
    producer_url = f'http://127.0.0.1:8000/hello/{object_id}/'
    
    try:
        response = requests.get(producer_url)

        if response.status_code == 200:
            message = response.text
            return HttpResponse(f"Received message: {message}")
        else:
            return HttpResponse(f"Failed to retrieve the message. Status code: {response.status_code}")

    except requests.RequestException as e:
        return HttpResponse(f"Error while making request to hello microservice: {str(e)}")