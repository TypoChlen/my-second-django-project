from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy



def home(request):
    data = {
        'title': 'Main Page',
        'values': ['idk' '123', 'OoOoOOoOoO'],
        'brands': {
            'nissan': 200.000,
            'mitsubishi': 250.000,
            'ford': 300.000
        }
    }
    return render(request, 'main/home.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def bomb(request):
    return render(request, 'main/bomb.html')

# def profile_view(request):
#     return render(request, '')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        user = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)  # authomatic login after register
        return super().form_valid(form)

# def registration(request):
#     return render(request, 'registration/registration.html')

# def registration(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Войти в систему после регистрации
#             return redirect('profile')  # Перенаправление на страницу профиля
#     else:
#         form = RegistrationForm()
#     return render(request, 'main/registration.html', {'form': form})