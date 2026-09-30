from django.shortcuts import render
from django.http import JsonResponse

def employeeView(request):
    emp={
        'id':29,
        'name':'archesh',
        'age':21
    }
    return JsonResponse(emp)

