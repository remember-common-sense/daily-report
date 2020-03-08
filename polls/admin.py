from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Question, Choice, Item, Team, System, SubSystem, Developer, Tester, Role, Progress1, Progress2, Progress3, Progress4, OtherWork, Risk, Matter, Email, EmailConfig

from django.apps import apps
from django.contrib import admin
from django.utils.text import capfirst

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    class QuestionFilter(admin.SimpleListFilter):
        title = _(u'项目组')
        parameter_name = 'question_text'

        def lookups(self, request, model_admin):
            return (
                ('0', _(u'网络收益')),

            )

        def queryset(self, request, queryset):
            if self.value() == 0:
                return queryset.filter(question_text__exact='网络收益')

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('get_question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', QuestionFilter]
    search_fields = ['pub_date']


def find_app_index(app_label):
    app = apps.get_app_config(app_label)
    main_menu_index = getattr(app, 'main_menu_index', 9999)
    return main_menu_index


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        app_list = templateresponse.context_data['app_list']
        app_list.sort(key=lambda r: find_app_index(r['app_label']))
        for app in app_list:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner


class Progress1Inline(admin.TabularInline):
    model = Progress1
    extra = 0

class Progress2Inline(admin.TabularInline):
    model = Progress2
    extra = 0

class Progress3Inline(admin.TabularInline):
    model = Progress3
    extra = 0

class Progress4Inline(admin.TabularInline):
    model = Progress4
    extra = 0

class ItemAdmin(admin.ModelAdmin):

    #批量标记任务已完成
    def make_done(self, request, queryset):
        queryset.update(is_done=True)
    make_done.short_description = "标记任务已完成"
    actions = ['make_done']

    #通过当前登录的用户过滤显示的数据
    def get_queryset(self, request):
        qs = super(ItemAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # tester_obj = Tester.objects.filter(name=request.user)
        # task_obj = tester_obj.qs.all().values("name")
        # return task_obj

        # return qs.get(tester=Tester.objects.filter(name=request.user))
        # return qs.filter(is_done=False)
        # return qs.filter(tester_name=request.user)
        return Item.objects.filter(is_done=False).filter(tester__name=request.user)

    def is_done_filter(self, request, extra_context=None):
        if not request.GET.has_key('is_done'):
            q = request.GET.copy()
            q['is_done'] = False
            request.GET = q
            request.META['完成情况'] = request.GET.urlencode()

            return super(ItemAdmin, self).is_done_filter(request, extra_context=extra_context)

    ordering = ('pub_date',)
    # list_editable = ['system']
    list_display = ('task', 'sub_task', 'team', 'system', 'sub_system', 'pub_date', 'comment', 'is_done')
    inlines = [Progress1Inline, Progress2Inline, Progress3Inline, Progress4Inline]
    fieldsets = [
        ('基本信息', {'fields': ['task', 'sub_task', 'pub_date']}),
        ('所属信息', {'fields': ['team', 'system', 'sub_system']}),
        ('人员信息', {'fields': ['developer', 'tester']}),
        ('备注信息', {'fields': ['comment', 'is_done'], 'classes': ['collapse']})
    ]
    list_filter = ['pub_date', 'team', 'system', 'sub_system', 'is_done']
    search_fields = ['task']
    empty_value_dispaly = '-none-'
    date_hierarchy = 'pub_date'
    filter_horizontal = ['developer', 'tester']

class OtherWorkAdmin(admin.ModelAdmin):
    ordering = ('pub_date',)
    list_display = ('content', 'pub_date')

class RiskAdmin(admin.ModelAdmin):
    ordering = ('pub_date',)
    list_display = ('content', 'team', 'pub_date')

class MatterAdmin(admin.ModelAdmin):
    ordering = ('pub_date',)
    list_display = ('content', 'team', 'pub_date')

class EmailConfigAdmin(admin.ModelAdmin):
    filter_horizontal = ['recipient', 'cc']
    list_display = ('title', 'team')

# registry = OrderedDict()
# registry.update(admin.site._registry)
# admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)

admin.site.register(Item, ItemAdmin)
admin.site.register(OtherWork, OtherWorkAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(Matter, MatterAdmin)
admin.site.register(Team)
admin.site.register(System)
admin.site.register(SubSystem)
admin.site.register(Developer)
admin.site.register(Tester)
admin.site.register(Role)
admin.site.register(Email)
admin.site.register(EmailConfig, EmailConfigAdmin)
admin.site.site_title = '测试日报'
# admin.site.register(Progress1)
# admin.site.register(Progress2)
# admin.site.register(Progress3)
# admin.site.register(Progress4)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

