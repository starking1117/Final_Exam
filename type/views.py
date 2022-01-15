from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from log.models import Log


# Create your views here.
class TypeList(LoginRequiredMixin, ListView):   # 圖書列表
    model = type  
    paginate_by = 10

class TypeView(LoginRequiredMixin, DetailView): # 檢視圖書
    model = type

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['log_list'] = Log.objects.filter(
            type=self.object, 
        ).order_by('-id').select_related('borrower')
        return ctx
        
class TypeAdd(LoginRequiredMixin, CreateView):  # 新增圖書
    model = type
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('type_list')

class TypeEdit(LoginRequiredMixin, UpdateView): # 編輯圖書
    model = type
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('type_list')

class TypeDelete(LoginRequiredMixin, DeleteView):   # 刪除圖書
    model = type
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('type_list')