from email.mime import image
from turtle import title
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.db import models
from user.models import CustomUser
from ckeditor.fields import RichTextField



class Events(models.Model):
    image = models.ImageField(upload_to='events')
    date = models.DateField()
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    ticket_price = models.TextField()
    content = RichTextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.SmallIntegerField(default=0)
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250) 

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Blogs(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    content = RichTextField()
    sub_title = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tags)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def comments(self):
        return BlogComments.objects.filter(blog__title=self.title).all()

    def __str__(self) -> str:
        return self.title


class BlogComments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class Course_Outline(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=250)
    def __str__(self):
        return self.text


class Trainer(models.Model):
    image = models.ImageField()
    full_name = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name



class Course(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    course_fee = models.CharField(max_length=250, null=True)
    sub_title = models.CharField(max_length=250)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    objective = RichTextField()
    courseoutline = models.ManyToManyField(Course_Outline)
    order = models.SmallIntegerField(default=0)
    def comments(self):
        return CourseComments.objects.filter(course__title=self.title)
    def __str__(self):
        return self.title



class CourseComments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = RichTextField()
    def __str__(self):
        return self.content
    





