from django.urls import path
from .views import console_view, linux_path_view, linux_lesson_view, check_task_view, linux_leaderboard_view

app_name = "serverconsole"


urlpatterns = [
    path("", console_view, name="console"),
    path("linux-path/", linux_path_view, name="linux-path"),
    path("linux-lesson/<slug:lesson_slug>/", linux_lesson_view, name="linux-lesson"),
    path("api/check-task/<str:task_id>/", check_task_view, name="check-task"),
    path("linux-leaderboard/", linux_leaderboard_view, name="linux-leaderboard"),
]
