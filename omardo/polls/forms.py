from django.forms import ModelForm
from omardo.polls.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ("question_text",)
