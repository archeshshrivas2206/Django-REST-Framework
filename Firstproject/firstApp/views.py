from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

def employeeView(request):
    emp={
        'id':29,
        'name':'archesh',
        'age':21
    }

    data = Employee.objects.all() # this is a query set and we cant respond with a queryset 

    response= {'employee':list(data.values('name','salary'))} 

    return JsonResponse(response)

