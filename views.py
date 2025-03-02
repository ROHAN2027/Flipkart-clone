from django.shortcuts import render, redirect
from .forms import InfoForm
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # return redirect('/')  # Redirect to a success page or display a success message
            messages.success(request, 'Your message has been sent successfully!')
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = InfoForm()
    
    return render(request, 'contact.html', {'form': form})
