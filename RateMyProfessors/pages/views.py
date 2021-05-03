from django.shortcuts import render, redirect
from Account.forms import UserUpdateForm, ImageUpdateForm
from django.contrib import messages
from . utils import getErrorMessage
from University.models import University, UniReview
from University.utils import calcUniRating, getStarsPercentage
from University.filters import UniReviewFilter, LecReviewFilter
from django.core.paginator import Paginator
from Lecturer.models import Lecturer, LecturerReview

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

    return render(request, 'pages/lecturer.html', context)


def university(request, id):
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

    
    return render(request, 'pages/university.html', context)

    


def profile(request, id):
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

    return render(request, 'pages/profile.html', context)
