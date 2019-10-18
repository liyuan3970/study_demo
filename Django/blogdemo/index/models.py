from django.db import models


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50, null=False, verbose_name="名称")

    class Meta:
        verbose_name = verbose_name_plural = '类别'

    def __str__(self):
        return self.tag_name


class Auther(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '男性'),
        (STATUS_DELETE, '女性'),
    )
    # null = True的时候才是设置不能为空！
    auther_name = models.CharField(max_length=50, null=True, verbose_name="作者姓名")

    sex = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="作者性别")

    age = models.IntegerField(verbose_name="作者年龄")

    class Meta:
        verbose_name = verbose_name_plural = '作者'

    # 这个是在admin中返回作者的创建成功后的列表
    def __str__(self):
        return self.auther_name


class Post(models.Model):
    post_name = models.CharField(max_length=50, null=True, verbose_name="名称")
    time = models.TimeField()
    auther = models.ForeignKey(Auther, verbose_name="作者姓名", on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, verbose_name="文章类别", on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=50, null=True, verbose_name="文章内容")

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.post_name
