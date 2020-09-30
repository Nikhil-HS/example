from django.shortcuts import render

#######################from Nikhil ########################3

from basic_app.models import Topic,WebPage,AccessRecord
from . import forms
from basic_app.forms import UserForm,UserProfileInfoForm
# Create your views here.

###################imports for login / logout of users #########################
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
################################################################################

def index(nikhil):
    """
    This function is for the practice of html tagging
    """
    my_dict = {'insert_me':"Hello, I am due to HTML Tagging",'number_entry':30}

    return render(nikhil,"basic_app/index.html",context=my_dict)


def myfunc(nikhil):
    #return HttpResponse("<em>Yo Yo, you need to give something meaningfull, after  / </em>") # each views.py file should return an HttpResponse object
    return render(nikhil,"basic_app/landing_page.html")

def MTV(mohini):
    webpg_list = AccessRecord.objects.order_by('date')
    new_dict = {'Date_List':webpg_list}
    return render(mohini,"basic_app/MTV_practice.html",context=new_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])

    return render(request,'basic_app/form_page.html',{'form':form})

#################### This code is for template tagging. Django level 4 #########

def template_tagging(request):
    return render(request, 'basic_app/relative.html')

################################################################################

#################### Django level 5 ###########################################

def register(request):
    registered=False

    if request.method=='POST':
        user_form = UserForm(data = request.POST)
        portfolio_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and portfolio_form.is_valid():
            user = user_form.save() # Here, we write data to .db file
            user.set_password(user.password)
            user.save()

            profile = portfolio_form.save(commit = False) # Here we do not write data to database
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,portfolio_form.errors)
    else:
        user_form = UserForm()
        portfolio_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'registered':registered,'user_form':user_form,'profile_form':portfolio_form})



################################################################################
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login but failed")
            print('Username : {} and Password : {}'.format(username,password) )
            return HttpResponse("Invalid Login Details")
    else:
         return render(request,'basic_app/login.html',{})

@login_required
def user_logout(request):
    """
    logically, the user shall logout only when he/she is logged in
    If we see the code in as stand-alone, we find, there is nothing like a IF loop saying that execute this function only when user is logged in
    These all complex stuff is taken cared by just one decorator written above the def
    """
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def special(request):
    """
    similar as above, this func will require the user logged in to work. This is due to the decorator
    """
    return HttpResponse("Your are logged in")
