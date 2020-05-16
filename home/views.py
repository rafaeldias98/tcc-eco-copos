import json
import requests

from .forms import QuestionsForm, RatingForm
from .models import ProductDetail, Questions, Rating
from django.views.generic import CreateView
from django import http
from django.conf import settings
from django.shortcuts import redirect


class CreateProductQuestionView(CreateView):
    model = Questions
    form_class = QuestionsForm
    template_name = 'product_question.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        identifier = self.kwargs.get('identifier')

        question_form = QuestionsForm(request.POST or None)
        if question_form.is_valid() and captcha_is_valid(request):
            question_obj = question_form.save(commit=False)
            related_product = ProductDetail.objects.get(product_id=identifier)
            question_obj.product = related_product
            question_obj.save()

            return http.HttpResponse("Pergunta salva com sucesso!", status=200)
        else:
            error_message = question_form.errors or 'Erro no preenchimento do Captcha'

            return http.HttpResponse(
                "Erro ao salvar pergunta: {}".format(error_message),
                status=500
            )

class CreateProductRatingView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'product_rating.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        identifier = self.kwargs.get('identifier')

        rating_form = RatingForm(request.POST or None)
        if rating_form.is_valid() and captcha_is_valid(request):
            rating_obj = rating_form.save(commit=False)
            related_product = ProductDetail.objects.get(product_id=identifier)
            rating_obj.product = related_product
            rating_obj.save()

            return http.HttpResponse("Avaliação salva com sucesso!", status=200)
        else:
            error_message = rating_form.errors or 'Erro no preenchimento do Captcha'

            return http.HttpResponse(
                "Erro ao salvar avaliação: {}".format(error_message),
                status=500
            )

def captcha_is_valid(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }

    r = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data=data
    )
    result = r.json()

    return result['success']
