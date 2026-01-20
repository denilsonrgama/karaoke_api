# scripts/update_video_names.py
import os
import sys
import django

# Adiciona a raiz do projeto ao PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from musicas.models import Musica

def atualizar_caminhos_video():
    todas = Musica.objects.all()
    atualizados = 0

    for m in todas:
        if m.caminho_video:
            # acessa o nome do arquivo corretamente
            nome_arquivo = os.path.basename(m.caminho_video.name)
            if nome_arquivo != m.caminho_video.name:
                print(f"[ATUALIZANDO] {m.codigo}: {m.caminho_video.name} -> {nome_arquivo}")
                m.caminho_video.name = nome_arquivo  # atualiza o FieldFile
                m.save(update_fields=["caminho_video"])
                atualizados += 1

    print(f"Total de registros atualizados: {atualizados}")

if __name__ == "__main__":
    atualizar_caminhos_video()
