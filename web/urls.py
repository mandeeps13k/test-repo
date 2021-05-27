from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^$', views.index,name = "index"),
    url(r'^login$', views.login,name = "login"),
    url(r'^logout$', views.logout,name = "logout"),
    url(r'^page$', views.page,name = "page"),
    url(r'^googleID$', views.googleID,name = "googleID"),


    #url(r'^securityStatus_html$', views.securityStatus_html,name = "securityStatus_html"),
    #url(r'^sendEmail$', views.sendEmail,name = "sendEmail"),

    #url(r'^jiraMetricsFCG$', views.jiraMetricsFCG,name = "jiraMetricsFCG"),



]
