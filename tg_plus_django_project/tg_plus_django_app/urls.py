from django.urls import path
from django.views.generic import TemplateView
from .views import *
from .views_package.home_view import *
from .views_package.user_page_and_change_self_data_view import *
from .views_package.confirm_cancel_change_order_views import *
from .views_package.login_registration_views import *
from .views_package.catalog_page_view import *
from .views_package.consoles_and_console_model_page_views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contacts_page/', TemplateView.as_view(template_name='contacts_page.html')),
    path('reg_and_auth_page/', RegFormView.as_view(), name='reg_and_auth_page'),
    path('auth_page/', LogFormView.as_view(), name='user_page'),
    path('user_page/', UserPageView.as_view(), name='user_page'),
    path('user_page/<str:user_data_to_change>/', ChangeDataView.as_view(), name='change_user_data_page'),
    path('user_page/change_my_order/<str:order_id_to_change>/', ChangeOrderView.as_view(), name='change_order_page'),
    path('cancel_my_order/<str:order_id_to_change>', CancelOrderView.as_view(), name='cancel_order_page'),
    path('user_page/confirm_my_order/<str:order_id_to_change>', ConfirmOrderView.as_view(), name='confirm_order_page'),
    path('catalog_page/', CatalogPageView.as_view(), name='catalog_page'),
    path('console_page/', ConsolesPageView.as_view(), name='console_page'),
    path('console_page/<str:console_model>/', ConsoleModelPageView.as_view(), name='console_model_page'),
]