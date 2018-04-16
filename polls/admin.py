from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# http://127.0.0.1:8080/admin/ 后台自动添加注册的模块， 相当于展示每个数据表的管理。 

class ChoiceInline(admin.TabularInline):  # StackedInline 是堆积瀑布增加，布局空隙太大， 换成：表格式的单行显示关联对象的方法
  model = Choice
  extra = 1  # 也可提供 3 个足够的选项字段（空的待填）

class QuestionAdmin(admin.ModelAdmin):
  # fields = ['pub_date', 'question_text']   #  改变自动生成的表单，如：排序方法。   还可以分组 fieldsets 设置
  fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline] # 编辑页面添加关联表单
  list_display = ('question_text', 'pub_date', 'was_published_recently')  # 列表展示的字段，最后一个是定义的方法字段。
  list_filter = ['pub_date']  # 添加了一个“过滤器”侧边栏，因为此字段是：DateTimeField 类型，自然显示日期相关的。
  search_fields = ['question_text'] # 在列表的顶部增加一个搜索框。可以使用任意多的字段，来Like查询。
  list_per_page = 20 # 定义每页的个数，默认 100个。

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)  # 与Question 关联一块处理，不需要单独 管理选项了，没多大意义。

admin.site.site_header = "投票管理后台"
admin.site.site_title = "在线投票"