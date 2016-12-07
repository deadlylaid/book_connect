"""wef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from wef.views import *
from users.views import *
from items.views import *
from items.api.views import *
from users.api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', Home.as_view(), name='home'),

    url(r'^joinus/$', join_us, name='join_us'),
    url(r'^login/$', LogInView.as_view(), name='log_in'),
    url(r'^logout/$', LogOutView.as_view(), name='log_out'),
    url(r'^mypage/$', MyPage.as_view(), name='my_page'),

    url(r'^lists/$', PostList.as_view(), name='postlist'),
    url(r'^search/$', SearchView.as_view(), name='postsearch'),

    url(r'^booksale/$', BookSale.as_view(), name='booksale'),
    url(r'^booksale/(?P<pk>\d+)/$', PostDetail.as_view(), name='postdetail'),
    url(r'^booksale/(?P<pk>\d+)/delete$', PostDelete.as_view(), name='postdelete'),

    url(r'^api/username/check/$', CheckOverlapUsername.as_view(), name='checkusername'),
    url(r'^api/token/check/$', CheckToken.as_view(), name='checktoken'),
    url(r'^api/phonenumber/sms/check/$', PhoneNumberCheck.as_view(), name='sendsms'),

    url(r'^api/sendbuysms/$', SendBuySMSAPIView.as_view(), name='sendsms'),
    url(r'^api/(?P<pk>\d+)/soldout/$', BookListAPIView.as_view(), name='booklistapi'),

    url(r'^aftersocial/$', AfterSocial.as_view(), name='aftersocial'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
