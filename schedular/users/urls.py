from django.conf.urls import url
from .views import login, student_details, addstudents, search_student, \
    students, edit_user, addteacher, get_teacher, \
    list_all_students, student_absente, get_absente, add_absente, get_absente_student, send_email
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^student/details$', student_details, name='student_details'),
    url(r'^student/all$', list_all_students, name='list-students'),
    url(r'^student/search$', search_student, name='search_student'),
    url(r'^teacher/add-student$', addstudents, name='addstudents'),
    url(r'^edit-user/(?P<pk>\d+)$', edit_user, name='edit-user'),
    url(r'^teacher/students$', students, name='students'),
    url(r'^teacher/get-all-teacher$', get_teacher, name='get_teacher'),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^teacher/add$', addteacher, name='add-teacher'),
    url(r'^teacher/student-absente/(?P<student_id>\d+)/$', student_absente,
        name="student_absente"),
    url(r'^teacher/get_absente/(?P<student_id>\d+)/$', get_absente,
        name="get_absente"),
    url(r'^teacher/add_absente/(?P<student_id>\d+)/$', add_absente,
        name="add_absente"),
    url(r'^teacher/add_absente_student/(?P<student_id>\d+)/$', get_absente_student,
        name="add_absente_student"),
    url(r'^teacher/send_email/$', send_email, name="send_email"),
]
