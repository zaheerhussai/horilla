"""
project/sidebar.py
"""

from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

from base.templatetags.basefilters import is_leave_approval_manager, is_reportingmanager
from leave.templatetags.leavefilters import is_compensatory

MENU = trans("Project")
IMG_SRC = "images/ui/project.png"

SUBMENUS = [
    {
        "menu": trans("Dashboard"),
        "redirect": reverse("project-dashboard-view"),
        # "accessibility": "leave.sidebar.dashboard_accessibility",
    },
    {
        "menu": trans("Projects"),
        "redirect": reverse("project-view"),
    },
    {
        "menu": trans("Tasks"),
        "redirect": reverse("task-all"),
        # "accessibility": "leave.sidebar.leave_request_accessibility",
    },
    {
        "menu": trans("Timesheet"),
        "redirect": reverse("view-time-sheet"),
        # "accessibility": "leave.sidebar.type_accessibility",
    },
]


def dashboard_accessibility(request, submenu, user_perms, *args, **kwargs):
    have_perm = request.user.has_perm("leave.view_leaverequest")
    if not have_perm:
        submenu["redirect"] = reverse("leave-employee-dashboard") + "?dashboard=true"
    return True


def leave_request_accessibility(request, submenu, user_perms, *args, **kwargs):
    return (
        request.user.has_perm("leave.view_leaverequest")
        or is_leave_approval_manager(request.user)
        or is_reportingmanager(request.user)
    )


def type_accessibility(request, submenu, user_perms, *args, **kwargs):
    return request.user.has_perm("leave.view_leavetype")


def assign_accessibility(request, submenu, user_perm, *args, **kwargs):
    return request.user.has_perm("leave.view_assignedleave") or is_reportingmanager(
        request.user
    )


def holiday_accessibility(request, submenu, user_perms, *args, **kwargs):
    return not request.user.has_perm("leave.add_holiday")


def company_leave_accessibility(request, submenu, user_perms, *args, **kwargs):
    return not request.user.has_perm("leave.add_companyleave")


def componstory_accessibility(request, submenu, user_perms, *args, **kwargs):
    return is_compensatory(request.user)
