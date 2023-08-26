from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'], 
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
            else:
                 return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
    
@login_required
def dashboard(request):
    return render (request,
                   'account/dashboard.html',
                   {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but do not save it yet
            new_user = user_form.save(commit=0)
            # set the chosen password for this new user
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # save the user object
            new_user.save()
            # create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(
        request,'account/register.html', {'user_form': user_form}
    )

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
             data=request.POST
        )
        profile_form = ProfileEditForm(
            instance=Profile.objects.get(),
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile
        )
    return render(request,
                  'account/edit.html',
                  {'user_form' : user_form,
                    'profile_form': profile_form }
                    )
                  
                