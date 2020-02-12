from django.forms import ModelForm
from .models import Questions, Rating

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['posted_by', 'user_question', 'user_email']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['posted_by', 'user_rating', 'user_email', 'user_comment']
