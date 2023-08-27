"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('remove-book', views.delete_bookByAdmin, name='remove-book-admin'),
    path('book/<int:pk>/', views.edit_book, name='edit-book'),
    path('remove-student', views.delete_studentByAdmin, name='remove-student-admin'),
    path('student/<int:pk>/', views.edit_student, name='edit-student'),
    path('viewbook_by_student', views.viewbook_viewbyStudent),
    path('borrow-book', views.request_borrow_book, name='borrow-book'),
    path('viewpendingbooks/', views.pending_book_requests, name='viewpendingbooks'),
    path('approve-issue-book/', views.approve_issue_book, name='approve-issue-book'),
    path('declineissuebook', views.decline_issue_book, name='decline-issue-book'),
    path('returnbook', views.request_return_book, name='returnbook'),
]
