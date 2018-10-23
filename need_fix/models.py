from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html


# class Comment(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#
#
# category = models.ForeignKey(Category, on_delete="SET_NULL")
# comment = models.ForeignKey(Comment, on_delete="SET_NULL")


class Record(models.Model):
    status_choices = (
        (True, '已完成'),
        (False, '进行中'),
    )

    priority_choices = (
        (True, '高'),
        (False, '中'),
        (None, '低'),
    )

    content = models.TextField(max_length=255, blank=False, verbose_name=_("内容"))
    person = models.CharField(max_length=64, blank=False, verbose_name=_("负责人"))
    status = models.BooleanField(default=False, choices=status_choices, verbose_name=_("状态"))
    priority = models.NullBooleanField(default=None, choices=priority_choices, verbose_name=_("优先级"))
    created = models.DateTimeField(verbose_name=_('date created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('last modified'), auto_now=True)

    def colored_status(self):
        if self.status:
            color = "green"
            message = "已完成"
        else:
            color = "red"
            message = "进行中"
        return format_html('<span style="color: {};">{}</span>'.format(color, message))

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '任务记录'
        verbose_name_plural = '任务记录'
        # 指定默认排序规则
        ordering = ['id']

    colored_status.short_description = "状态"
