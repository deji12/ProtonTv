from django.shortcuts import render, redirect
from movieapp.models import movie, series, comment, reviewss
from AuthenticationApp.models import Profile
from Globals.models import *
from SeriesApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def DashboardHome(request):
    if request.user.is_superuser:
        all_movies = movie.objects.all().order_by('-clicks')[:5]
        all_series = series.objects.all().order_by('-clicks')[:5]
        new_movies = movie.objects.all().order_by('-date_added')[:5]
        new_series = series.objects.all().order_by('-series_air_date')[:5]
        new_reviews = episode_review.objects.all().order_by('-date')[:5]
        all_users = User.objects.all().order_by('-username')[:5]

        final = 0
        for i in comment.objects.all():
            final+=1
        for j in episode_comment.objects.all():
            final+=1

        final_review_num = 0
        for i in reviewss.objects.all():
            final_review_num+=1
        
        for j in episode_review.objects.all():
            final_review_num+=1

        context = {
            'movies': all_movies, 
            'series': all_series,
            'new_movies': new_movies,
            'new_series': new_series,
            'new_review': new_reviews,
            'users': all_users,
            'total_comments': final,
            'total_reviews': final_review_num,
        }
        return render(request, 'dashboard/index.html', context)
    else:
        return redirect('home')

@login_required
def Catalog(request):
    if request.user.is_superuser:
        all_movies = movie.objects.all().order_by('-clicks')
        all_series = series.objects.all().order_by('-clicks')
        final = 0
        for i in all_movies:
            final+=1
        for j in all_series:
            final+=1
        context = {
            'movies': all_movies, 
            'series': all_series,
            'content': final
        }
        return render(request, 'dashboard/catalog.html', context)
    else:
        return redirect('home')

@login_required
def NotFound(request):
    if request.user.is_superuser:
        context = {
            
        }
        return render(request, 'dashboard/pages.html', context)
    else:
        return redirect('home')

@login_required
def AddNewItem(request):
    if request.user.is_superuser:
        context = {
            
        }
        return render(request, 'dashboard/add-item.html', context)
    else:
        return redirect('home')

@login_required
def DraftPostSeries(request, name):
    if request.user.is_superuser:
        get_series = series.objects.get(name=name)
        if get_series.draft == False:
            get_series.draft = True
            get_series.save()
            return redirect('catalog')
        else:
            get_series.draft = False
            get_series.save()
            return redirect('catalog')
    else:
        return redirect('home')
    
@login_required
def DraftPostMovies(request, name):
    if request.user.is_superuser:
        get_movie = movie.objects.get(name=name)
        if get_movie == False:
            get_movie.draft = True
            get_movie.save()
            return redirect('catalog')
        else:
            get_movie.draft = False
            get_movie.save()
            return redirect('catalog')
    else:
        return redirect('home')

@login_required
def ChangePassword(request, email):
    if request.user.is_superuser:
        get_user = User.objects.get(email=email)
        get_profile = Profile.objects.get(email=email)
        
        if request.method == 'POST':
            oldpassword = request.POST.get('oldpass')
            newpassword = request.POST.get('newpass')
            confirmpassword = request.POST.get('confirmpass')

            if len(confirmpassword) < 5:
                messages.success(request, 'Password too short')
                return render(request, 'dashboard/edit-user.html', {'profile': get_profile})

            auth_user = authenticate(username=get_user.username, password=oldpassword)
        
            if auth_user is not None:
                if confirmpassword != newpassword:
                    messages.success(request, 'Passwords do not match')
                    return render(request, 'dashboard/edit-user.html', {'profile': get_profile})
                else:
                    get_user.set_password(confirmpassword)
                    get_user.save()
                    messages.success(request, 'Password changed successfully')
                    return render(request, 'dashboard/edit-user.html', {'profile': get_profile})
            else:
                messages.success(request, 'Error, wrong details')
                return render(request, 'dashboard/edit-user.html', {'profile': get_profile})
    else:
        return redirect('home')

@login_required     
def search(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            search_val = request.POST.get('search')
            user_search = request.POST.get('search-user')
            print(user_search)
            if user_search:
                if '@' in user_search:
                    search_for_user_by_email = Profile.objects.filter(email=user_search)
                    print(search_for_user_by_email)
                    context = {
                        'all_users': search_for_user_by_email,
                        'search': user_search,
                    }
                    return render(request, 'dashboard/users.html', context)

                else:
                    search_for_user_by_username = Profile.objects.filter(user_name=user_search)
                    print(search_for_user_by_username)
                    context = {
                        'all_users': search_for_user_by_username,
                        'search': user_search,
                    }
                    return render(request, 'dashboard/users.html', context)

            if search_val:
                filter_movie_for_search = movie.objects.filter(name__icontains=search_val)
                filter_series_for_search = series.objects.filter(name__icontains=search_val)

                final = 0
                for i in filter_movie_for_search:
                    final+=1
                for i in filter_series_for_search:
                    final+=1

                context = {
                    'movie_result': filter_movie_for_search,
                    'series_result': filter_series_for_search,
                    'search': search_val,
                    'final': final,
                }
                return render(request, 'dashboard/search.html', context)
    else:
        return redirect('home')

@login_required
def Date_Created(request):
    if request.user.is_superuser:
        all_movies = movie.objects.all().order_by('-date_added')
        all_series = series.objects.all().order_by('-series_air_date')
        final = 0
        for i in all_movies:
            final+=1
        for j in all_series:
            final+=1
        context = {
            'movies': all_movies, 
            'series': all_series,
            'content': final
        }
        return render(request, 'dashboard/catalog.html', context)
    else:
        return redirect('home')

@login_required
def DateUserCreated(request):
    if request.user.is_superuser:
        all_users = Profile.objects.all().order_by('-creation_date')
        user_number = 0
        for i in all_users:
            user_number+=1
        
        context = {
            'all_users': all_users,
            'user_num': user_number,
        }
        return render(request, 'dashboard/users.html', context)
    else:
        return redirect('home')