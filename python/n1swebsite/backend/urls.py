from django.urls import path
from .views import *

urlpatterns = [
    path('', RendererDashboardView.as_view(), name='dashboard'),
    path('view/<path:pathfind>/', listView, name='listview'),
    path('set/slideshow', setSlideshow, name='setslideshow'),
    path('set/sitesettings', setSiteSettings, name='setsitesettings'),
    path('create/slideshow/', CreateSlideshow.as_view(), name='createslideshow'),
    path('update/slideshow/<int:pk>/', UpdateSlideshow.as_view(), name='updateslideshow'),
    path('delete/slideshow/<int:pk>/', DeleteSlideshow.as_view(), name='deleteslideshow'),
    path('update/about/<int:pk>/', UpdateAbout.as_view(), name='updateabout'),
    path('create/branch/', CreateBranch.as_view(), name='createbranch'),
    path('details/branch/<int:pk>/', DetailsBranch.as_view(), name='detailsbranch'),
    path('update/brancn/<int:pk>/', UpdateBranch.as_view(), name='updatebranch'),
    path('delete/branch/<int:pk>/', DeleteBranch.as_view(), name='deletebranch'),
    path('create/milestone/', CreateMilestone.as_view(), name='createmilestone'),
    path('details/milestone/<int:pk>/', DetailsMilestone.as_view(), name='detailsmilestone'),
    path('update/milestone/<int:pk>/', UpdateMilestone.as_view(), name='updatemilestone'),
    path('delete/milestone/<int:pk>/', DeleteMilestone.as_view(), name='deletemilestone'),
    path('create/newsevent', CreateNewsEvent.as_view(), name='createnewsevent'),
    path('details/newsevent/<int:pk>/', DetailsNewsEvent.as_view(), name='detailsnewsevent'),
    path('update/newsevent/<int:pk>/', UpdateNewsEvent.as_view(), name='updatenewsevent'),
    path('delete/newsevent/<int:pk>/', DeleteNewsEvent.as_view(), name='deletenewsevent'),
    path('create/video/', CreateVideo.as_view(), name='createvideo'),
    path('update/video/<int:pk>/', UpdateVideo.as_view(), name='updatevideo'),
    path('delete/video/<int:pk>/', DeleteVideo.as_view(), name='deletevideo'),
    path('login/', RendererLoginView.as_view(), name='login'),
    path('changepassword/', RendererChangePasswordView.as_view(), name='changepassword'),
    path('logout/', RendererLogoutView.as_view(), name='logout'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('update/user/', UpdateUserInfo.as_view(), name='updateuser'),
    path('create/careers/', CreateCareers.as_view(), name='createcareers'),
    path('update/careers/<int:pk>/', UpdateCareers.as_view(), name='updatecareers'),
    path('delete/careers/<int:pk>/', DeleteCareers.as_view(), name='deletecareers'),
    path('delete/contactus/<int:pk>/', DeleteContactus.as_view(), name='deletecontactus'),
]

app_name = 'backend'
