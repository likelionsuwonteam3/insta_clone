from django.contrib import admin
from django.urls import path
import main.views
import accounts.views

#media, static 설정
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('new/', main.views.new, name='new'),
    path('create/', main.views.create, name='create'),
    path('like/<int:post_id>', main.views.like, name='like'),
    path('comment/<int:post_id>', main.views.comment, name='comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#media 설정
