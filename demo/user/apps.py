from django.apps import AppConfig

# 应用配置
class UserConfig(AppConfig):
    name = 'user'  # 此类加载至哪个应用，Django创应用时自动写入
    verbose_name = 'user应用'  # 此应用的可视化名字，后台可以察觉
