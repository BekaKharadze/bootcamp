
from django.contrib import admin
from django.urls import path
from django.views import View
from core.views import api_view, home_view, PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_view),
    path('blog/', PostListView.as_view()),
    path('', home_view)
]
