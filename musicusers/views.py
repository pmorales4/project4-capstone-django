from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegistrationFrom
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
    return render(request, 'musicusers/profile.html')