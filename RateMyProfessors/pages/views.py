from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from Account.forms import UserUpdateForm, ImageUpdateForm

from . utils import getErrorMessage

from Lecturer.models import Lecturer
from University.models import University

from Review.models import UniReview, LecturerReview
from Review.utils import calcUniRating, getStarsPercentage
from Review.filters import UniReviewFilter, LecReviewFilter

from django.core.paginator import Paginator

import json
from django.http import JsonResponse

import random

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'pages/home.html')


def universities(request):
    uni_list = University.objects.all()
    context = {
        'universities': uni_list
    }
    return render(request, 'pages/universities.html', context)

def lecturers(request):
    lecturer_list = Lecturer.objects.all()
    context = {
        'lecturers': lecturer_list
    }
    return render(request, 'pages/lecturers.html', context)

def lecturer(request, id):
    if request.user.is_authenticated: 
        # curr lecturer
        lec = Lecturer.objects.get(id=id)
        # all review of curr lec
        reviews = LecturerReview.objects.filter(lecturer=lec)
        # all review count of curr uni
        reviewsCount = reviews.count()
        # find if user can vote
        canVote = False if LecturerReview.objects.filter(lecturer=lec, user=request.user) else True
        # # get curr uni rating
        rating = calcUniRating(None, lec)
        # # get curr uni stars percentage
        starsPercentage = getStarsPercentage(None, lec)

        # filter
        myFilter = LecReviewFilter(request.GET, queryset=reviews)
        reviews = myFilter.qs

        # pagination
        paginator = Paginator(reviews, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'lec': lec,
            'reviews': reviews,
            'reviewsCount': reviewsCount,
            'canVote': canVote,
            'rating': rating,
            'starsPercentage': starsPercentage,
            'myFilter': myFilter,
            'page_obj': page_obj
        }

        if request.method == "POST":
            score = request.POST.get('star', False)
            isAnonymous = request.POST.get('Anonymous', False);
            text = request.POST['reviewText']
            user = None
            if isAnonymous == False:
                user = request.user
        
            if score and text:
                LecturerReview.objects.create(
                    lecturer = lec,
                    user = user,
                    score = score,
                    text = text
                )
            else:
                messages.info(request, 'sorry but this is true')
                
            
            return redirect('lecturer', lec.id)
    else:
        return redirect('login')
    return render(request, 'pages/lecturer.html', context)

def university(request, id):
    if request.user.is_authenticated: 
        # curr uni
        uni = University.objects.get(id=id)
        # all review of curr uni
        reviews = UniReview.objects.filter(university=uni)
        # all review count of curr uni
        reviewsCount = reviews.count()
        # find if user can vote
        canVote = False if UniReview.objects.filter(university=uni, user=request.user) else True
        # get curr uni rating
        rating = calcUniRating(uni)
        # get curr uni stars percentage
        starsPercentage = getStarsPercentage(uni)

        # filter
        myFilter = UniReviewFilter(request.GET, queryset=reviews)
        reviews = myFilter.qs


        # pagination
        paginator = Paginator(reviews, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        
        context = {
            'uni': uni,
            'reviews': reviews,
            'reviewsCount': reviewsCount,
            'canVote': canVote,
            'rating': rating,
            'starsPercentage': starsPercentage,
            'myFilter': myFilter,
            'page_obj': page_obj
        }
        
        
        if request.method == "POST":
            score = request.POST.get('star', False)
            isAnonymous = request.POST.get('Anonymous', False);
            text = request.POST['reviewText']
            user = None
            if isAnonymous == False:
                user = request.user
            
            if score and text:
                UniReview.objects.create(
                    university = uni,
                    user = user,
                    score = score,
                    text = text
                )
            else:
                messages.info(request, 'sorry but this is true')
                
            
            return redirect('university', uni.id)
    else:
        return redirect('login')
    
    return render(request, 'pages/university.html', context)

    

def profile(request, id):
    if request.user.is_authenticated: 

        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=request.user)
            img_form = ImageUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)

            if form.is_valid():
                form.save()
                img_form.save()
                messages.success(
                    request, f'Account was successfully updated.')
                return redirect('profile', request.user.id)
            else:
                errMsg = getErrorMessage(form)
                if errMsg:
                    messages.info(request, f'{errMsg}')

                return redirect('profile', request.user.id)

        else:
            form = UserUpdateForm(instance=request.user)
            img_form = ImageUpdateForm(instance=request.user.profile)

        context = {
            'form': form,
            'img_form': img_form
        }
    else:
        return redirect('login')
    return render(request, 'pages/profile.html', context)


def deleteUniReview(request, id):
    if request.method == 'POST':
        review = UniReview.objects.get(id=id)
        if review.user == request.user:
            review.delete()
            messages.info(
                request, f'Review was removed successfuly')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def deleteLecReview(request, id):
    if request.method == 'POST':
        review = LecturerReview.objects.get(id=id)
        if review.user == request.user:
            review.delete()
            messages.info(
                request, f'Review was removed successfuly')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def homeSearch(request):
    print('view recived call')
    if request.method == 'POST':
        # get request body
        reqData = json.loads(request.body)
        searchVal = reqData['searchValue']
        uniData = University.objects.filter(
            name__istartswith=searchVal ) | University.objects.filter (
            short_name__istartswith=searchVal) 

        lectData = Lecturer.objects.filter(
            first_name__istartswith=searchVal 
        ) | Lecturer.objects.filter(last_name__istartswith=searchVal)

        data = []
        data += lectData.values()
        data += uniData.values()
        
        # print(type(data))
        new_data = random.sample( data, len(data) )

        # data.append(list(uniData.values()))
        # data.append(list(lectData.values()))

        # print(lectData.values()) 

        return JsonResponse(list(new_data), safe=False)
        
            
        
