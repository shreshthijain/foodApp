
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Users import views as user_view
from django.contrib.auth import views as login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('Food.urls')), 
    path('user/', include('Users.urls')), 
    path('register/', user_view.register, name='register'),
    path('login/', login_view.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', login_view.LogoutView.as_view(), name='logout'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)