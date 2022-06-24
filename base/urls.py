from unicodedata import name
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
# from django.conf.urls import url
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact-me/', views.ContactMe, name="contact-me"),
    path('thank-you/', views.thankYou, name="thank-you"),
    path('services/', views.services, name="services"),
    path('project-archive/', views.ProjectArchiveView, name='project-archive'),
    path('project/<slug:slug>', views.ProjectView, name='project'),
    re_path('^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),