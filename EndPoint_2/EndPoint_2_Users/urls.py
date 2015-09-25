from django.conf.urls import url
from views import searchuserbyprofession, listallusers


urlpatterns = [
    url(r'allusers', listallusers, name='ListAllUser'),
    url(r'(?P<filter_factor>[\w \s]+)/(?P<filter_criteria>[\w \s]+)/(?P<group_criteria>[\w \s]+)$', searchuserbyprofession, name='SearchUser'),
]
