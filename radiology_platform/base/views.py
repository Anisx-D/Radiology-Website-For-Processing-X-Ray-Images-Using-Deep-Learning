from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')
def requestappointment(request):
    return render(request, 'base/requestappointment.html')
def patientcare(request):
    return render(request, 'base/patientcare.html')
def blog(request):
    return render(request, 'base/blog.html')
def aboutus(request):
    return render(request, 'base/aboutus.html')

