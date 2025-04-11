from django.urls import path
from . import views


urlpatterns = [
    path("students/", views.studentsView),
    path("student/<int:pk>/", views.studentDetailsView),
    path("employee/", views.EmployeeView.as_view()),
    # path("employee/<int:pk>/", views.EmployeeDetailView)

]