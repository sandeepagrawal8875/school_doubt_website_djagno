# Generated by Django 3.1.4 on 2020-12-08 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('views', models.IntegerField(default=0)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('answer_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question')),
            ],
        ),
    ]
