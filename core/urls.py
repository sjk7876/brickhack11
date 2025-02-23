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
    path("caretaker/", caregiver_view.render_individual_item_input_box, name="caretaker-dashboard"),
    path("choose-user-type/", auth_view.choose_user_type, name="choose_user_type"),
    path("patient/<int:node_id>/", patient_view.render_nodes, name="patient-node"),
    path("caretaker/uploaditem/upload/",caregiver_view.upload, name="caretaker-upload"),
    path('caretaker/newCat/', caregiver_view.newCat, name='caretaker-newCat'),
    path('caretaker/uploaditem/', caregiver_view.render_individual_item_input_box, name='caretaker-upload-item'),
    path("caretaker/uploadwordlist/", caregiver_view.render_word_list_input_box, name="caretaker-word-list"),
    path("caretaker/uploadwordlist/upload/", caregiver_view.generate_objects_from_word_list, name="caretaker-upload-word-list"),
    path("caretaker/uploaditem/generateimage", caregiver_view.generate_single_image, name="caretaker-generate-single-image"),
    path('caretaker/generate/', caregiver_view.render_Generate, name='caretakerGenerate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
