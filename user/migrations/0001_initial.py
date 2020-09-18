# Generated by Django 3.1.1 on 2020-09-18 14:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('genre', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'unique': '이미 존재하는 이메일입니다.'}, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('nickname', models.CharField(error_messages={'unique': '이미 존재하는 닉네임입니다.'}, max_length=50, unique=True)),
                ('name', models.CharField(default='username', max_length=30)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(default='010-1234-5678', max_length=13)),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('is_author', models.BooleanField(default=False)),
                ('point', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('prefer_genre', models.ManyToManyField(related_name='prefer_users', to='genre.Genre')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', user.managers.TMUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TMAuthor',
            fields=[
                ('author_name', models.CharField(error_messages={'unique': '이미 존재하는 작가명입니다.'}, max_length=50, unique=True, verbose_name='작가명')),
                ('introduce', models.TextField(blank=True, max_length=500, null=True)),
                ('page_link', models.TextField(blank=True, max_length=300, null=True)),
                ('sns_link', models.TextField(blank=True, max_length=300, null=True)),
                ('portfolio', models.FileField(blank=True, null=True, upload_to='portfolios')),
                ('opening_date', models.DateField(default=django.utils.timezone.now)),
                ('follower_num', models.PositiveIntegerField(default=0)),
                ('tomag_num', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.tmuser')),
            ],
        ),
    ]
