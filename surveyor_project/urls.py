from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
    # for image upload
from django.conf.urls.static import static
    # for image upload


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/
    # this will need to be reconfigured for deployment