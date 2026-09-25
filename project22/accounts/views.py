from django.shortcuts import render, redirect 
from .forms import ProfileForm
from .models import profile
from django.contrib import messages

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile uploaded successfully!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Error uploading profile. Please check the form.')
    else:
        form = ProfileForm()
    return render(request, 'accounts/upload_profile.html', {'form': form})

def view_profile(request):
    profiles = profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles': profiles})
