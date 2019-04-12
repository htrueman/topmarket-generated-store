from django.http import JsonResponse


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            form.save()
            return JsonResponse({
                'successed': True,
            })
        else:
            return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            form_errors = {}
            errors = {}
            for key, value in form.errors.items():
                errors[key] = ' '.join(value)
            form_errors['errors'] = errors
            return JsonResponse(form_errors)
        else:
            return response
