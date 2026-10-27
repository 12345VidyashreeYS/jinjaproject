from django.shortcuts import render

# Create your views here.
def view1(request):
    name="Rama"
    age=22
    place="Banglore"
    ctx={'NAME':name,
         'AGE':age,
         'PLACE':place}
    return render(request, 'myapp/jinja.html', ctx)

def view2(request):
    name=input("Enter your Name: ")
    age=int(input("Enter your Age: "))
    place=input("Enter the Place: ")
    ctx={'NAME':name,
         'AGE':age,
         'PLACE':place}
    return render(request, 'myapp/jinja.html', ctx)
