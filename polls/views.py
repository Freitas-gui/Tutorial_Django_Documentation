from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={
        'latest_question_list' : latest_question_list
    }
    return render(request,'polls/index.html', context)

def detaill(request, question_id):
    question = get_object_or_404(Question , pk=question_id)
    return render(request, 'polls/detaill.html', {'question' : question})

def detail(request, question_id):
    this_question = Question.objects.filter(pk__in=[question_id])
    context ={
        'this_question' : this_question
    }
    return render(request,'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're votting on question %s."%question_id)


# Create your views here.
