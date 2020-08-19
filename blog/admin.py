from django.contrib import admin
from .models import Post
from .models import Education
from .models import Work_Experience
from .models import Personal_Statement
from .models import UoB_Year_1
from .models import UoB_Year_2
from .models import UoB_Year_3
from .models import MyDetail
from .models import Gallery, Photos

# Register your models here.
admin.site.register(Post)
admin.site.register(Education)
admin.site.register(Work_Experience)
admin.site.register(Personal_Statement)
admin.site.register(UoB_Year_1)
admin.site.register(UoB_Year_2)
admin.site.register(UoB_Year_3)
admin.site.register(MyDetail)
admin.site.register(Gallery)
admin.site.register(Photos)
