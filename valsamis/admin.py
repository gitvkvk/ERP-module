from django.contrib import admin
from .models import ship, company, customer, supplier, project, PurchaseOrder, MaterialItemRegister, generalitem

admin.site.register(ship)
admin.site.register(company)
admin.site.register(customer)
admin.site.register(supplier)
admin.site.register(project)
admin.site.register(PurchaseOrder)
admin.site.register(MaterialItemRegister)
admin.site.register(generalitem)


