from django.shortcuts import render

# Create your views here.
# producer/hello_service/views.py
from django.http import JsonResponse

# def hello_view(request):
#     message = "Hello from Microservice 1! I m so happy"
#     data = {'message': message}
#     return JsonResponse(data)


from .models import MyModel

def home(request):
    return render(request,'userid.html')

def hello_view(request, object_id):
    obj = MyModel.objects.get(pk=object_id)
    data = {'name': obj.name, 'description': obj.description}
    return JsonResponse(data)
