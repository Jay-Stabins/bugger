import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse

from bugger.users.forms import UserAdminChangeForm
from bugger.users.models import User
from bugger.users.tests.factories import UserFactory
from bugger.users.views import (
    UserRedirectView,
    UserUpdateImageView,
    UserUpdateView,
    get_profile,
    user_detail_view,
)

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    def dummy_get_response(self, request: HttpRequest):
        return None

    def test_get_success_url(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user

    def test_form_valid(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")

        # Add the session/message middleware to the request
        SessionMiddleware(self.dummy_get_response).process_request(request)
        MessageMiddleware(self.dummy_get_response).process_request(request)
        request.user = user

        view.request = request

        # Initialize the form
        form = UserAdminChangeForm()
        form.cleaned_data = {}
        form.instance = user
        view.form_valid(form)

        assert view.form_valid(form).status_code == 200


class TestUserRedirectView:
    def test_get_redirect_url(self, user: User, rf: RequestFactory):
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserDetailView:
    def test_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory()

        response = user_detail_view(request, username=user.username)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()

        response = user_detail_view(request, username=user.username)
        login_url = reverse(settings.LOGIN_URL)

        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/fake-url/"


"""
    path("get_profile_card/<str:username>", get_profile, name="get-profile-card"),
    path("upload_photo", view=user_update_image_view, name="photo-upload"),
    path("get_profile_photo", get_profile_image, name="get-profile-image"),

"""


class TestUserGetProfile:
    def test_get_profile_card(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = user

        response = get_profile(request, user.username)
        assert response.status_code == 200

    def test_upload_photo(self, user: User, rf: RequestFactory):
        view = UserUpdateImageView()
        request = rf.get("/fake-url/")
        request.user = UserFactory()
        pass

    def test_get_profile_photo(self, user: User, rf: RequestFactory):
        pass
