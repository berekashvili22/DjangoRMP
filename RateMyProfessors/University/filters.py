import django_filters
from . models import UniReview, University
from django_filters import CharFilter, ChoiceFilter


STAR_CHOICES = (
    (1, 'One Star'),
    (2, 'Two Star'),    
    (3, 'Three Star'),    
    (4, 'Four Star'),    
    (5, 'Five Star')    
)

class UniReviewFilter(django_filters.FilterSet):
         text = CharFilter(field_name='text', lookup_expr='icontains')
         score = ChoiceFilter(choices=STAR_CHOICES)
         class Meta:
                  model = UniReview
                  fields = '__all__'
                  exclude = ['text', 'score']