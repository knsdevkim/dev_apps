from django.shortcuts import render

def dashboard(request):
    context = {}
    context['page_name'] = 'Dashboard'
    return render(request, 'components/dashboard/index.html', context = context)