from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
#from django.http import Http404  # for detail function2
from django.shortcuts import get_object_or_404, render

from .models import Question

#That code loads the template called polls/index.html and passes it a context. 
# The context is a dictionary mapping template variable names to Python objects.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

        #Upgraded above to use render-a better shorcut. This is the former version
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

            #Upgraded above to include the template loader. This is the former version
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


        ##The detail function 1
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

#The detail function2: Better version for error handling when requested question doesn't exist
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


#The detail function3 : Rewritten with the get object or raise error 404
#The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments,
# which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

 


    