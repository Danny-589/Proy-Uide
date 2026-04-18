from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_cargo_titulo_profile_hoja_de_vida_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resenas_recibidas', to='core.profile', verbose_name='Perfil reseñado')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resenas_escritas', to='core.profile', verbose_name='Autor de la reseña')),
            ],
            options={
                'verbose_name': 'Reseña',
                'verbose_name_plural': 'Reseñas',
                'ordering': ['-fecha'],
                'unique_together': {('destinatario', 'autor')},
            },
        ),
    ]
