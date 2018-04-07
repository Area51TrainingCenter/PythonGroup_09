from django.views.generic import TemplateView
# from django.shortcuts import render
# from django.views import View


# class Home(View):
#     def get(self, request):
#         return render(request, 'index.html', {})
#
#    def post(self, request):
#         return
#

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'nombre': 'Moisés',
            'tareas': ['Lavar', 'Cocinar', 'Planchar', 'Correr']
        }

