from .forms import QuestionsForm, RatingForm
from .models import ProductDetail, Questions, Rating
from django.views.generic import CreateView
from django import http


class CreateProductQuestionView(CreateView):
    model = Questions
    form_class = QuestionsForm
    template_name = 'product_question.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        identifier = self.kwargs.get('identifier')

        question_form = QuestionsForm(request.POST or None)
        if question_form.is_valid():
            question_obj = question_form.save(commit=False)
            related_product = ProductDetail.objects.get(product_id=identifier)
            question_obj.product = related_product
            question_obj.save()

            return http.HttpResponse("Pergunta salva com sucesso!", status=200)
        else:
            return http.HttpResponse(
                "Erro ao salvar pergunta: {}".format(question_form.errors),
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
        if rating_form.is_valid():
            rating_obj = rating_form.save(commit=False)
            related_product = ProductDetail.objects.get(product_id=identifier)
            rating_obj.product = related_product
            rating_obj.save()

            return http.HttpResponse("Avaliação salva com sucesso!", status=200)
        else:
            return http.HttpResponse(
                "Erro ao salvar avaliação: {}".format(rating_form.errors),
                status=500
            )
