from django.db import models

class Work(models.Model):
    work_name = models.CharField(max_length=100, verbose_name="نام نمونه کار")
    work_description = models.TextField(max_length=200, verbose_name="توضیح کوتاه در مورد نمونه کار", null=True)
    work_url = models.CharField(verbose_name="کد نمونه کار در آپارات", max_length=300)
    displayOnLandingPage = models.BooleanField(default=False, verbose_name="نمایش در صفحه اصلی")

    class Meta:
        verbose_name_plural = "نمونه کار ها"


class TeamMember(models.Model):
    member_name = models.CharField(max_length=100, verbose_name="نام عضو تیم")
    member_job = models.CharField(max_length=150, verbose_name="وظیفه در تیم")
    member_image = models.ImageField(verbose_name="تصویر عضو", null="True", upload_to="team/")

    class Meta:
        verbose_name_plural = "اعضای تیم"


class Corporation(models.Model):
    corp_name = models.CharField(max_length=100, verbose_name="نام سازمان", null="True")
    corp_image = models.ImageField(verbose_name="لوگوی سازمان", null="True", upload_to="corp/")

    class Meta:
        verbose_name_plural = "همکاری ها"
