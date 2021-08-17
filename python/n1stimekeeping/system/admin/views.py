from django.shortcuts import render
from django.db.models import Count
from django.views.generic import (
    TemplateView,
    ListView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import (
    LoginForm,
    GenerateReportForm
)
from core.models import *

# Create your views here.

def generatereport(request):
    context = {}
    
    date_from = request.POST.get('date_range_from', '')
    date_to = request.POST.get('date_range_to', '')
    
    objects = [_ for _ in TimeLogsModel.objects.filter(date__employee__in = request.POST.getlist('employee'), date__date__range = (date_from, date_to)).order_by().select_related('date')]
    
    context['object'] = objects
    context['context_title'] = 'Generate Reports'
    
    return render(request, 'components/panel/generatereport.html', context = context)

class DashboardClassBaseView(LoginRequiredMixin, TemplateView):
    template_name = 'components/panel/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Dashboard'
        return super(DashboardClassBaseView, self).get_context_data(**kwargs)

class PositionsClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/panel/positions.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Available Positions'
        return super(PositionsClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return EmployeeRecordModel.objects.values('employee_position').annotate(num_rows = Count('employee_position')).order_by()

class GetEmployeeClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/panel/viewemployees.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Employee List'
        kwargs['context_form'] = GenerateReportForm
        return super(GetEmployeeClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return EmployeeRecordModel.objects.filter(employee_position = self.kwargs['position'])

class DateClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/panel/datelogs.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Date Logs'
        return super(DateClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return TimeKeepingDateModel.objects.filter(employee = self.kwargs['employee_id'])

class TimeClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/panel/timelogs.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Time Logs'
        return super(TimeClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return TimeLogsModel.objects.filter(date = self.kwargs['date'])


class LoginClassBaseView(LoginView):
    template_name = 'components/login/view.html'
    authentication_form = LoginForm

class LogoutClassBaseView(LogoutView):
    pass