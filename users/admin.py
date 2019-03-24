from django.contrib import admin
from .models import Profile
from .models import Owner
from .models import Matatu
from .models import Crew
from .models import Finance
from .models import Activity_log


admin.site.register(Profile)
admin.site.register(Owner)
admin.site.register(Matatu)
admin.site.register(Crew)
admin.site.register(Finance)
admin.site.register(Activity_log)


