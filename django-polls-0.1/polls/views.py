from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import os
from .models import Question
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# from django.template import loader

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		""" Return the last five published questions."""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'



class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



# Create your views here.

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'polls/index.html', context)

def love(request):
	# for key in request.META:
	# 	print(key, request.META[key])

	# print("Cookies: " + request.META['HTTP_COOKIE'])
	# print("Encodings: " + request.META['HTTP_ACCEPT_ENCODING'])
	# print("HTTP User Agent: " + request.META["HTTP_USER_AGENT"])
	# print(os.path.dirname(os.path.dirname(os.path.abspath("mysite/settings"))))
	return HttpResponse("I love you but I don't want to marry you")

# def detail(request, question_id):
# 	try: 
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not in sooth exist")
# 	# question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form. 
		return render(request, 'polls/detail.html', {
				'question': question,
				'error_message': "You didn't select a choice.",
			})
	else: 
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.


	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))