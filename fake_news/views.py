from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from .models import Prediction, Image
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from . import prediction
import numpy as np


def home(request):
    return render(request, 'fake_news/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In!')
            return redirect('home')
        else:
            messages.success(request, 'Error Logging In - Please Try Again...')
            return redirect('login')
    else:
        return render(request, 'fake_news/login.html', {})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Registered')
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'fake_news/register.html', context)


@login_required(login_url='login')
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Edited Your Profile,,,')
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'fake_news/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You Have Edited Your Password...')
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)

    context = {'form': form}
    return render(request, 'fake_news/change_password.html', context)


@login_required(login_url='login')
def user_history(request):
    history_data = Prediction.objects.filter(user_id=request.user.id)
    return render(request, "fake_news/history.html", {"data": history_data})


@login_required(login_url='login')
def predict(request):
    if request.method == 'POST':
        try:
            news = request.POST['news']
            data = np.array(news)
            time = timezone.now()
            mnb2pred, rfpred, decisionpred, svmpred, knnpred, hybrid = prediction.predict(data)
            q = Prediction(
                news=news,
                mnb2pred=mnb2pred,
                rfpred=rfpred,
                decisionpred=decisionpred,
                svmpred=svmpred,
                knnpred=knnpred,
                hybrid=hybrid,
                predicted_date=time,
                user_id=request.user.id
            )
            q.save()
            images = Image.objects.all()
            images = [i.image.url for i in images]
            return render(request, 'fake_news/prediction.html', {"data": {"Naive Bayes": [mnb2pred, images[0]],
                                                                          "Random Forest": [rfpred, images[1]],
                                                                          "Decision Tree": [decisionpred, images[2]],
                                                                          "SVM": [svmpred, images[3]],
                                                                          "K Nearest Neighbours": [knnpred, images[4]],
                                                                          "Hybrid": [hybrid, images[5]]},
                                                                 "news": news,
                                                                 "time": time
                                                                 }
                          )
        except:
            messages.success(request, 'Error : Invalid Expression')
            return redirect('home')
    else:
        return render(request, 'fake_news/home.html', {})

# def detail(request, algorithm_id):
#     algo_details = get_object_or_404(Prediction, pk=algorithm_id)
#     return render(request, 'fake_news/detail.html', {'algo': algo_details})
