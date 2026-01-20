# urls.py
from django.urls import path
from .views import MusicaListView, MusicaDetailByCodigoView

urlpatterns = [
    path("musicas/", MusicaListView.as_view(), name="musica-list"),           # lista / filtro
    path("musicas/<str:codigo>/", MusicaDetailByCodigoView.as_view(), name="musica-por-codigo"),  # detalhe
]
