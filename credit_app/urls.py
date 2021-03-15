
from django.contrib                  import admin
from django.urls                     import path, include

urlpatterns = [
    path('admin/'        , admin.site.urls),
    path('starter/'      , include('starter.urls')),
    path('generate_pdf/' , include('generate_pdf.urls')),
]
