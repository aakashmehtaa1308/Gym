from typing import Counter
from django import urls
from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from gym_app.models import Food, Profile,FoodTaken
# from app_accounts.models import User
from .forms import RegistrationForm, ProfileForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User

# from django.contrib.auth.models import User
# Create your views here.

def SignIn(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                urlTo=reverse('home')
                return HttpResponseRedirect(urlTo)
            else:
                urlTo=reverse('signin')
                messages.error(request,'username or password not correct')
                return HttpResponseRedirect(urlTo)
        form=AuthenticationForm()
        return render(request,'gym_app/signin.html',{'form':form})
    else:
        urlTo=reverse('home')
        return HttpResponseRedirect(urlTo)

def Signout(request):
    if request.user.is_authenticated:
        logout(request)
        urlTo=reverse('home')
        return HttpResponseRedirect(urlTo+'signin')
    urlTo=reverse('home')
    return HttpResponseRedirect(urlTo+'signin')

def SignUpPage(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully') 
                urlTo=reverse('home')
                return  HttpResponseRedirect(urlTo+'signin')
            return  render(request,'gym_app/signup.html',{'form':form})
        else:
            form=RegistrationForm()
            return  render(request,'gym_app/signup.html',{'form':form})
    urlTo=reverse('home')
    return HttpResponseRedirect(urlTo)

def Thankyou(request):
    return render(request, 'gym_app/thankyou.html')

def HomePage(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=ProfileForm(request.POST)
            if form.is_valid():

                height=form.cleaned_data['height']
                weight=form.cleaned_data['weight']
                category=form.cleaned_data['category']
                goal=form.cleaned_data['goal']

                print(request.user.username)

                profile=Profile.objects.filter(user=request.user)

                print(profile)

                if len(profile)>0:
                    profile=profile[0]
                    profile.height=height
                    profile.weight=weight
                    profile.category=category
                    profile.goal=goal
                    messages.success(request,'Profile updated successfully')
                else:
                    profile = Profile(user=request.user,height=height,weight=weight,category=category,goal=goal)
                    messages.success(request,'profile created successfully')
                profile.save()


                urlTo=reverse('home')
                return HttpResponseRedirect(urlTo)

            print('not valid')
            return render(request,'gym_app/home.html',{'form':form})
        form=ProfileForm()
        profile=Profile.objects.filter(user=request.user)
        if len(profile):
            return render(request,'gym_app/home.html',{'form':form,'profile':profile[0]})
        return render(request,'gym_app/home.html',{'form':form})
    return render(request,'gym_app/home.html')

def CaloriePage(request):
    if request.method=='POST':
        ingredient1=request.POST['ingredient1']
        ingredient2=request.POST['ingredient2']
        ingredient3=request.POST['ingredient3']
        ingredient4=request.POST['ingredient4']
        fooditems=Food.objects.all()

        Counter=fooditems[int(ingredient1)-1].calories
        Counter+=fooditems[int(ingredient2)-1].calories
        Counter+=fooditems[int(ingredient3)-1].calories
        Counter+=fooditems[int(ingredient4)-1].calories
        
        

        f1=FoodTaken(user=request.user,ingredient1=fooditems[int(ingredient1)-1].name,ingredient2=fooditems[int(ingredient2)-1].name,ingredient3=fooditems[int(ingredient3)-1].name,ingredient4=fooditems[int(ingredient4)-1].name,calorie_count=Counter)
        f1.save()

        messages.success(request,f'your calories count is = {Counter}')
        urlTo=reverse('calorie')
        return HttpResponseRedirect(urlTo)
    profile=Profile.objects.get(user=request.user)
    fooditems=Food.objects.filter(category = profile.category)
    diets=FoodTaken.objects.filter(user=request.user)
    return render(request,'gym_app/calorie.html',{'choices':fooditems,'diets':diets})