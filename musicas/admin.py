from django.contrib import admin
from musicas.models import Musica

# Admin do carro
@admin.register(Musica)
class GenreAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'codigo',
        'nome',        
        'artista',
        'letra',
        'caminho_video',
    )
    list_filter = (
        'codigo',
        'nome',        
        'artista'
    )
    search_fields = (
        'codigo',
        'nome',        
        'artista'
    )
    ordering = ('-codigo',)    
    readonly_fields = ('codigo',)
