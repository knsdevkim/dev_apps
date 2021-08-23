from django.urls import path

from .views import *

app_name = 'apps'

urlpatterns = [
    path('', LoginViewTemplate.as_view(), name = 'login'),
    path('logout/', LogoutViewTemplate.as_view(), name = 'logout'),
    path('admin/', dashboard, name = 'dashboard'),

    # CREATE URL's
    path('admin/create/newsevents/', NewsEventsCreateView.as_view(), name = 'createnewsevents'),
    path('admin/create/department/', DepartmentCreateView.as_view(), name = 'createdepartment'),
    path('admin/create/jobposition/<int:department_id>/', JobPositionCreateView.as_view(), name = 'createjobposition'),
    path('admin/create/jobqualification/<int:jobposition_id>/', JobQualificationCreateView.as_view(), name = 'createjobqualification'),
    path('admin/upload/media/<slug:slug>/<str:token>/', MediaUploadCreateView.as_view(), name = 'uploadcontentmedia'),

    #UPDATE URL's
    path('admin/update/newsevents/<int:pk>/', NewsEventsUpdateView.as_view(), name = 'updatenewsevents'),
    path('admin/update/department/<int:pk>/', DepartmentUpdateView.as_view(), name = 'updatedepartment'),
    path('update/visibility/<slug:slug>/<int:parent_id>/<str:visibility>/<int:pk>/', update_job_visibilty, name = 'updatejobvisibility'),

    # DELETE URL's
    path('admin/delete/newsevents/<int:pk>/', NewsEventsDeleteView.as_view(), name = 'deletenewsevents'),
    path('admin/delete/department/<int:pk>/', DepartmentDeleteView.as_view(), name = 'deletedepartment'),
    path('admin/delete/jobposition/<int:pk>/', JobPositionDeleteView.as_view(), name = 'deletejobposition'),
    path('admin/delete/jobqualification/<int:pk>/', JobQualificationDeleteView.as_view(), name = 'deletejobqualification'),
    path('admin/delete/media/<int:pk>/', MediaDeleteView.as_view(), name = 'deletemedia'),

    # LIST URL's
    path('admin/list/<slug:slug>/', ListViewModule.as_view(), name = 'listviewmodule'),
    path('admin/analytic/<slug:slug>/', WebAnalyticViewModule.as_view(), name = 'analyticviewmodule'),
    path('admin/view/<slug:slug>/', DepartmentListView.as_view(), name = 'departmentlistview'),
    path('admin/webform/applicant/', ApplicationListView.as_view(), name = 'applicationlistview'),
    path('admin/webform/contactus/', ContactListView.as_view(), name = 'contactlistview'),
    path('admin/view/<slug:slug>/<int:id>/', JobPositionListView.as_view(), name = 'jobpositionlistview'),
    path('admin/view/q/<slug:slug>/<int:id>/', JobQualificationListView.as_view(), name = 'jobqualificationlistview'),
    path('admin/view/media/<slug:slug>/<int:token_id>/<str:token>/', MediaListView.as_view(), name = 'medialistview'),
]