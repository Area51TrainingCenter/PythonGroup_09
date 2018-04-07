from django.views.generic import TemplateView, DetailView

from mociones.models import Mocion

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
        contexto = super(Home, self).get_context_data(**kwargs)
        # contexto['nombre'] = 'Moisés'
        # contexto['tareas'] = ['Lavar', 'Cocinar', 'Planchar', 'Correr']
        # SELECT * FROM mociones_mocion ORDER BY id DESC LIMIT 5;
        contexto['mociones'] = Mocion.objects.all().order_by('-id')[:5]
        return contexto


class Detalle(DetailView):
    template_name = 'detalle.html'
    model = Mocion
    context_object_name = 'mocion'
