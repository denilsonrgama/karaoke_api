import pandas as pd
from django.core.management.base import BaseCommand
from musicas.models import Musica

class Command(BaseCommand):
    help = "Importa músicas de um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            'arquivo',
            type=str,
            help='Caminho do arquivo CSV'
        )

    def handle(self, *args, **kwargs):
        arquivo = kwargs['arquivo']

        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin-1"
        )

        total = 0
        for _, row in df.iterrows():
            Musica.objects.update_or_create(
                codigo=str(row['codigo']).replace('.0', '').strip(),
                defaults={
                    'nome': str(row['nome']).strip(),
                    'artista': str(row['artista']).strip(),
                    'letra': str(row['letra']).strip(),
                }
            )
            total += 1

        self.stdout.write(
            self.style.SUCCESS(f"{total} músicas importadas com sucesso!")
        )
