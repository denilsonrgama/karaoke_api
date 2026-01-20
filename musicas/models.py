#karaoke_api/musicas/models.py  
from django.db import models


class Musica(models.Model):
    codigo = models.CharField(max_length=20,unique=True,db_index=True)
    nome = models.CharField(max_length=255, db_index=True)
    artista = models.CharField(max_length=255, db_index=True)
    letra = models.TextField()
    caminho_video = models.FileField(
        upload_to="",  # ou "videos/" se quiser subpastas
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nome} - {self.artista}"


