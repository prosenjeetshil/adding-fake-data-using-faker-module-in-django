from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from faker import Faker

# Create your views here.

def add_fake_data(request):
    fake = Faker()
    for _ in range(10):  # Generating 10 fake students
        Student.objects.create(
            name=fake.name(),
            roll_number=fake.random_int(min=1000, max=9999),
            age=fake.random_int(min=15, max=18),
            grade=fake.random_element(elements=('A', 'B', 'C', 'D'))            
            )
    return HttpResponse("Fake Data Added!")

def show_fake_data(request):
    students = Student.objects.all()
    template_name = "fake_data.html"
    context = {"students": students}
    return render(request, template_name, context)