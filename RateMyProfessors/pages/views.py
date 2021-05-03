from django.shortcuts import render, redirect
from Account.forms import UserUpdateForm, ImageUpdateForm
from django.contrib import messages
from . utils import getErrorMessage
from University.models import University, UniReview


def home(request):
    return render(request, 'pages/home.html')


def universities(request):
    uni_list = University.objects.all()
    context = {
        'universities': uni_list
    }
    return render(request, 'pages/universities.html', context)


def lecturers(request):
    return render(request, 'pages/lecturers.html')


def university(request, id):
    uni = University.objects.get(id=id)
    reviews = UniReview.objects.filter(university=uni)
    canRate = True
    userReview = UniReview.objects.filter(university=uni, user=request.user)
    if userReview:
        canRate = False
    

    stars1 = UniReview.objects.filter(university=uni, score=1).count()
    stars2 = UniReview.objects.filter(university=uni, score=2).count()
    stars3 = UniReview.objects.filter(university=uni, score=3).count()
    stars4 = UniReview.objects.filter(university=uni, score=4).count()
    stars5 = UniReview.objects.filter(university=uni, score=5).count()

    total = stars1+stars2+stars3+stars4+stars5
    rating = 'N/A'
    if total != 0:        
        rating = (5*stars5 + 4*stars4 + 3*stars3 + 2*stars2 + 1*stars1) / (total)
        rating = "{:.1f}".format(rating)
    
    print(rating)
    
    context = {
        'uni': uni,
        'reviews': reviews,
        'canRate': canRate,
        'rating': rating
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

        
        print(rating, isAnonymous, text)
    
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
