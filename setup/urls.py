from django.contrib import admin
from django.urls import path

from tasks.views import TodoListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view()),
]
