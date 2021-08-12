#proj_tdd/urls.py

from django.contrib import admin
#from django.urls import path
from django.conf.urls import  include, url

import firstapp.views

urlpatterns = [
    url(r'^$', firstapp.views.home_page, name='home'),
    # path('admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls))
]
