import json
import re
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from tinydb import TinyDB


@method_decorator(csrf_exempt, name='dispatch')
class SelectTemplate(View):
    def post(self, request):
        db = TinyDB('db.json')
        templates = db.all()  # get templates
        form_data = request.POST  # get form

        # Validation
        new_form_data = {}  # new form, where values = types of values in old form
        for field in form_data:
            if (re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', form_data[field]) or
                    re.fullmatch(r'\d{4}-\d{2}-\d{2}', form_data[field])):
                new_form_data[field] = 'date'
            elif re.fullmatch(r'\+7 \d{3} \d{3} \d{2} \d{2}', form_data[field]):
                new_form_data[field] = 'phone'
            elif re.fullmatch(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+', form_data[field]):
                new_form_data[field] = 'email'
            else:
                new_form_data[field] = 'text'

        # Search template
        for template in templates:
            template = dict(template)
            template_name = template['name']
            template.pop('name')
            template_is_find = False  # flag
            for key in template:
                try:
                    new_form_value = new_form_data[key]
                except KeyError:
                    template_is_find = False
                    break
                if template[key] == new_form_value:
                    print(f'{template[key]} == {new_form_value}?')
                    template_is_find = True
                    continue
                else:
                    template_is_find = False
                    break
            if template_is_find:
                return HttpResponse(template_name)
            else:
                continue
        return HttpResponse(json.dumps(new_form_data))
