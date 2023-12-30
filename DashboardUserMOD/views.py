from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from movieapp.models import *
from django.contrib import messages
from AuthenticationApp.models import Profile
from SeriesApp.models import episode_comment, episode_review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def AllUsers(request):
    if request.user.is_superuser:
        all_users = Profile.objects.all()
        
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
    
    return render('home')

@login_required
def EditUser(request, email):
    if request.user.is_superuser:
        get_profile = Profile.objects.get(email=email) 
        get_user = User.objects.get(email=email)

        all_comments_movie = comment.objects.all()
        all_series_comments = episode_comment.objects.all()
        total_comments = 0
        for i in  all_comments_movie:
            total_comments+=1
        for i in all_series_comments:
            total_comments+=1
    else:
        return redirect('home')


    series_comment = episode_comment.objects.filter(name=get_user)
    movie_comments  = comment.objects.filter(name=get_user)
    number_of_comment_by_user = 0
    for i in series_comment:
        number_of_comment_by_user+=1

    for i in movie_comments:
        number_of_comment_by_user+=1

    movie_review = reviewss.objects.filter(name=get_user)
    series_reviews = episode_review.objects.filter(name=get_user)
    all_movie_review = reviewss.objects.all()
    all_series_review = episode_review.objects.all()

    user_reviews = 0
    for i in movie_review:
        user_reviews+=1
    for i in series_reviews:
        user_reviews+=1

    all_reviews = 0
    for i in all_series_review:
        all_reviews+=1
    for i in all_series_review:
        all_reviews+=1

    context = {
        'profile': get_profile,
        'episode': series_comment,
        'movie': movie_comments,
        'user_comment': number_of_comment_by_user,
        'number_of_comments': total_comments,
        'movie_review': movie_review,
        'series_review': series_reviews,
        'user_review': user_reviews,
        'number_of_revs': all_reviews,
        'user': get_user,
    }
    return render(request, 'dashboard/edit-user.html', context)

@login_required
def BanUser(request, email):
    if request.user.is_superuser:
        get_profile = Profile.objects.get(email=email) 
        if get_profile.verified == True:
            get_profile.verified = False
            get_profile.save()
            return redirect('users')
        else:
            get_profile.verified = True
            get_profile.save()
            return redirect('users')
    else:
        return redirect('home')

@login_required
# EDIT USER VIEWS
def EditProfileDetails(request, email):
    if request.user.is_superuser:
        get_profile = Profile.objects.get(email=email) 
        get_user = User.objects.get(email=email)
        series_comment = episode_comment.objects.filter(name=get_user)

        if request.method == 'POST':        
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            subscription = request.POST.get('subscription')
            user_type = request.POST.get('user_type')

            if username:
                get_user.username = username
                get_profile.user_name = username
                get_user.save()
            if email:
                get_user.email = email
                get_profile.email = email
                get_user.save()
            if first_name:
                get_user.first_name = first_name
                get_user.save()
            if last_name:
                get_user.last_name = last_name
                get_user.save()
            if subscription:
                get_profile.pricing_plan = subscription
                get_profile.save()
            if user_type:
                if user_type == 'Admin':
                    get_user.is_superuser = True
                    get_user.save()
                elif user_type == 'User':
                    get_user.is_superuser = False
                    get_user.save()
            messages.success(request, 'Profile Updated Successfully')
            return render(request, 'dashboard/edit-user.html', {'profile': get_profile})

        return render(request, 'dashboard/edit-user.html', {'profile': get_profile, 'episode': series_comment})
    else:
        return redirect('home')
    
@login_required
def VerifiedUsers(request):
    if request.user.is_superuser:
        all_users = Profile.objects.filter(verified=True)
        
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
    
    return redirect('home')
    
@login_required
def BannedUsers(request):
    if request.user.is_superuser:
        all_users = Profile.objects.filter(verified=False)
        
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
    return redirect('home')