from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from log.models import Log

# Create your views here.
class EquipmentList(LoginRequiredMixin, ListView):   # 圖書列表
    model = equipment   
    paginate_by = 10

class EquipmentView(LoginRequiredMixin, DetailView): # 檢視圖書
    model = equipment

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['log_list'] = Log.objects.filter(
            equipment=self.object, 
        ).order_by('-id').select_related('borrower')
        return ctx
        
class EquipmentAdd(LoginRequiredMixin, CreateView):  # 新增圖書
    model = equipment
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('equipment_list')

class EquipmentEdit(LoginRequiredMixin, UpdateView): # 編輯圖書
    model = equipment
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('equipment_list')

class EquipmentDelete(LoginRequiredMixin, DeleteView):   # 刪除圖書
    model = equipment
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('equipment_list')