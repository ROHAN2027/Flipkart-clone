from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             username=request.user.username
#             messages.success(request, f'Profile updated for {username}!')
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profile.html', {'form': form})
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            print("Form is valid. Saving profile...")
            form.save()
            username = request.user.username
            messages.success(request, f'Profile updated for {username}!')
            return redirect('profile')
        else:
            messages.error(request,f'{form.errors}') # Print any form errors to the console for debugging
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'profile.html', {'form': form})
