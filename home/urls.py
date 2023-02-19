
from argparse import RawTextHelpFormatter
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('blog-home', blog_home, name='blog-home'),
    path('blog-single', blog_single, name='blog-single'),
    path('contact', contact, name='contact'),
    path('<int:id>/course-details', course_details, name='course-details'),
   #path('<int:id>/comment', comment,name='comment')
    path('courses', courses, name='courses'),
    path('elements', elements, name='elements'),
    path('<int:id>/event-details', event_details, name='event-details'),
    path('events', events, name='events'),
    path('gallery', gallery, name='gallery'),
    path('', index, name='home'),

]
