from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs["content_page"] = "polls/list.html"
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs["content_page"] = "polls/detail.html"
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs["content_page"] = "polls/results.html"
        return super().get_context_data(**kwargs)


def add(request: HttpRequest):
    content = "polls/notyet.html" if request.method == "POST" else "polls/add.html"

    return render(
        request,
        "polls/index.html",
        {
            "content_page": content,
        },
    )


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/index.html",
            {
                "content_page": "polls/detail.html",
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
