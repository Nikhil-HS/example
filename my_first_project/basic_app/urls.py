from django.conf.urls import url
from basic_app import views
from django.urls import path

#template_tagging
app_name = "basic_app"

urlpatterns = [
url(r'^$',views.myfunc,name='myfunc'),
url(r'^data_record',views.MTV,name='MTV'),
url(r'^formpage',views.form_name_view,name='form_name'),
url(r'^template_tagging',views.template_tagging,name='template_tagging'),
url(r'^register',views.register,name='register'),
url(r'^user_login/$',views.user_login,name='user_login')
]
