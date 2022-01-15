from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from log.models import Log

# Create your views here.
class BorrowerList(LoginRequiredMixin, ListView):     # 讀者列表
    model = borrower
    ordering = ['realname']     # 依姓名排序
    paginate_by = 20

class BorrowerView(LoginRequiredMixin, DetailView):   # 檢視讀者
    model = borrower

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['log_list'] = Log.objects.filter(
            Borrower=self.object
        ).order_by('-id').select_related('book')
        return ctx
        
class BorrowerAdd(LoginRequiredMixin, CreateView):    # 新增讀者
    model = borrower
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerEdit(LoginRequiredMixin, UpdateView):   # 編輯讀者
    model = borrower
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerDelete(LoginRequiredMixin, DeleteView): # 刪除讀者
    model = borrower
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('borrower_list')
