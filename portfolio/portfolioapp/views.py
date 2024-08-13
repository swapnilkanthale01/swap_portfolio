from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import enquiry

# Create your views here.
def portfolio(request):
    if request.method=='POST':
        name=request.POST.get('cname')
        email=request.POST.get('cemail')
        mobile=request.POST.get('cno')
        message=request.POST.get('cmsg')
        
        client= enquiry(name=name,email=email,mobile_number=mobile,message=message)
        client.save()
        return redirect('submit')
        print(name,email,mobile,message)
    else:
        return render(request,'portfolio.html',{'error':'all feilds are compulsary.'})



    return render(request,'portfolio.html')
def submit_view(request):
    return render(request,'submit.html')