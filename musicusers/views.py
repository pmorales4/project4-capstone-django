from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegistrationFrom, UpdateUserForm, UpdateProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account is created you can login!')
            return redirect('login')
    else:
        form = UserRegistrationFrom()
    return render(request, 'musicusers/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
    # make instance of the two added
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfile(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your accoutn is updated!')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfile(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form

    }
    return render(request, 'musicusers/profile.html', context)