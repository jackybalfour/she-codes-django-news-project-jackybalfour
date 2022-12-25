from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render
from news.models import NewsStory
from django.views.generic.edit import CreateView, FormView, UpdateView
from .forms import CustomUserCreationForm, EditUserProfileForm
from django.views.generic import ListView

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/createAccount.html'


class AccountView(generic.DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context

class EditUserProfileView(UpdateView):
    form_class = EditUserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'registration/editProfile.html'
    
    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:profile', kwargs={"pk":self.request.user.id})

    def get_object(self):
        return self.request.user


class AuthorsView(ListView):
    model = CustomUser
    template_name = 'users/viewAuthors.html'
    # context_object_name = 'author'

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = CustomUser.objects.all()
        return context



# def register(request):
#     data = {
#         'form': CustomUserCreationForm()
#     }
#     return render(request, 'registration/register.html', data)


# def profile(request):
#     return render(request, 'registration/profile.html')