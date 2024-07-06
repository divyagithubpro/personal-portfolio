from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact.objects.create(name=name,email=email,subject=subject,message=message)
        return redirect('/')
    return render(request,"index.html")


def portfolio(request):
    return render(request,"portfolio-details.html")



def pro1(request):
    return render(request,"pro1.html")


def pro2(request):
    return render(request,"pro2.html")


def pro3(request):
    return render(request,"pro3.html")


def pro4(request):
    return render(request,"pro4.html")
