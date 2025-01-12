from django.urls import path

from .views_package.catalog_page_view import *
from .views_package.category_page_view import CategoryPageViewById, CategoryPageView
from .views_package.confirm_cancel_change_order_views import *
from .views_package.home_view import *
from .views_package.login_registration_views import *
from .views_package.personal_page_view import UserPersonalPageView
from .views_package.product_page_view import ProductPageViewById, ProductPageView
from .views_package.rate_order_view import RateOrderView
from .views_package.user_page_and_change_self_data_view import *

urlpatterns = [
    # Главная страница
    path('', HomePage.as_view(), name='home'),
    path('<int:user_id>', HomePageById.as_view(), name='authed_home'),
    # < --- --- --- --- --- --- >

    # Страница для продуктов одной категории
    path('category_page/<int:user_id>/<str:category_name>', CategoryPageViewById.as_view(), name='category_page_by_id'),
    path('category_page/<str:category_name>', CategoryPageView.as_view(), name='category_page'),
    # < --- --- --- --- --- --- >

    # Страница одного продукта
    path('category_page/<int:user_id>/<str:category_name>/product_page/<int:product_id>', ProductPageViewById.as_view(), name='product_page_by_id'),
    path('category_page/<str:category_name>/product_page/<int:product_id>', ProductPageView.as_view(),
         name='product_page'),
    # < --- --- --- --- --- --- >

    # Личная страница
    path('user_page/<int:user_id>/', UserPersonalPageView.as_view(), name='user_personal_page'),
    # < --- --- --- --- --- --- >

    # Изменение личный данных
    path('user_page/<int:user_id>/<str:user_data_to_change>/', ChangeDataView.as_view(), name='change_user_data_page'),
    # < --- --- --- --- --- --- >

    # Изменение заказа, его статусов, оценка заказа
    path('user_page/<int:user_id>/change_my_order/<str:order_id_to_change>/', ChangeOrderView.as_view(),
         name='change_order_page'),
    path('cancel_my_order/<int:user_id>/<str:order_id_to_change>', CancelOrderView.as_view(), name='cancel_order_page'),
    path('user_page/<int:user_id>/confirm_my_order/<str:order_id_to_change>', ConfirmOrderView.as_view(),
         name='confirm_order_page'),
    path('user_page/<int:user_id>/rate_my_order/<str:order_id_to_rate>', RateOrderView.as_view(),
         name='rate_order_page'),
    # < --- --- --- --- --- --- >

    # Контакты
    path('contacts_page/<int:user_id>/', TemplateView.as_view(template_name='contacts_page.html')),
    path('contacts_page/', TemplateView.as_view(template_name='contacts_page.html')),
    # < --- --- --- --- --- --- >

    # Регистрация и авторизация
    path('reg_and_auth_page/', RegFormView.as_view(), name='reg_and_auth_page'),
    path('auth_page/', LogFormView.as_view(), name='login_page'),
    # < --- --- --- --- --- --- >

    # Каталог
    path('catalog_page/', CatalogPageView.as_view(), name='catalog_page'),
    path('catalog_page/<int:user_id>/', CatalogPageViewById.as_view(), name='catalog_page_by_id'),
    # < --- --- --- --- --- --- >
]