from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from FoodApp.modules.PhoneAuthentication import checkVerificationCode, sendVerificationCode


def index(request):
    return render(request , 'index.html')

def phoneAuthentication(request):
    phone_number = request.POST['phone_number']
    phone_number = '+91' + phone_number
    print(phone_number)
    response = sendVerificationCode(phone_number)
    return JsonResponse(response)

def codeVerification(request):
    phone_number = request.POST['phone_number']
    phone_number = '+91' + phone_number
    verification_code = request.POST['verification_code']
    response = checkVerificationCode(verification_code , phone_number)
    return response

