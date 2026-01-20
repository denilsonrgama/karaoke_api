# karaoke_api/  views.py
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Musica
from .serializers import MusicaSerializer

class MusicaListView(ListAPIView):
    serializer_class = MusicaSerializer

    def get_queryset(self):
        queryset = Musica.objects.all()

        # Recebendo parâmetros da query string
        codigo = self.request.query_params.get("codigo")
        artista = self.request.query_params.get("artista")
        nome = self.request.query_params.get("nome")
        


        # 🔹 FILTRO POR CÓDIGO (retorna só 1)
        if codigo:
            # Se o campo codigo for IntegerField
            try:
                codigo_int = int(codigo)
                queryset = queryset.filter(codigo=codigo_int)
            except ValueError:
                queryset = queryset.none()  # código inválido → retorna vazio

        if artista:
            queryset = queryset.filter(artista__icontains=artista)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset.order_by("codigo")


class MusicaDetailByCodigoView(RetrieveAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    lookup_field = "codigo"  # 🔹 Busca pelo campo 'codigo' em vez de 'pk'
