from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    ROLE_CHOICES = [
        ("ADMIN", "Administrator"),
        ("POLICE", "Police Authority"),
        ("SACHIVALAYAM", "Sachivalayam Employee"),
        ("CITIZEN", "Citizen"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    area = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class MissingChild(models.Model):

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]

    STATUS_CHOICES = [
        ("REPORTED", "Reported"),
        ("UNDER_REVIEW", "Under Review"),
        ("ACTIVE", "Active"),
        ("RESOLVED", "Resolved"),
    ]

    case_number = models.CharField(
        max_length=20,
        unique=True
    )

    child_name = models.CharField(
        max_length=100
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    # Child photo
    photo = models.ImageField(
        upload_to="missing_children/",
        blank=True,
        null=True
    )

    date_last_seen = models.DateField()

    location_last_seen = models.CharField(
        max_length=200
    )

    description = models.TextField()

    guardian_name = models.CharField(
        max_length=100
    )

    guardian_contact = models.CharField(
        max_length=15
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="REPORTED"
    )

    reported_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.case_number} - {self.child_name}"


class Alert(models.Model):

    ALERT_TYPES = [
        ("MISSING_CHILD", "Missing Child Alert"),
        ("STATUS_UPDATE", "Case Status Update"),
    ]

    case = models.ForeignKey(
        MissingChild,
        on_delete=models.CASCADE
    )

    alert_type = models.CharField(
        max_length=30,
        choices=ALERT_TYPES
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.alert_type} - {self.case.case_number}"