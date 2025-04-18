from django.views.generic import TemplateView

from . import models


class Index(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'shop': models.Shop.objects.first(),
            'items': models.MenuItem.objects.all()
        })
        return context
