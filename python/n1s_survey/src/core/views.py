from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


from core.decorators import authenticated
from core.forms import *
from core.models import *
# Create your views here.

@login_required
def dashboard(request):
    context = {}
    context['context_title'] = "Dashboard"
    return render(request, 'components/dashboard/index.html', context = context)


@method_decorator(authenticated, name = 'dispatch')
class Login(LoginView):
    template_name       = 'root/login.html'
    authentication_form = LoginForm


class Logout(LogoutView):
    pass


class EvaluationList(LoginRequiredMixin, ListView):
    template_name       = 'components/read/index.html'
    context_object_name = 'dataObject'

    def get_context_data(self, **kwargs):
        kwargs['context_title']       = 'evaluation list'
        kwargs['context_panel_title'] = 'coaching data entry'
        return super(EvaluationList, self).get_context_data(**kwargs)

    def get_queryset(self):
        return Evaluation.objects.all()


class EvaluatedDetails(DetailView):
    template_name       = 'components/details/evaluation/index.html'
    context_object_name = 'dataObject'

    def get_queryset(self):
        return Evaluation.objects.filter(pk = self.kwargs[self.pk_url_kwarg])


class TrainingmemoList(LoginRequiredMixin, ListView):
    template_name       = 'components/read/index.html'
    context_object_name = 'dataObject'

    def get_context_data(self, **kwargs):
        kwargs['context_title']       = 'training memo list'
        kwargs['context_panel_title'] = 'training memo data entry'
        return super(TrainingmemoList, self).get_context_data(**kwargs)

    def get_queryset(self):
        return TrainingMemo.objects.all()


class TrainingmemoDetails(DetailView):
    template_name       = 'components/details/trainingmemo/index.html'
    context_object_name = 'dataObject'

    def get_queryset(self):
        return TrainingMemo.objects.filter(pk = self.kwargs[self.pk_url_kwarg])
