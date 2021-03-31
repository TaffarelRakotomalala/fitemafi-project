import django_filters

from blog.models import *


class DroitFilter(django_filters.FilterSet):
    class Meta:
        model = Droit
        fields = '__all__'
        exclude = ['id_droit','id_membres']