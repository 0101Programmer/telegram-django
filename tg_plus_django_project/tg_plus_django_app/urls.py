from django.urls import path

from .views_package.catalog_page_view import *
from .views_package.confirm_cancel_change_order_views import *
from .views_package.consoles_and_console_model_page_views import *
from .views_package.home_view import *
from .views_package.login_registration_views import *
from .views_package.user_page_and_change_self_data_view import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:user_id>', HomePageById.as_view(), name='authed_home'),

    path('contacts_page/<int:user_id>/', TemplateView.as_view(template_name='contacts_page.html')),
    path('contacts_page/', TemplateView.as_view(template_name='contacts_page.html')),

    path('reg_and_auth_page/', RegFormView.as_view(), name='reg_and_auth_page'),
    path('auth_page/', LogFormView.as_view(), name='login_page'),

    path('user_page/<int:user_id>/', UserPageView.as_view(), name='user_page_by_id'),
    path('user_page/<int:user_id>/<str:user_data_to_change>/', ChangeDataView.as_view(), name='change_user_data_page'),

    path('user_page/<int:user_id>/change_my_order/<str:order_id_to_change>/', ChangeOrderView.as_view(), name='change_order_page'),
    path('cancel_my_order/<int:user_id>/<str:order_id_to_change>', CancelOrderView.as_view(), name='cancel_order_page'),
    path('user_page/<int:user_id>/confirm_my_order/<str:order_id_to_change>', ConfirmOrderView.as_view(), name='confirm_order_page'),

    path('catalog_page/', CatalogPageView.as_view(), name='catalog_page'),
    path('catalog_page/<int:user_id>/', CatalogPageViewById.as_view(), name='catalog_page_by_id'),

    path('console_page/', ConsolesPageView.as_view(), name='console_page'),
    path('console_page/<int:user_id>/', ConsolesPageViewById.as_view(), name='console_page_by_id'),

    path('console_page/<str:console_model>/', ConsoleModelPageView.as_view(), name='console_model_page'),
    path('console_page/<int:user_id>/<str:console_model>/', ConsoleModelPageViewById.as_view(), name='console_model_page_by_id'),
]