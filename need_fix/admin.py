from django.contrib import admin
from need_fix.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "status", "colored_status", "person", "priority", "created")
    list_editable = ("status",)
    ordering = ("status", "person", "priority")
    list_display_links = ("id", "content")

    list_filter = ('created', 'modified', 'person')  # 过滤器
    search_fields = ("content",)  # 搜索字段
    # date_hierarchy = 'created'  # 详细时间分层筛选　


admin.site.site_title = '企业信用项目进度共享平台'
admin.site.site_header = '登录|项目进度共享平台'


admin.site.register(Record, RecordAdmin)
