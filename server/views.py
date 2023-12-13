from inertia import render
from django.http import HttpRequest, HttpResponse
from django.views import View


class Test(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            component="Test",
            props={
                'test': {
                    'first_name': "Mameng",
                    'last_name': "Galuh"
                }
            }
        )
