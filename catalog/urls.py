from catalog import views
from django.urls import include, path

urlpatterns = [
    path('', views.SectionsListView.as_view(), name='sections'),
    path('detail-section/<id_section>', views.section_detail_view, name='section_detail'),
    path('detail-section/<id_section>/product-detail/<id_product>', views.product_detail_view, name='product_detail')
]
