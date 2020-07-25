from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .tokens import account_activation_token
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import login, authenticate
import json
from .models import Profile

def home(request):
    return render(request, 'user/index.html')


def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('user/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        subject, message, to=[to_email]
            )
            email.send()
            return redirect('activation_sent.html')
    else:
         form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def get_jwt_token(user):
    

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    # create payload for authorised
    payload = jwt_payload_handler(user)
    print(payload)
    print(jwt_encode_handler(payload))
    # return encoded payload
    return jwt_encode_handler(payload)

def user_login(request):
    
    if request.method == 'POST':
        # get username and password from submitted form
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check for authentication
        user = authenticate(username=username, password=password)
        # user is valid
        
        if user:
            if user.is_active:
                login(request,user)
                # generate token for user
                jwt_token = get_jwt_token(user)
                print(jwt_token)
                url = 'mainhome'
                response = redirect(url)
                # Add token in header of url
                response['Token'] = jwt_token
                return response
                

            else:
                return HttpResponse(messages.success(request,"Your account was inactive."))
        else:
            messages.success(request, f'Invalid username or password')
            
            return redirect('login')
    else:
        return render(request, 'user/login.html', {})



def activation_sent_view(request):
    return render(request, 'user/activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        messages.success(request, f'Thank you for your email confirmation.Now you can login your account.')
        return redirect('home')
    else:
    	messages.success(request, f'Activation link is inivalid')
    	return redirect('home')



def base_layout(request):
    template='user/base.html'
    return render(request,template)