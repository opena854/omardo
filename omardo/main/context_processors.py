from django.http import HttpRequest
from django.apps import apps

MENU_OPTIONS = ("main", "polls")

def menu(request: HttpRequest):
    current_app = request.resolver_match.app_name
    
    def option_info(app_name):
        app = apps.get_app_config(app_name)
        
        return {
            "label": app.verbose_name,
            "url": ":".join([app.name, "index"]),
            "active": current_app == app.name
        }
    
    options = list([option_info(app) for app in MENU_OPTIONS])

    return {
        "MENU_OPTIONS": options,
        "CURRENT_APP": option_info(current_app)
    }

