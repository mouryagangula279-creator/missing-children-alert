"""
URL configuration for safetrace project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts import views


urlpatterns = [

    # Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Home
    path(
        "",
        views.home,
        name="home"
    ),

    # Authentication
    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    # Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    # Register Missing Child
    path(
        "register-missing-child/",
        views.register_missing_child,
        name="register_missing_child"
    ),

    # Missing Cases
    path(
        "missing-cases/",
        views.missing_cases,
        name="missing_cases"
    ),

    # Case Details
    path(
        "case/<int:case_id>/",
        views.case_detail,
        name="case_detail"
    ),

    # Update Case Status
    path(
        "case/<int:case_id>/update-status/",
        views.update_case_status,
        name="update_case_status"
    ),

    # Alerts
    path(
        "alerts/",
        views.alerts,
        name="alerts"
    ),

    # Mark Alert as Read
    path(
        "alerts/<int:alert_id>/read/",
        views.mark_alert_read,
        name="mark_alert_read"
    ),

    # Reports
    path(
        "reports/",
        views.reports,
        name="reports"
    ),
    path(
        "case/<int:case_id>/edit/",
        views.edit_case,
        name="edit_case"
    ),
    path(
        "cases/<int:case_id>/edit/",
        views.edit_case,
        name="edit_case"
    ),
    path(
        "case/<int:case_id>/delete/",
        views.delete_case,
        name="delete_case"
    ),
    path(
        "case/<int:case_id>/delete/",
        views.delete_case,
        name="delete_case"
    ),
    path(
        "alerts/mark-all-read/",
        views.mark_all_alerts_read,
        name="mark_all_alerts_read"
    ),
    path(
        "alerts/mark-all-read/",
        views.mark_all_alerts_read,
        name="mark_all_alerts_read"
    ),path("alerts/", views.alerts, name="alerts"),
    path(
        "alerts/read/<int:alert_id>/",
        views.mark_alert_read,
        name="mark_alert_read"
    ),
    path(
        "alerts/mark-all-read/",
        views.mark_all_alerts_read,
        name="mark_all_alerts_read"
    ),
    path(
        "reports/download/",
        views.download_report,
        name="download_report"
    ),  
    path(
        "download-report/",
        views.download_report,
        name="download_report"
    ),

]


# Media files (uploaded child photos)
if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )