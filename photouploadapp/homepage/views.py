from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Photo

@login_required
def mainhome(request):
	logged_user=request.user
	Photos= Photo.objects.filter(photo_uploader=logged_user).order_by('-uploaded_at')
	context = {'Photos' : Photos}
	return render(request, 'homepage/index.html', context)
    

def model_form_upload(request):
	if request.user.is_authenticated:
		photo_uploader = request.user
		if request.method == 'POST':
			form = DocumentForm(request.POST, request.FILES)
			if form.is_valid():
				document= form.cleaned_data.get('document')
				Photo.objects.create(
                	photo_uploader=photo_uploader,
                	document=document,
                )
				return redirect('upload')
		else:
			form = DocumentForm()
		return render(request, 'homepage/model_form_upload.html', {'form': form})

