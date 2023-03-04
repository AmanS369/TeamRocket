from django.http import HttpResponse
from django.shortcuts import render, redirect
from track.models import Ngodetails,desc_model,achievement_model
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout

def home(request):
   
   return render(request,"home.html")


def event_dashboard(request):
 if request.method == 'GET':
   data={}
   user=request.user
   print(user)
   
   if user.is_authenticated:
      prod = Ngodetails.objects.filter(manage=user)
      data['prod']=prod
   return render(request,'event.html',data)
 

def achievment(request):
  if request.method == 'GET':
     return redirect(dashboard)
  else:
        desc = request.POST['desc2']
        t1 = request.POST['t1']
        
        img1 = request.FILES.get('img_1')
       
        user=request.user
        ngo=Ngodetails.objects.get(manage=user)
        achieve=achievement_model(ngo=ngo,manage=user,img1=img1,t1=t1,desc2=desc)
        achieve.save()
        return redirect(dashboard)
     

      

def dashboard(request):
 if request.method == 'GET':
   data={}
   user=request.user
   print(user)
   
   if user.is_authenticated:
      prod = Ngodetails.objects.filter(manage=user)
      data['prod']=prod
   return render(request,'index.html',data)
 
 
 else:
        desc = request.POST['description']
        t1 = request.POST['title_1']
        t2 = request.POST['title_2']
        im1 = request.FILES.get('image_1')
        img2 = request.FILES.get('image_2')
        user=request.user
        print(user)
        ngo=Ngodetails.objects.get(manage=user)
        blog=desc_model(ngo=ngo,manage=user,im1=im1,img2=img2,title1=t1,title2=t2,desc=desc)
        blog.save()
        return redirect(dashboard)




   
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
        phone=request.POST.get('ngo_phone')
        
        if Password==Cpassword:
         if User.objects.filter(username=username).exists():
            error_message="Username already taken"
            return render(request, 'Sing.html',{'error':error_message})
         elif User.objects.filter(email=Email).exists():
              error_message="Email already taken"
              return render(request, 'Sing.html',{'error':error_message})
         else:
            user=User.objects.create_user(username=username,password=Cpassword,email=Email,first_name=First_Name,last_name=Last_Name)
            user.save();

            user = auth.authenticate(username=username, password=Password)
            auth.login(request,user)

            submission = Ngodetails(manage=request.user ,name=name, state=location, description=description, vision=vision, founding_year=year, emailid=email, logo=image,phone=phone)
            submission.save()
            return redirect(dashboard)
           
        else:
         error_message = "PASSWORD DO NOT MATCH"
         return render(request, 'Sing(1).html')
        
        

    else:  
     return render(request,'Sing(1).html')





def Login(request):
   if request.method == 'POST':
       Email=request.POST['email']
       Password=request.POST['password']
       
       user = auth.authenticate(username=Email, password=Password)
       print(Email)
       print(Password)
       if user is not None:
         auth.login(request,user)
         return redirect(dashboard)
       else:
         error="Invalid Creditanidals"
         return render(request, 'login.html', {'error': error})
   else:
      return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect(home)



def landing_page(request,input):
    x=int(input)
    print("--------")
    print(x)
    ngo=Ngodetails.objects.get(id=x)
    ngo_data=Ngodetails.objects.filter(id=x)
    ans = desc_model.objects.filter(ngo=ngo).last()
    ach=achievement_model.objects.filter(ngo=ngo)
    print(ans.title1)
    data={}
    data['ngo_data']=ngo_data
    data['ans']=ans
    data['ach']=ach
    return render(request,"landing.html",data)