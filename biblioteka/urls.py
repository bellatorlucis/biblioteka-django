"""biblioteka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from biblioteka import settings

from biblioteka import views as biblioteka_views

urlpatterns = [
    url(r'^$', biblioteka_views.BibliotekaHome.as_view(), name='biblioteka-index'),
    url(r'^admin/', admin.site.urls, name='adminHome'),
    url(r'^login/', biblioteka_views.LoginView.as_view(), name="login"),
    url(r'^login-success/', biblioteka_views.login_success, name='login-success'),
    url(r'^logout/', biblioteka_views.LogOutView.as_view(), name="logout"),
    url(r'^korisnik/', include('korisnik.urls'),name='korisnik'),
    url(r'^sluzbenik/', include('sluzbenik.urls'),name='sluzbenik'),
    url(r'^registration/',biblioteka_views.SignUpView.as_view(), name='registration'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
