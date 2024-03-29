from django.urls import path

from bugger.users.views import (
    get_profile,
    get_profile_image,
    user_detail_view,
    user_redirect_view,
    user_update_image_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("get_profile_card/<str:username>", get_profile, name="get-profile-card"),
    path("upload_photo", view=user_update_image_view, name="photo-upload"),
    path("get_profile_photo", get_profile_image, name="get-profile-image"),
]
