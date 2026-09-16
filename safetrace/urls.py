"""
URL configuration for safetrace project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path

from accounts import views


urlpatterns = [

    # ============================================================
    # ADMIN
    # ============================================================

    path(
        "admin/",
        admin.site.urls
    ),


    # ============================================================
    # HOME
    # ============================================================

    path(
        "",
        views.home,
        name="home"
    ),


    # ============================================================
    # AUTHENTICATION
    # ============================================================

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


    # ============================================================
    # DASHBOARD
    # ============================================================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    # ============================================================
    # MISSING CHILD REGISTRATION
    # ============================================================

    path(
        "register-missing-child/",
        views.register_missing_child,
        name="register_missing_child"
    ),


    # ============================================================
    # MISSING CASES
    # ============================================================

    path(
        "missing-cases/",
        views.missing_cases,
        name="missing_cases"
    ),


    # ============================================================
    # CASE DETAILS
    # ============================================================

    path(
        "case/<int:case_id>/",
        views.case_detail,
        name="case_detail"
    ),


    # ============================================================
    # UPDATE CASE STATUS
    # ============================================================

    path(
        "case/<int:case_id>/update-status/",
        views.update_case_status,
        name="update_case_status"
    ),


    # ============================================================
    # EDIT CASE
    # ============================================================

    path(
        "case/<int:case_id>/edit/",
        views.edit_case,
        name="edit_case"
    ),


    # ============================================================
    # DELETE CASE
    # ============================================================

    path(
        "case/<int:case_id>/delete/",
        views.delete_case,
        name="delete_case"
    ),


    # ============================================================
    # ALERTS
    # ============================================================

    path(
        "alerts/",
        views.alerts,
        name="alerts"
    ),

    path(
        "alerts/<int:alert_id>/read/",
        views.mark_alert_read,
        name="mark_alert_read"
    ),

    path(
        "alerts/mark-all-read/",
        views.mark_all_alerts_read,
        name="mark_all_alerts_read"
    ),


    # ============================================================
    # REPORTS
    # ============================================================

    path(
        "reports/",
        views.reports,
        name="reports"
    ),

    path(
        "reports/download/",
        views.download_report,
        name="download_report"
    ),
]


# ============================================================
# MEDIA FILES
# ============================================================
# Used during local development for uploaded child photos.

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        views.serve_media,
        name="serve_media",
    ),
]