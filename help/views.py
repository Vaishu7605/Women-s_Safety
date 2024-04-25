from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import clients
from .form import helpform
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import auth
from django.core.mail import send_mail,EmailMultiAlternatives
from .models import Feedback

# #email
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes
# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# from django.contrib.auth import get_user_model
# from django.http import HttpResponse


def main(request):
    current_user = request.user
    user_id = current_user.id
    print(user_id)
    context = {'user_id': user_id}
    return render(request,'womensafety.html')


  
def harrasment(request):
    return render(request, "harrasment.html")
  
def helpdesk (request):
    return render(request, "helpdesk.html")

def helpline(request):
    return render(request, "helpline.html")
  
def legally(request):
    return render(request, "legally.html")
  
def login(request):
    return render(request, "login.html")

def schemes(request):
    return render(request,"schemes.html")
  
def signup(request):
    return render(request, "signup.html")
  
def contact(request):
    return render(request, "contact.html")

def cybercrime(request):
    return render(request, "cybercrime.html")
  
def domestic(request):
    return render(request, "domestic.html")
  
def eveteasing(request):
    return render(request, "eveteasing.html")

def home(request):
    return render(request,"womensafety.html")

def logout(request):
    auth.logout(request)
    return redirect('/')






def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

         # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different username.")
        
        if pass1 != pass2:
            return HttpResponse("Passwords do not match. Please enter matching passwords.")
        
        # Create a new user
        user = User.objects.create_user(username, email, pass1)
        user.save()
        # You can also set additional fields like first_name, last_name, etc., if needed.

        # Redirect to the login page or any other desired page after successful signup
        return redirect('login')
    
    return render(request, 'signup.html')
   

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']
        user = authenticate(request, username=username, email=email, password=pass1)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('womensafety')
        else:
            return HttpResponse("Username or Password is incorrect !!! ")

    return render(request, 'login.html')
    


# def sendme(request):
#     subject = "Django Mail"
#     body = "<h1 class=text-center style='color:blue'> Welcome to our website</h1>"
#     sender="safetywomen75@gmail.com"
#     recepient =["{{ user.email }}"]

#     mail = EmailMultiAlternatives(subject,body, sender, recepient)

#     mail.content_subtype ='html'
#     mail.send()
#     return render(request,'womensafety')

def Feedback(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        mail=request.POST["mail"]
        query=request.POST["query"]
        hello=Feedback(uname=uname, email=mail, query=query)
        hello.save()
        return HttpResponse("<h1> Feedback has been submitted </h1>")
        # print(name,email,feedback)
    return render(request,'feedback.html')