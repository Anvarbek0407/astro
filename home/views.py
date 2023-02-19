from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from home.models import *
# Create your views here.
def about(request):
    return render(request, 'about.html')
def course_details(request, id):
    context = {}
    course = Course.objects.filter(id=id).first()
    courses = Course.objects.exclude(id=id).all()
    context['comments'] = CourseComments.objects.all()
    context['courses'] = courses
    context['course'] = course
    if request.method == "POST":
       if request.user.is_authenticated:
        content = request.POST.get("content",False) 
        if content:
            cm = CourseComments.objects.create(user=request.user,course=course,content=content)
            cm.save()
    return render(request, 'course-details.html',context)



def event_details(request, id):
    context = {}
    event = Events.objects.filter(id=id).first()
    #events = Events.objects.exclude(id=id).all()
    context['tags'] = Tags.objects.all()
    context['blogs'] = Blogs.objects.all() 
    context['categorys'] = Category.objects.all()
    context['blogcomments'] = BlogComments.objects.all()
    context['event'] = event
    return render(request, 'event-details.html', context)
    

def events(request):
    context = {}
    context['events1'] =Events.objects.all().order_by('order')[:4]
    context['events2'] =Events.objects.all().order_by('order')[4:8]
    
    return render(request, 'events.html', context)
    
def gallery(request):
    return render(request, 'gallery.html')
def index(request):
    return render(request, 'index.html')

def courses(request, ):
    context = {}
    context['courses1'] =Course.objects.all().order_by('order')[:4]
    context['courses2'] =Course.objects.all().order_by('order')[4:8]
    
    return render(request, 'courses.html', context) 

def blog_home(request):
    return render(request, 'blog-home.html')
def blog_single(request):
    return render(request, 'blog-single.html')
def contact(request):
    return render(request, 'contact.html')
def elements(request):
    return render(request, 'elements.html')
def contact(request):
    return render(request, 'contact.html')

