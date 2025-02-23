from django.urls import path
from .views import test_view, caregiver_view, patient_view, auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", auth_view.login_redirect, name="login_redirect"),
    path("home/", auth_view.index, name="index"),
    path("login/", auth_view.login, name="login"),
    path("logout", auth_view.logout, name="logout"),
    path("callback", auth_view.callback, name="callback"),
    path("patient/", patient_view.render_nodes, name="patient-dashboard"),
    path("caretaker/", caregiver_view.home, name="caretaker-dashboard"),
    path("choose-user-type/", auth_view.choose_user_type, name="choose_user_type"),
    path("patient/<int:node_id>/", patient_view.render_nodes, name="patient-node"),
    path("caretaker/upload/",caregiver_view.upload, name="caretaker-upload"),
    path('caretaker/newCat/', caregiver_view.newCat, name='caretaker-newCat'),
    # path("about/", about_view.home, name="about-page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
