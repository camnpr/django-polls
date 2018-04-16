from django.urls import path

from . import views

# by https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial05/   test TestCase flag
# by https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial06/		引入资源static
# by https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial07/   修改后台模板，增加功能
# by https://docs.djangoproject.com/zh-hans/2.0/intro/reusable-apps/ 进阶指南：如何编写可重用程序

app_name = 'polls'

urlpatterns = [
	# ex: /polls/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
]