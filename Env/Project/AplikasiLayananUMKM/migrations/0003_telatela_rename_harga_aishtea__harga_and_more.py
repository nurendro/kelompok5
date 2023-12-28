# Generated by Django 4.2.6 on 2023-12-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikasiLayananUMKM', '0002_aishtea_roti_saguku_wang_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelaTela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_menu', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('_harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gambar', models.ImageField(null=True, upload_to='img/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='aishtea',
            old_name='harga',
            new_name='_harga',
        ),
        migrations.RenameField(
            model_name='roti',
            old_name='harga',
            new_name='_harga',
        ),
        migrations.RenameField(
            model_name='saguku',
            old_name='harga',
            new_name='_harga',
        ),
        migrations.RenameField(
            model_name='wang',
            old_name='harga',
            new_name='_harga',
        ),
    ]