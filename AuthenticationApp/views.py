from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from AuthenticationApp.models import Profile
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from movieapp.models import movie, series, comment, reviewss
from Globals.models import *
from SeriesApp.models import *
from SeriesApp.models import episode_review as er

def reset_password(request):
    myuser = User.objects.get(username=request.user)
    if request.method == 'POST':
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        confirm = request.POST['confirmpass']

        auth_user = authenticate(username=request.user, password=oldpass)
        if auth_user is not None:
            if newpass == confirm:
                myuser.set_password(confirm)
                myuser.save()
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('profile')
        else:
            messages.error(request, 'You entered a wrong password')
            return redirect('profile')

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST['username']
        pass1 = request.POST['pass'] 
        
        my_user = authenticate(username=uname, password=pass1)
        if my_user is not None:
            get_profile = Profile.objects.get(user=my_user)
            if get_profile.verified  == False:
                messages.error(request, 'Your account has been temporarily banned due to misconduct.')
                return redirect('login')
            login(request, my_user)
            if request.POST.get('next'):
                return redirect(request.POST['next'])
            
            return redirect('home')
        else:
            messages.error(request, 'Invalid password')
            return redirect('login')   
    
    return render(request, 'movieapp/signin.html', {})

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST['name']
        user_name = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass']

        if len(pass1) < 8:
            messages.error(request, 'Password is too short.')
            return redirect('register')

        check_username = User.objects.filter(username=name)
        if check_username:
            messages.error(request, 'Username already exists.')
            return redirect('register')

        check_email = User.objects.filter(email=email)
        if check_email:
            messages.error(request, 'Email already exists.')
            return redirect('register')

        try:
            first_name = name.split()[0]
            last_name = name.split()[1]

            new_user = User.objects.create_user(username=user_name, email=email, password=pass1)
            new_user.first_name=first_name
            new_user.last_name  = last_name
            new_user.save()

            new_profile = Profile(user=new_user, email=email, user_name=user_name)
            new_profile.save()

            messages.success(request, 'User successfully created. Login')
            return redirect('login')
        except:
            messages.success(request, 'Enter first & last names')
            return redirect('register')


    return render(request, 'movieapp/signup.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']
        check = User.objects.filter(email=email)
        if check:
            user=User.objects.get(email=email)
            email_templat_name = 'movieapp/email_template.html'

            c = {
                'username': user.username
            }
            emaill = render_to_string(email_templat_name, c)     

            email_mess = EmailMessage (
                'ProtonTv Password Reset',
                emaill,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_mess.fail_silently = True
            email_mess.content_subtype = 'html'
            email_mess.send()
            messages.success(request, 'We have sent you an email that will help you reset your password.')
            return redirect('reset-sent')
        else:
            messages.error(request, 'No user with that email exists')
            return redirect('fp')    

    return render(request, 'movieapp/forgot.html', {})

def password_reset_sent(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'movieapp/password-reset-sent.html', {})

def PasswordResedtView(request, name):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('reset_view')
        if len(pass1) < 5:
            messages.error(request, 'Password cannot be less than 5 characters')
            return redirect('reset_view')

        user = User.objects.get(username=name)
        user.set_password(pass2)
        user.save()
        messages.success(request, 'Password successfully changed. Login now')
        return redirect('login')

    return render(request, 'movieapp/password-reset-form.html', {})

@login_required
def profile(request):
    my_user = User.objects.get(username=request.user)
    
    # update profile
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')
        confirm = request.POST.get('confirm')

        if oldpass:
            auth_user = authenticate(username=request.user.username,  password=oldpass)
            if auth_user is not None:
                if newpass == confirm:
                    my_user.set_password(confirm)
                    my_user.save()
                    logout(request)
                    return HttpResponse( 'Password updated successfully!. You will be redirected to the login page in a few seconds')
                else:
                    return HttpResponse('New & confirm password do not match!')
            else:
                return HttpResponse('Wrong details or user does not exist!')

        if username:
            my_user.username = username
            my_user.save()
            
        if email:
            my_user.email = email
            my_user.save()
            
        if name:
            fname = name.split()[0]
            lname = name.split()[1]
            my_user.first_name = fname
            my_user.last_name = lname
            my_user.save()
            
        return HttpResponse('Profile successfully updated')
    
    #get latest reviews
    get_reviews = reviewss.objects.filter(name=request.user)
    episode_review = er.objects.all().order_by('-date')[:5]

    #order movies by clicks
    for_you = series.objects.all().order_by('-clicks')[:4]
    for_you_movie = movie.objects.all().order_by('-clicks')[:4]

    context = {
        'for_you_series': for_you,
        'for_you_movie': for_you_movie,
        'episode_review': episode_review,
    }
    return render(request, 'movieapp/profile.html', context)