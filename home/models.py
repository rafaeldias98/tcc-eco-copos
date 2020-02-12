from django.db import models
from django.template.defaulttags import register
from django.conf import settings

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


class ProductList(Page):
    def get_context(self, request):
        context = super().get_context(request)

        context['products'] = ProductDetail.objects.child_of(self).live()

        category_infos = {}
        filter_key = 1
        for product in context['products']:
            if product.category not in category_infos:
                category_infos.update(
                    {
                        product.category: {
                            'count': 1,
                            'filter_key': filter_key
                        }
                    }
                )

                filter_key += 1
            else:
                category_infos[product.category]['count'] += 1

        context['category_infos'] = category_infos
        context['category_count'] = sum(value.get('count') for _, value in category_infos.items())

        return context

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)


class ProductDetail(Page):
    product_id = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('product_id'),
        FieldPanel('category'),
        FieldPanel('price'),
        ImageChooserPanel('image'),
        FieldPanel('short_description'),
        InlinePanel('custom_fields', label='Custom fields'),
        InlinePanel('questions', label='Questions'),
        InlinePanel('ratings', label='Ratings'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        fields = []
        for field_obj in self.custom_fields.get_object_list():
            if field_obj.options:
                field_obj.options_array = field_obj.options.split('|')
                fields.append(field_obj)
            else:
                fields.append(field_obj)

        context['custom_fields'] = fields

        context['questions'] = self.questions.get_object_list()

        context['ratings'] = self.ratings.get_object_list()

        return context

    @register.filter
    def make_range(number):
        return range(number)


class ProductCustomField(Orderable):
    product = ParentalKey(ProductDetail, on_delete=models.CASCADE, related_name='custom_fields')
    name = models.CharField(max_length=255)
    options = models.CharField(max_length=500)

    panels = [
        FieldPanel('name'),
        FieldPanel('options')
    ]


class Questions(Orderable):
    product = ParentalKey(ProductDetail, on_delete=models.CASCADE, related_name='questions')
    posted_by = models.CharField(max_length=255)
    user_question = models.TextField()
    user_email = models.EmailField()
    site_response = models.TextField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Rating(Orderable):
    product = ParentalKey(ProductDetail, on_delete=models.CASCADE, related_name='ratings')
    posted_by = models.CharField(max_length=255)
    user_rating = models.IntegerField()
    user_comment = models.TextField()
    user_email = models.EmailField(unique=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


@register_setting
class SnipcartSettings(BaseSetting):
    api_key = models.CharField(
        max_length=255,
        help_text='Your Snipcart public API key'
    )
