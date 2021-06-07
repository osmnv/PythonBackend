
from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict


class JsonDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        if self.request.method == "GET":
            self.object = self.get_object()
            data = model_to_dict(self.object)
            return JsonResponse(
                data,
                safe=False,
                json_dumps_params={'ensure_ascii': False, 'indent': 4}
            )
        response = HttpResponse()
        response.status_code = 405
        return response
