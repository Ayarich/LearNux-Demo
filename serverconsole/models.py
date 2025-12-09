# serverconsole/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone


class TaskProgress(models.Model):
    """
    Progress for a single hard-coded task in the LINUX_PATH tree.
    task_id is the string like 'l2_t2'.
    lesson_slug is the code slug, e.g. 'listing-files' (useful for querying).
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=32)
    lesson_slug = models.CharField(max_length=64)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "task_id")

    def __str__(self):
        return f"{self.user} - {self.task_id} ({'done' if self.completed else 'pending'})"


class Badge(models.Model):
    """
    Simple achievements – you can hard-code logic & reference by slug.
    """
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # e.g. "tasks_completed", "first_lesson_done", etc.
    rule_type = models.CharField(max_length=50, default="tasks_completed")
    rule_value = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("user", "badge")

    def __str__(self):
        return f"{self.user} → {self.badge.name}"


class Challenge(models.Model):
    """
    Time-limited training missions ("Finish Level 1 in 20 minutes").
    """
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    # in minutes
    duration_minutes = models.PositiveIntegerField(default=15)
    # which lesson slugs or task ids this challenge cares about
    target_lesson_slug = models.CharField(max_length=64, blank=True)
    target_task_ids = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title


class UserChallengeSession(models.Model):
    """
    A running/finished challenge for a user.
    """
    STATUS_CHOICES = [
        ("running", "Running"),
        ("success", "Success"),
        ("failed", "Failed"),
        ("expired", "Expired"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    started_at = models.DateTimeField(default=timezone.now)
    finished_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="running")

    class Meta:
        unique_together = ("user", "challenge", "started_at")


class SandboxInstance(models.Model):
    """
    Link a learner to their sandbox container (for multi-tenant future).
    For now you can just store a name; later you can integrate with Docker / Kubernetes.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    container_name = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} → {self.container_name}"
