from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<int:team_id>', views.dashboard_id, name='dashboard_id'),
    path('progress/', views.progress, name='progress'),
    path('progress/<int:team_id>', views.progress_id, name='progress_id'),
    path('report/', views.report, name='report'),
    path('report/<int:team_id>', views.report_id, name='report_id'),
    path('send/<int:team_id>', views.send_report, name='send_report')

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]