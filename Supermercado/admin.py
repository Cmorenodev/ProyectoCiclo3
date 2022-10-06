from django.contrib import admin

# Register your models here.
from Supermercado.models import ADMINISTRATOR
from Supermercado.models import BUSINESS
from Supermercado.models import EMPLOYEES
from Supermercado.models import PRODUCTS
from Supermercado.models import INCOME
from Supermercado.models import WORKINGHOURS
from Supermercado.models import EMPLOYEEPAYROLL
from Supermercado.models import CUSTOMERS
from Supermercado.models import LISTBUY
from Supermercado.models import EXPENSES


admin.site.register(ADMINISTRATOR)
admin.site.register(BUSINESS)
admin.site.register(EMPLOYEES)
admin.site.register(PRODUCTS)
admin.site.register(INCOME)
admin.site.register(WORKINGHOURS)
admin.site.register(EMPLOYEEPAYROLL)
admin.site.register(CUSTOMERS)
admin.site.register(LISTBUY)
admin.site.register(EXPENSES)