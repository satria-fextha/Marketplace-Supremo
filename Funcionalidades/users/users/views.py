Funcionalidades/users/users/views.py
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {email}!')
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def send_verification_email(email):
    subject = 'Verify your email'
    message = 'Please click the link below to verify your email:\n\nhttp://localhost:8000/users/verify_email/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def verify_email(request):
    if request.method == 'GET':
        user = request.user
        user.profile.email_verified = True
        user.profile.save()
        messages.success(request, 'Email verified successfully!')
        return redirect('home')
    else:
        return HttpResponse('Invalid request')

def farmer_register(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.user_type = 'farmer'
            user.profile.save()
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = FarmerSignUpForm()
    return render(request, 'users/farmer_register.html', {'form': form})

def rancher_register(request):
    if request.method == 'POST':
        form = RancherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.user_type = 'rancher'
            user.profile.save()
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = RancherSignUpForm()
    return render(request, 'users/rancher_register.html', {'form': form})

def consumer_register(request):
    if request.method == 'POST':
        form = ConsumerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.user_type = 'consumer'
            user.profile.save()
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = ConsumerSignUpForm()
    return render(request, 'users/consumer_register.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FarmerSignUpForm, RancherSignUpForm, ConsumerSignUpForm, ProfileForm
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {email}!')
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def send_verification_email(email):
    subject = 'Verify your email'
    message = 'Please click the link below to verify your email:\n\nhttp://localhost:8000/users/verify_email/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def verify_email(request):
    if request.method == 'GET':
        user = request.user
        user.profile.email_verified = True
        user.profile.save()
        messages.success(request, 'Email verified successfully!')
        return redirect('home')
    else:
        return HttpResponse('Invalid request')

def farmer_register(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.groups.add(Group.objects.get(name='Farmer'))
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = FarmerSignUpForm()
    return render(request, 'users/farmer_register.html', {'form': form})

def rancher_register(request):
    if request.method == 'POST':
        form = RancherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.groups.add(Group.objects.get(name='Rancher'))
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = RancherSignUpForm()
    return render(request, 'users/rancher_register.html', {'form': form})

def consumer_register(request):
    if request.method == 'POST':
        form = ConsumerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.groups.add(Group.objects.get(name='Consumer'))
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            send_verification_email(user.email)
            return redirect('home')
    else:
        form = ConsumerSignUpForm()
    return render(request, 'users/consumer_register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})
