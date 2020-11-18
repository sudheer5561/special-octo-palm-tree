from django.urls import path

from . import views

urlpatterns = [
    path('<link_name>', views.redirect_view, name='redirect'),
]
