from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('aluno/', include('app.urls')), #inclui a rota dos app
]
