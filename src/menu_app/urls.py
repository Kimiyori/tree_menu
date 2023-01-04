from django.urls import path

from menu_app.views import MenuView

urlpatterns = [
    path("", MenuView.as_view(), name="menu_list"),
]
