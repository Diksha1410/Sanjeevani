
from django.urls import path,include
from.import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index-1',views.index,name='index-1'),

    path('',views.login,name='login'),

    #==============================REGISTRATION===================================================
    path('doctor-register',views.docregister,name='doctor-register'),                                 # Doctor Registration Page
    path('register',views.register,name='register'),                                                  # Patient Registration Page
    #=============================================================================================
    
    #==================================Doctor Page Urls=============================================
    path('doctors',views.doctor,name='doctors'),
    path('doctor-dashboard',views.doctordashboard,name='doctor-dashboard'),
    path('appointments',views.appointments,name='appointments'),
    path('patients-list',views.patients,name='patients-list'),
    path('schedule-timings',views.schedule,name='schedule-timings'),
    path('patient-profile',views.patientpro,name='patient-profile'),
    path('doctor-profile-settings',views.docprofilesettings,name='doctor-profile-settings'),
    path('doctor-update-profile',views.doctorupdateprofile,name='doctor-update-profile'),
    path('reviews',views.reviews,name='reviews'),
    #===============================================================================================

    #==============================Patient Page Urls=================================================
    path('patients',views.pat,name='patients'),
    path('search',views.search,name='search'),
    path('doctor-profile',views.doctorprofile,name='doctor-profile'),
    path('patient-dashboard',views.patientdashboard,name='patient-dashboard'),
    path('booking-success',views.bookingsuccess,name='booking-success'),
    path('patient-profile-settings',views.patprosettings,name='patient-profile-settings'),
    path('patient-update-profile',views.patupdateprofile,name='patient-update-profile'),

    #=======================================Change Password==================================================
    path('doctor-change-password',views.docchangepass,name='doctor-change-password'),
    path('patient-change-password',views.patchangepass,name='patient-change-password'),
    
    #========================================ABOUT PAGE ===========================================================

    path('forgot-password',views.forgotpass,name='forgot-password'),
    path('logout',views.logout,name='logout'), 
    path('about',views.about,name='about'), 


    path('admin',views.admin,name='admin'),

    
    #(===================================== "Forget Password" =======================================)
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

### ath('page',views.function,name=page)