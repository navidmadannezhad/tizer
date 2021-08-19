# Generated by Django 3.1.7 on 2021-08-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_image', models.ImageField(upload_to='', verbose_name='لوگوی سازمان')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memeber_name', models.CharField(max_length=100)),
                ('member_job', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100, verbose_name='نام نمونه کار')),
                ('work_description', models.CharField(max_length=200, verbose_name='توضیح کوتاه در مورد نمونه کار')),
                ('displayOnLandingPage', models.BooleanField(default=False, verbose_name='نمایش در صفحه اصلی')),
            ],
        ),
    ]