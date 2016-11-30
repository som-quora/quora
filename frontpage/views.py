from django.shortcuts import render
from forms import AskQuestion, PostAnswer
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'frontpage/home.html', {})

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
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AskQuestion()

    return render(request, 'frontpage/createquestion.html', {'form': form})
