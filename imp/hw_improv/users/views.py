
from django.shortcuts import render, redirect
from django.views import View

from django.contrib import messages #Flash messages

from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:main")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request, *args, **kwargs):
        pass
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Вітаю {username}. Ваш акаунт успішно створено.')
            return redirect(to="users:login")

        return render(request, self.template_name, {"form": form})
    # якщо форма не пройшла реєстрацію, то повертаємо з помилками


# def my_mess(request):
#     messages.success(request, 'Успішно створено')
#     messages.warning(request, 'Попередження')
#     messages.error(request, 'Помилка')
#     return render(request, 'xx.html')