from django.shortcuts import render, redirect
from . import models


def index(request):
    inde_x = models.Index.objects.all()
    index_image = models.Indeximage.objects.all()
    index_banner = models.Index_Banner.objects.all()
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        models.Message.objects.create(
            name = name,
            email = email,
            message = message
        )
        print(request.POST)

    content = {
        'index_image':index_image,
        'inde_x':inde_x,
        'index_banner':index_banner

    }

    return render(request,'index.html',content)

def index_apps(request):
    return render(request,'index-apps.html')

def index_cons(request):
    return render(request,'index-construction.html')

def index_education(request):
    return render(request,'index-education.html')

def index_medical(request):
    return render(request,'index-medical.html')

def index_realest(request):
    return render(request,'index-realestate.html')

def index_1(request):
    return render(request,'index-01.html')

def index_2(request):
    return render(request,'index-02.html')

def index_3(request):
    return render(request,'index-03.html')

def index_4(request):
    return render(request,'index-04.html')

def index_5(request):
    return render(request,'index-05.html')

def index_6(request):
    return render(request,'index-06.html')

def index_7(request):
    return render(request,'index-07.html')

def about_us(request):
    return render(request,'about-us.html')

def portfolio(request):
    index_image = models.Indeximage.objects.all()

    content ={
        'index_image':index_image
    }

    return render(request,'portfolio.html',content)

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def portfolio_detail(request):
    index_image = models.Indeximage.objects.all()

    content = {
        'index_image': index_image
    }

    return render(request,'portfolio-detail.html',content)

def testimonial(request):
    return render(request,'testimonial.html')

def blog(request):
    return render(request,'blog-listing.html')

def blog_grid(request):
    return render(request,'blog-grid.html')

def blog_listing_left(request):
    return render(request,'blog-listing-left.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        models.Message.objects.create(
            name = name,
            email = email,
            message = message
        )
        print(request.POST)
    return render(request,'contact-us.html')

def blog_detail(request):
    return render(request,'blog-details.html')



