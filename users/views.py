
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm

def register(request):
    '''
    This function handles user registration.

    It displays the UserRegisterForm from the users/forms.py file.

    It also validates user input and creates an account for the user if their input is valid.
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form': form })

def profile(request):
    return render(request, 'users/profile.html')
