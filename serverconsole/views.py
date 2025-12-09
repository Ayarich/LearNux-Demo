# serverconsole/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.utils import timezone

from .learning import LINUX_PATH
from .models import TaskProgress, Badge, UserBadge
from .checkers import CHECKERS
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .learning import LINUX_PATH
from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from .models import TaskProgress, UserBadge  # you already created these earlier

@login_required
def linux_leaderboard_view(request):
  User = get_user_model()

  # Aggregate per-user stats
  users = (
      User.objects
      .annotate(
          tasks_completed=Count(
              "taskprogress",
              filter=Q(taskprogress__completed=True),
              distinct=True,
          ),
          badges_count=Count("userbadge", distinct=True),
      )
      .filter(tasks_completed__gt=0)  # only show people who have done *something*
      .order_by("-tasks_completed", "-badges_count", "username")[:50]
  )

  leaderboard = []
  for u in users:
      # simple scoring formula: 10 points per task + 30 per badge
      score = u.tasks_completed * 10 + u.badges_count * 30
      leaderboard.append(
          {
              "user": u,
              "tasks_completed": u.tasks_completed,
              "badges_count": u.badges_count,
              "score": score,
          }
      )

  # sort in Python by score just to be safe
  leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

  context = {
      "path": LINUX_PATH,
      "leaderboard": leaderboard,
  }
  return render(request, "serverconsole/linux_leaderboard.html", context)


def home_view(request):
    return render(request, "serverconsole/home.html")


def staff_check(user):
    return user.is_active and user.is_staff


@login_required
@user_passes_test(staff_check)
def console_view(request):
    # Just render template; WebSocket handles interaction
    return render(request, "serverconsole/console.html")





@login_required
def linux_path_view(request):
    """Show overall Linux learning path with levels & lessons."""
    return render(request, "serverconsole/linux_path.html", {"path": LINUX_PATH})


@login_required
def linux_lesson_view(request, lesson_slug):
    """Show a single lesson with its tasks, next/prev, etc."""
    lesson = None
    level_meta = None

    for level in LINUX_PATH["levels"]:
        for l in level["lessons"]:
            if l["slug"] == lesson_slug:
                lesson = l
                level_meta = {"id": level["id"], "title": level["title"]}
                break
        if lesson:
            break

    if not lesson:
        # simple 404 if slug not found
        raise Http404("Lesson not found")

    context = {
        "path": LINUX_PATH,
        "level": level_meta,
        "lesson": lesson,
    }
    return render(request, "serverconsole/linux_lesson.html", context)



def find_task_by_id(task_id: str):
    """
    Search LINUX_PATH for a task with matching id.
    Returns (lesson_slug, task_dict) or (None, None).
    """
    for level in LINUX_PATH["levels"]:
        for lesson in level["lessons"]:
            for task in lesson.get("tasks", []):
                if task.get("id") == task_id:
                    return lesson["slug"], task
    return None, None



def _award_badges_if_needed(user):
    """
    Very simple badge logic:
    - 'first_task' when user completes 1 task
    - 'ten_tasks' when user completes 10 tasks
    """
    completed_count = TaskProgress.objects.filter(
        user=user, completed=True
    ).count()

    for slug, threshold in [("first_task", 1), ("ten_tasks", 10)]:
        if completed_count >= threshold:
            try:
                badge = Badge.objects.get(slug=slug)
            except Badge.DoesNotExist:
                continue
            UserBadge.objects.get_or_create(user=user, badge=badge)


@login_required
def check_task_view(request, task_id):
    if request.method != "POST":
        return JsonResponse({"ok": False, "error": "POST required"}, status=405)

    lesson_slug, task = find_task_by_id(task_id)
    if not task:
        raise Http404("Task not found")

    check_type = task.get("check_type", "manual")
    params = task.get("check_params", {}) or {}

    # Manual tasks can't be auto-checked – just return info
    if check_type == "manual":
        return JsonResponse({
            "ok": False,
            "manual": True,
            "message": "This is a practice task. There is no auto-check.",
        })

    checker = CHECKERS.get(check_type)
    if not checker:
        return JsonResponse({"ok": False, "error": f"No checker for type {check_type}"}, status=400)

    ok, details = checker(params)

    if ok:
        progress, _ = TaskProgress.objects.get_or_create(
            user=request.user,
            task_id=task_id,
            lesson_slug=lesson_slug,
        )
        if not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
            progress.save()

        _award_badges_if_needed(request.user)

    return JsonResponse({"ok": ok, "details": details})
