from rest_framework import serializers
from .models import Musica

class MusicaSerializer(serializers.ModelSerializer):
    caminho_video = serializers.SerializerMethodField()

    class Meta:
        model = Musica
        fields = ["id", "codigo", "nome", "artista", "letra", "caminho_video"]

    def get_caminho_video(self, obj):
        """
        Retorna apenas o nome do arquivo como string.
        """
        if obj.caminho_video:
            return str(obj.caminho_video.name)  # força string, sem conteúdo binário
        return None
