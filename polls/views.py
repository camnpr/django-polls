from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import loader
from django.shortcuts import render #, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from django.views import generic   # 通用视图

from django.db.models import F
from .models import Question, Choice


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""返回最近发布的5个问题"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

#...主页
"""def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = '<br /> '.join([q.question_text for q in latest_question_list])
	
	# template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list
	}
	# HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)
"""

class DetailView(generic.DetailView):
		model = Question
		template_name='polls/detail.html' # 默认情况下，通用视图 DetailView 使用一个叫做 <app name>/<model name>_detail.html 的模板。在我们的例子中，它将使用 "polls/question_detail.html" 模板
		def get_queryset(self):
			# 发布时间未到，不展示任何问题详情。如果没有，返回： 没有找到符合查询的 question
			return Question.objects.filter(pub_date__lte=timezone.now())

#...详情页
"""def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("未找到！o(╯□╰)o")
	return render(request, 'polls/detail.html', {'question': question})
"""


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	def get_queryset(self):
		# 发布时间未到，不展示任何问题详情。如果没有，返回： 没有找到符合查询的 question
		return Question.objects.filter(pub_date__lte=timezone.now())

#...投票结果页
"""def results(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("未找到！o(╯□╰)o")
	
	return render(request, 'polls/results.html', {'question': question})
"""


#...处理投票表单
def vote(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("未找到！o(╯□╰)o")
	
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# 有错误就返回到上一页
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "请选择一个选项",
		})
	else:
		selected_choice.votes = F('votes') + 1 # F 防止竞争条件，多个同事投票，解决：下边的save丢失的问题。
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))