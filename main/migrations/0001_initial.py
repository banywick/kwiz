# Generated by Django 5.0.6 on 2024-05-18 08:32

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Младшее звено 1-4 классы', 'Младшее звено 1-4 класс'), ('Среднее звено 5-7 классы', 'Среднее звено 5-7 классы'), ('Старшее звено 8-11 классы', 'Старшее звено 8-11 классы')], max_length=100, verbose_name='Наименование степени обучающихся (звена)')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('Date_Start', models.DateField(blank=True, null=True)),
                ('Date_End', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Интеллектуальный квиз', 'Интеллектуальный квиз'), ('Музыкальный квиз', 'Музыкальный квиз'), ('Спортивное мероприятие', 'Спортивное мероприятие'), ('Классическая Мафия', 'Классическая Мафия'), ('Своя Игра', 'Своя Игра'), ('Интеллектуальная игра 100к1', 'Интеллектуальная игра 100к1'), ('Брейн-ринг', 'Брейн-ринг')], max_length=100, verbose_name='Наименование типа мероприятия')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('На рассмотрении', 'На рассмотрении'), ('Принята', 'Принята'), ('Отклонена', 'Отклонена'), ('Отменена', 'Отменена'), ('Посещено', 'Посещено')], default='На рассмотрении', max_length=255, verbose_name='Статус заявки')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_disbanded', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('class_scool', models.CharField(max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('max_eventers', models.IntegerField(default=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField(blank=True, null=True)),
                ('EducationLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.educationlevel')),
                ('EventType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Plan_Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('Date_Plan', models.DateField(blank=True, null=True)),
                ('Date_Fact', models.DateField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Eventers_Plan', models.IntegerField(blank=True, null=True)),
                ('Eventers_Fact', models.IntegerField(blank=True, null=True)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.event')),
                ('Event_Plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.event_plan')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество (если есть)')),
                ('klass', models.CharField(blank=True, choices=[('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('5Г', '5Г'), ('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('6Г', '6Г'), ('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('7Г', '7Г'), ('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('8Г', '8Г'), ('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('9Г', '9Г'), ('10А', '10А'), ('10Б', '10Б'), ('10В', '10В'), ('10Г', '10Г'), ('11А', '11А'), ('11Б', '11Б'), ('11В', '11В'), ('11Г', '11Г')], max_length=4, verbose_name='Класс обучающегося')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateField(blank=True, null=True)),
                ('Event_Plan_Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event_plan_position')),
                ('Profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('Team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.TextField(blank=True, null=True)),
                ('Time_Submit', models.DateTimeField(blank=True, null=True)),
                ('Event_Plan_Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event_plan_position')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.AddField(
            model_name='event_plan',
            name='Responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.CreateModel(
            name='InvitationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_Date', models.DateField(auto_now_add=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.invitation')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.status')),
            ],
        ),
        migrations.CreateModel(
            name='Team_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Result', models.TextField(blank=True, null=True)),
                ('Invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.invitation')),
                ('Team_List', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team_list')),
            ],
        ),
        migrations.CreateModel(
            name='Team_Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('Team_List', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team_list')),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='Team_Members',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.team_members'),
        ),
    ]
