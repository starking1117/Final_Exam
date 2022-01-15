from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from borrower.models import borrower
from equipment.models import equipment
from .models import Log

# 借閱記錄列表
class LogList(LoginRequiredMixin, ListView):
    model = Log
    ordering = ['-checkout']
    paginate_by = 20

# 借書階段1：選擇讀者
class CheckoutBorrower(LoginRequiredMixin, ListView):
    model = borrower
    paginate_by = 20
    template_name = 'log/checkout_borrower_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            borrowers = borrower.objects.filter(realname__icontains=query)
        else:
            borrowers = borrower.objects
        return borrowers.order_by('realname')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

# 借書階段2：選擇書籍
class CheckoutEquipment(LoginRequiredMixin, ListView):
    model = equipment
    paginate_by = 5
    template_name = 'log/checkout_equipment_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            equipments = equipment.objects.filter(title__icontains=query)
        else:
            equipments = equipment.objects
        return equipments.exclude(
            log__checkout__isnull=False, 
            log__returned__isnull=True
        ).order_by('title')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        curr_borrower = borrower.objects.get(id=self.kwargs['rid'])
        ctx['query'] = self.request.GET.get('query') or ""
        ctx['borrower'] = curr_borrower
        ctx['borrowing'] = curr_borrower.log_set.filter(
            returned__isnull=True
        ).select_related('equipment')
        return ctx

# 借書階段3：借書登錄
class CheckoutLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        borrowers = borrower.objects.get(id=self.kwargs['rid'])
        equipments = equipment.objects.get(id=self.kwargs['bid'])
        log = Log(borrower=borrower, equipment=equipment)
        log.save()
        return reverse('checkout_equipment', kwargs={'rid': borrower.id})

# 還書階段1：借閱中書籍列表
class ReturnEquipment(LoginRequiredMixin, ListView):
    model = Log
    paginate_by = 20
    template_name = 'log/return_equipment_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            logs = Log.objects.filter(equipment__title__icontains=query)
        else:
            logs = Log.objects
        return logs.exclude(
            returned__isnull=False
        ).select_related('equipment', 'borrower')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

# 還書階段2：還書登記
class ReturnLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        log = Log.objects.get(id=self.kwargs['lid'])
        log.returned = datetime.now()
        log.save()
        return reverse('return_equipment')
