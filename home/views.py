from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import views as login_view
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        password = request.POST['password']
        cpassword = request.POST['confirmPassword']
        if password != cpassword:
            return redirect('/')
        user = User.objects.create_user(
            username=username, email=email, password=cpassword, first_name=first_name, last_name=last_name)
        return redirect('/login/')
    return render(request, 'home/register.html')


class LoginUser(login_view.LoginView):
    form_class = LoginForm
    template_name = 'home/login.html'
    redirect_authenticated_user = True


def login(request):
    if request.method == "POST":
        pass
    form = LoginForm()
    return render(request, 'home/login.html', {'form': form})


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'home/index.html')
