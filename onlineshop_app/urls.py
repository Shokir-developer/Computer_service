from django.urls import path
from .views import contact_us, buy, about, signUp, loginPage, logOutPage

urlpatterns = [
    path('', contact_us, name='home'),
    path('buy/', buy, name='buy'),
    path('about/', about, name='about'),
    path('register/', signUp, name='sign_up'),
    path('login/', loginPage, name='login'),
    path('logOut/', logOutPage, name='log_out'),
]