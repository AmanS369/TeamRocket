from django.http import HttpResponse
from django.shortcuts import render, redirect
from track.models import Ngodetails
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout
def home(request):
   return render(request,"home.html")



# def ngo_form(request):

#     if request.method == 'POST':
#         name = request.POST['name']
#         location = request.POST['location']
#         description = request.POST['description']
#         vision = request.POST['vision']
#         year = request.POST['year']
#         email = request.POST['email']
#         image = request.FILES.get('image')
#         phone=request.POST.get('phone')
        
#         submission = Ngodetails(manage=request.user ,name=name, state=location, description=description, vision=vision, founding_year=year, emailid=email, logo=image,phone=phone)
#         submission.save()
#         return redirect(home)
#     else:
#         # Render the form if it's a GET request
#         return render(request, 'ngo_form.html')

   
def register_user(request):
    if request.method == 'POST':
        First_Name=request.POST['first_name']
        Last_Name=request.POST['last_name']
        username=request.POST['username']
        Email=request.POST['email']
        Password=request.POST['password']
        Cpassword=request.POST['Cpassword']
        name = request.POST['name']
        location = request.POST['location']
        description = request.POST['description']
        vision = request.POST['vision']
        year = request.POST['year']
        email = request.POST['email']
        image = request.FILES.get('image')
        phone=request.POST.get('phone')
        
        if Password==Cpassword:
         if User.objects.filter(username=username).exists():
            error_message="Username already taken"
            return render(request, 'register.html',{'error':error_message})
         elif User.objects.filter(email=Email).exists():
              error_message="Email already taken"
              return render(request, 'register.html',{'error':error_message})
         else:
            user=User.objects.create_user(username=username,password=Cpassword,email=Email,first_name=First_Name,last_name=Last_Name)
            user.save();

            submission = Ngodetails(manage=request.user ,name=name, state=location, description=description, vision=vision, founding_year=year, emailid=email, logo=image,phone=phone)
            submission.save()
            return redirect(home)
           
        else:
         error_message = "PASSWORD DO NOT MATCH"
         return render(request, 'Sing.html')
        
        

    else:  
     return render(request, 'Sing.html')





def Login(request):
   if request.method == 'POST':
       Email=request.POST['email']
       Password=request.POST['password']
       
       user = auth.authenticate(username=Email, password=Password)
       print(Email)
       print(Password)
       if user is not None:
         auth.login(request,user)
         return redirect(home)
       else:
         error="Invalid Creditanidals"
         return render(request, 'login.html', {'error': error})
   else:
      return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect(home)


   