from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegistrationFrom

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('music-home')
    else:
        form = UserRegistrationFrom()
    return render(request, 'musicusers/register.html', {'form': form})
