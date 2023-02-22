from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from .models import UserComment
from .forms import UserCommentForm


class UserCommentView(View):
    model = UserComment
    form_class = UserCommentForm
    template_name = 'comments/usercomments.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'success'})
        return JsonResponse({'message': 'invalid'})