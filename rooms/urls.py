from django.urls import path
from rooms import views as room_views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", room_views.RoomDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", room_views.EditRoomView.as_view(), name="edit"),
    path("create/", room_views.CreateRoomView.as_view(), name="create"),
    path("<int:pk>/photos/", room_views.RoomPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add", room_views.AddPhotoView.as_view(), name="add_photo"),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/delete/",
        room_views.delete_photo,
        name="delete_photo",
    ),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/edit/",
        room_views.EditPhotoView.as_view(),
        name="edit_photo",
    ),
    path("search/", room_views.SearchView.as_view(), name="search"),
]
