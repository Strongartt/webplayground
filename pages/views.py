from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page
    
class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')
    
class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy ('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")