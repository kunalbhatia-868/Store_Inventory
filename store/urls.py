from django.urls import path
from .views import (
CreateBoxView,
UpdateBoxView,
AllBoxView,
UserBoxView,
BoxDeleteView
)

urlpatterns = [
    path('get_box',AllBoxView.as_view(),name="get_box"),
    path('get_user_box',UserBoxView.as_view(),name="get_box"),
    path('add_box',CreateBoxView.as_view(),name="create_box"),
    path('update_box/<int:pk>',UpdateBoxView.as_view(),name="update_box"),
    path('delete_box/<int:pk>',BoxDeleteView.as_view(),name="delete_box"),
]
