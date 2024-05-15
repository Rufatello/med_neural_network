from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from users.forms import UserFormCreate
from users.models import User
from users.services import generation


class UserCreation(CreateView):
    model = User
    form_class = UserFormCreate
    template_name = 'users/reg.html'
    success_url = reverse_lazy('users:code')

    def form_valid(self, form):
        code = generation()
        new_user = form.save(commit=False)
        new_user.code = code
        send_mail(
            subject='Подтверждение почты',
            message=f'Ваш код: {new_user.code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class CodeView(View):
    """Страница ввода кода, который пришел на почту"""
    model = User
    template_name = 'users/code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        code = request.POST.get('code')
        user = User.objects.filter(code=code).first()

        if user is not None and user.code == code:
            user.is_active = True
            user.save()
            return redirect('appointment:home')
