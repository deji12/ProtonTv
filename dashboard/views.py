from django.shortcuts import render, redirect
from movieapp.models import movie, series, comment, reviewss
from AuthenticationApp.models import Profile
from Globals.models import *
from SeriesApp.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

@login_required
def DashboardHome(request):
    if request.user.is_superuser:
        all_movies = movie.objects.all().order_by('-clicks')[:5]
        all_series = series.objects.all().order_by('-clicks')[:5]
        new_movies = movie.objects.all().order_by('-date_added')[:5]
        new_series = series.objects.all().order_by('-series_air_date')[:5]
        new_reviews = episode_review.objects.all().order_by('-date')[:5]
        all_users = User.objects.all().order_by('-username')[:5]

        number_of_comments = comment.objects.count() + episode_comment.objects.count()
        number_of_reviews = reviewss.objects.count() + episode_review.objects.count()

        context = {
            'movies': all_movies, 
            'series': all_series,
            'new_movies': new_movies,
            'new_series': new_series,
            'new_review': new_reviews,
            'users': all_users,
            'total_comments': number_of_comments,
            'total_reviews': number_of_reviews,
            'number_of_movies': movie.objects.count(),
            'number_of_series': series.objects.count(),
        }
        return render(request, 'dashboard/index.html', context)
    else:
        return redirect('home')

@login_required
def MovieCatalog(request):
    if request.user.is_superuser:
        all_movies = movie.objects.all().order_by('-clicks')
        # all_series = series.objects.all().order_by('-clicks')
        p = Paginator(all_movies, 10)
        page = request.GET.get('page')
        page_series = p.get_page(page)

        try:
            # Get the current page's items
            current_page_items = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            current_page_items = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            current_page_items = p.page(p.num_pages)

        total_items = p.count
        start_index = current_page_items.start_index()
        end_index = current_page_items.end_index()

        context = {
            'content': all_movies.count(),
            'pages': page_series,
            'start_index': start_index,
            'end_index': end_index,
            'total_items': total_items,
        }
        return render(request, 'dashboard/catalog.html', context)
    
    return redirect('home')
    
@login_required
def SeriesCatalog(request):
    if request.user.is_superuser:
        all_series = series.objects.all().order_by('-clicks')
        p = Paginator(all_series, 10)
        page = request.GET.get('page')
        page_series = p.get_page(page)

        try:
            # Get the current page's items
            current_page_items = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            current_page_items = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            current_page_items = p.page(p.num_pages)

        # Pass additional information to the template context
        total_items = p.count
        start_index = current_page_items.start_index()
        end_index = current_page_items.end_index()
        context = {
            'content': all_series.count(),
            'pages': page_series,
            'start_index': start_index,
            'end_index': end_index,
            'total_items': total_items,
        }
        return render(request, 'dashboard/seriescatalog.html', context)

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
            return redirect('series-catalog')
        else:
            get_series.draft = False
            get_series.save()
            return redirect('series-catalog')
    else:
        return redirect('home')
    
@login_required
def DraftPostMovies(request, name):
    if request.user.is_superuser:
        get_movie = movie.objects.get(name=name)
        if get_movie.draft == False:
            get_movie.draft = True
            get_movie.save()
            return redirect('catalog')
        else:
            get_movie.draft = False
            get_movie.save()
            return redirect('catalog')
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
    if request.user.is_superuser and request.method == 'POST':
        
        movie_search = request.POST.get('search')
        series_search = request.POST.get('series-search')
        user_search = request.POST.get('search-user')
    
        if user_search:

            context = {'search': user_search,}
            
            profiles = Profile.objects.filter(
                Q(user__first_name__icontains=user_search) |
                Q(user__last_name__icontains=user_search) |
                Q(user__username__icontains=user_search) |
                Q(email__icontains=user_search)
            )
            context['all_users'] = profiles

            return render(request, 'dashboard/users.html', context)

        if movie_search:
            filter_movie_for_search = movie.objects.filter(name__icontains=movie_search)

            p = Paginator(filter_movie_for_search, 10)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            try:
                # Get the current page's items
                current_page_items = p.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                current_page_items = p.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                current_page_items = p.page(p.num_pages)

            # Pass additional information to the template context
            total_items = p.count
            start_index = current_page_items.start_index()
            end_index = current_page_items.end_index()

            context = {
                'pages': page_series,
                'start_index': start_index,
                'end_index': end_index,
                'total_items': total_items,
                'search': movie_search,
                'final': filter_movie_for_search.count(),
            }
            return render(request, 'dashboard/search.html', context)
        
        if series_search:
            filter_series_for_search = series.objects.filter(name__icontains=series_search)

            p = Paginator(filter_series_for_search, 10)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            try:
                # Get the current page's items
                current_page_items = p.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                current_page_items = p.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                current_page_items = p.page(p.num_pages)

            # Pass additional information to the template context
            total_items = p.count
            start_index = current_page_items.start_index()
            end_index = current_page_items.end_index()

            context = {
                'pages': page_series,
                'start_index': start_index,
                'end_index': end_index,
                'total_items': total_items,
                'search': series_search,
                'final': filter_series_for_search.count(),
            }
            return render(request, 'dashboard/search.html', context)
    
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
        
        p = Paginator(all_users, 10)
        page = request.GET.get('page')
        page_series = p.get_page(page)

        try:
            # Get the current page's items
            current_page_items = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            current_page_items = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            current_page_items = p.page(p.num_pages)

        total_items = p.count
        start_index = current_page_items.start_index()
        end_index = current_page_items.end_index()
        
        context = {
            'pages': page_series,
            'start_index': start_index,
            'end_index': end_index,
            'total_items': total_items,
            'user_num': all_users.count(),
        }
        return render(request, 'dashboard/users.html', context)
    else:
        return redirect('home')