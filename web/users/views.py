from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from users.models import Profile, Test
from . forms import CustomUserCreationForm, ProfileForm, TestForm





def userLogin(request):
    if request.user.is_authenticated: 
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)  
        except:
            messages.error(request, "username doesnt exixt!")
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "username or password is not correct")

    return render(request, 'users/login.html')



def userRegister(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            profile = Profile.objects.create(user=user).save()


            messages.success(request, 'User accout is created!')
            
            authenticated_user = authenticate(username=user.username,
                                      password=form.cleaned_data['password1'])

            login(request, authenticated_user)

            return redirect('profile')
        else:
            messages.error(request, "An error occured during registration")

    context = {'page':page, 'form':form}
    return render(request, 'users/register.html', context)



   
@login_required(login_url='/')
def userTest(request):
    form = TestForm()
    if request.method =='POST':
        print( request.FILES)
        form = TestForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            print('valid form')
            profile = Profile.objects.filter(user = request.user).first()
            test = form.save(commit=False)
            test.profile = profile
            test.save()
            messages.success(request, 'Test submitted')
            return redirect('tests')
        else:
            print('invalid form')
            messages.error(request, "An error occured during test")

    context = {'active':'newtest', 'form': form}
    return render(request, 'users/newtest.html', context)


   
@login_required(login_url='/')
def userProfile(request):
    profile = Profile.objects.filter(user = request.user).first()
    print(profile)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form':form, 'active':'profile'}
    return render(request, 'users/profile.html',context)



def logoutUser(request):
    logout(request)
    return redirect('/')





@login_required(login_url='/')
def userHome(request):
    # homepage = HomePage.objects.filter().first()
    # products = homepage.products.all()
    # cities = City.objects.all()
    # categories = Category.objects.all() 
    context = {'active':'home'} #,'products':products,'cities':cities,'categories':categories}
    return render(request, 'users/home.html',context=context)


@login_required(login_url='/')
def userTests(request):
    profile = Profile.objects.filter(user = request.user).first()

    print(profile)
    tests = Test.objects.filter(profile=profile).all()

    context = {'active':'tests', 'tests': tests}
    return render(request, 'users/tests.html',context=context)