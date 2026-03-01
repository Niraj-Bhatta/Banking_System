
from django.contrib import admin
from django.urls import path
from banking import views  # import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),

    # Public pages
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),      # changed from login → user_login
    path('register/', views.register, name='register'),

    # Authenticated pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),

    # Banking operations
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transfer/', views.transfer, name='transfer'),
]


