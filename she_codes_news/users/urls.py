from django.urls import path
from .views import CreateAccountView, AccountView, EditUserProfileView, AuthorsView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', AccountView.as_view(), name='profile'),
    path('view-authors', AuthorsView.as_view(), name='authors'),
    path('edit-profile/', EditUserProfileView.as_view(), name='editProfile'),

]