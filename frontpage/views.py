from django.shortcuts import render
from forms import AskQuestion, PostAnswer
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Question, Answer

# Create your views here.

def home(request):
	questions = Question.objects.all()
	return render(request, 'frontpage/home.html', {'questions': questions})

def askquestion(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AskQuestion(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save(commit=False)
            post.author = request.user
            post.question_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/question/%s' % post.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AskQuestion()

    return render(request, 'frontpage/createquestion.html', {'form': form})

def postanswer(request, qid):
    question = Question.objects.get(id=qid)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostAnswer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save(commit=False)
            post.author = request.user
            post.answer_date = timezone.now()
            post.question = question
            post.save()
            return HttpResponseRedirect('/question/%s' % qid)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostAnswer()

    return render(request, 'frontpage/postanswer.html', {'form': form, 'question': question})

def question(request, qid):
    question = Question.objects.get(id=qid)
    answers = Answer.objects.filter(question__id=qid)
    return render(request, 'frontpage/question.html', {'question': question, 'answers':answers})