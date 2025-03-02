from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from .forms import HelloForm 
from .forms import marksheet
from .forms import signupform
import math
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from .middlewares import auth, gest
from django.core.signing import TimestampSigner ,BadSignature,SignatureExpired
from .utils import validate_token,genrate_token
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

def home(request):
    # data={
    #     'title': 'Home Page',
    #     'alt':'sorry for this inconvenience',
    #     'courses': ['Python','Django','Flask'],
    #     'year': 2022,
    #     'author': 'John Doe',
    #     'details':[
    #      {'name': 'rohan','phone':123556789},
    #      {'name': 'ramesh','phone':987654321},
    #      {'name': 'rahul','phone':123456789}  , 
    #     ],
    # }
    # return render(request, 'parctice5_2.html',data)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
@auth
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         # Process form data here (e.g., send email or save to database)
#         print(f"Message received from {name} ({email}): {message}")
#     return render(request, 'contact.html')

def aboutus(request):
    return HttpResponse("<b>Hello, world. You're at the about page.</b>")

def detail(request,courseid):
    return HttpResponse(courseid)

def services(request):
    return render(request, 'service.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # Process form data here (e.g., authenticate user)
#         if username == 'admin' and password == 'password':
#             return HttpResponse("Login successful")
#         else:
#             return HttpResponse("Invalid credentials")
#     return render(request, 'login.html')

# def login(request):
#     var="o/p_will_come"
#     fn=HelloForm()
#     data={'form': fn}
#     if request.method == "POST":
#         # username = request.GET['username']
#         # password = request.GET['password']
#             username=request.POST.get('username')
#             password=request.POST.get('password')
#             user=authenticate(request,username=username,password=password)
#             if user is not None:
#                 auth_login(request,user) # Log the user in
#                 print("Login successful")
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 error="Invalid credentials1"
#                 data['error']=error
#                 return render(request, 'login.html',data)
#             # url='/about/?output={}'.format(var)
#             # # return HttpResponseRedirect('/about/')
#             # return HttpResponseRedirect(url)
#     return render(request, 'login.html',data)

@gest
def login(request):
    fn = HelloForm()
    data = {'form': fn}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Log the user in
            print("Login successful")
            return HttpResponseRedirect(reverse('home'))  # Redirect to home page
        else:
            data['error'] = "Invalid credentials"
            return render(request, 'login.html', data)
    return render(request, 'login.html', data)

@gest
def signup(request):
        fn = signupform()
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                return render(request, 'signup.html', {'error': 'Passwords do not match'})

            try:
                user = User.objects.create_user(username, email, password1)
                user.is_active = False
                user.save()

                # Generate token and send verification email
                token = default_token_generator.make_token(user)
                print("\n ",token)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                print("\n ",uid)
                verification_link = request.build_absolute_uri(
                    reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
                )
                print("\n ",verification_link)
                subject = "Verify Your Email Address"
                message = f"Hi {user.username},\n\nPlease verify your email by clicking the link below:\n{verification_link}\n\nThank you!"
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
                return render(request, 'signup.html', {'success': 'Account created successfully. Please verify your email.'})
            except IntegrityError:
                return render(request, 'signup.html', {'error': 'Username already exists'})

        return render(request, 'signup.html', {'form': fn})

def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        print("\n ",uid)
        user = User.objects.get(pk=uid)
        print("\n ",user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Email already verified")
    else:
        return HttpResponse("The verification link is invalid or has expired")

def marks(request):
    form = marksheet()
    if request.method == 'POST':
        total=eval(request.POST.get('subject1'))
        total+=eval(request.POST.get('subject2'))
        total+=eval(request.POST.get('subject3'))
        total+=eval(request.POST.get('subject4'))
        total+=eval(request.POST.get('subject5'))
        per=math.ceil(total/500*100)
        div='fail'
        if(per>=60):
            div='first'
        elif(per>=50):
            div='second'
        elif(per>=35):
            div='third'
        return render(request,'marks.html', {'form': form, 'total': total, 'percentage': per,"div" :div})
    return render(request,'marks.html', {'form': form})

def submit(request):
    return render(request,'submitform.html')



