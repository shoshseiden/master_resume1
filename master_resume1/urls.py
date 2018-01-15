from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from . import views


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", views.SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", views.LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),
    url(r"^(?P<profile_id>[0-9]+)/customize/", views.custom, name="custom"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
