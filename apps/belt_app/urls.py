from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.login),
    url(r'^process_login$', views.process_login),
    url(r'^process_registration$', views.process_registration),
    url(r'^quotes$',views.index),
    url(r'^create$',views.create),
    url(r'^edit$', views.edit),
    url(r'^update$',views.update),
    url(r'^user/(?P<user_id>\d+)$',views.show_user),
    url(r'^logout/(?P<user_id>\d+)$',views.logout),
    url(r'^delete/(?P<quote_id>\d+)$',views.delete),
    url(r'^add_like/(?P<quote_id>\d+)$',views.add_like)
]                           

# 1. login page
# 2. process login
# 3. process registration
# 4. Index page
# 5. Edit account page
# 6. Update account process
# 7. Show user quotes
# 8. create quote process
# 9. process logout