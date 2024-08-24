from django.contrib.admin import widgets


class CustomDateTimeWidget(widgets.AdminSplitDateTime):
    template_name = "datetime.html"