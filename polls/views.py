from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from polls.models import Question, Choice
from django.contrib.auth import login, logout, authenticate
import datetime
from .forms import OurSignupForm


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    pub_date = datetime.datetime.now()

    context = {
        "latest_questions": latest_questions,
        "pub_date": pub_date
    }
    print(context)
    return render(request, 'polls/index.html', context)
    #pub_date = Question.objects.order_by('-pub_date')[:1][0].pub_date
    #return HttpResponse(output + "<br>" + str(pub_date.strftime("%d.%m.%Y %H:%M")))

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question':question, 'error_mesage': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def signup(request):
    if request.method == 'POST':
        form = OurSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/polls/')
    form = OurSignupForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)