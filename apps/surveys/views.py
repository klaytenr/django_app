from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    response = "Placeholder to display all the surveys created"
    return HttpResponse(response)

def new(request):
    response = "Placeholder for users to add a new survey"
    return HttpResponse(response)