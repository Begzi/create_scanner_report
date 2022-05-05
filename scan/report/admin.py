from django.contrib import admin

from .models import Group_vulnerability, Node, Vulnerability, CVSS2, CVSS3
# Register your models here.

admin.site.register(Node)
admin.site.register(Group_vulnerability)
admin.site.register(Vulnerability)
admin.site.register(CVSS2)
admin.site.register(CVSS3)