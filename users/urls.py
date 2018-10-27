from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
# 修改模版路径
LoginView.template_name = 'users/login.html'

urlpatterns = [
	# 登录页面
	# django1.8 以前
	# path('login/', login, {'template_name=':'users/login.html'}, name='login'),
	
	# django2.0 以上
	# 修改方法一
	# path('login/', LoginView.as_view(template_name='users/login.html'), name='login')
	# 修改方法二：修改模版路径 + 以下
	path('login/', LoginView.as_view(), name='login'),

	# logout
	path('logout/', views.logout_view, name='logout'),

	# user register
	path('register/', views.register, name='register'),
]
