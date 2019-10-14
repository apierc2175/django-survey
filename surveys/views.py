from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.forms.formsets import formset_factory

from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm

class IndexView(generic.ListView):
    template_name = 'surveys/index.html'
    model = Question
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'surveys/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'surveys/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes = selected_choice.votes + 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('surveys:results', args=(question.id,)))

class CreateView(generic.CreateView):
    model = Question
    fields = ['question_text',]
    template_name = 'surveys/create.html'

def add_survey(request):
    ChoiceFormSet = formset_factory(ChoiceForm, extra=0, min_num=2)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST)

        if all([form.is_valid(), formset.is_valid()]):
            form.instance.created_by = request.user
            question = form.save()

            for inline_form in formset:
                if inline_form.cleaned_data:
                    choice = inline_form.save(commit=False)
                    choice.question = question
                    choice.save()
            return HttpResponseRedirect(reverse('surveys:index',))
    else:
        form = QuestionForm()
        formset = ChoiceFormSet()

    return render(request, 'surveys/create.html', {'form': form, 'formset': formset,})
