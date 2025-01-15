from django.urls import path

from loan_management_service.views import register_user,apply_loan, make_payment, get_statement

urlpatterns = [
    path("register_user/", register_user, name="register_user"),
    path("apply_loan/", apply_loan, name="apply_loan"),
]
