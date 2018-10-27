"""定义learning_logs的URL模式"""

from django.urls import path,re_path
from . import views

app_name='learning_logs'
urlpatterns = [
	#主页
	path('',views.index, name='index'),
	#显示所有主题页面
	path('topics/',views.topics, name='topics'),
	#显示特定的主题详细页面
	path('topic/<int:topic_id>/',views.topic,name='topic'),
	#用于添加新主题的网页
	path('new_topic/',views.new_topic, name='new_topic'),
	#用于添加新条目的页面
	path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
	#用于修改条目的页面
	path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),


]
