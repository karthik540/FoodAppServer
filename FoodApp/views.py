from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'index.html')

def phoneAuthentication(request):
    phone_number = request.POST['phone_number']
    phone_number = '+91' + phone_number
    print(phone_number)
    response = sendVerificationCode(phone_number)
    return JsonResponse(response)

def checkVerificationCode(request):
    phone_number = request.POST['phone_number']
    phone_number = '+91' + phone_number
    verification_code = request.POST['verification_code']
    response = checkVerificationCode(verification_code , phone_number)
    return response