from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import News
from .forms import FeedbackForm

def home(request):
    news = News.objects.all().order_by('-id')

    faq = [
        {"q": _("Работает ли ваша служба в моём городе?"),
         "a": _("Да. Уточните ваш город в форме ниже — мы ответим и подскажем ближайший филиал.")},
        {"q": _("Вы проводите исследования по заявкам организаций?"),
         "a": _("Да. Принимаем заявки от организаций и госструктур. Условия уточняются по контактам.")},
        {"q": _("Какие сроки выполнения исследований?"),
         "a": _("Сроки зависят от вида исследования. Обычно от 1 до 7 рабочих дней.")},
        {"q": _("Как получить консультацию?"),
         "a": _("Оставьте вопрос в форме обратной связи — мы свяжемся с вами.")},
    ]

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ сохраняем в БД
            messages.success(request, _("Спасибо! Ваше сообщение отправлено."))
            return redirect("home")  # чтобы не отправлялось повторно при F5
    else:
        form = FeedbackForm()

    return render(request, "main/home.html", {
        "news": news,
        "faq": faq,
        "feedback_form": form,
    })


def about(request):
    return render(request, 'main/about.html')


def structure(request):
    return render(request, 'main/structure.html')


def services(request):
    return render(request, 'main/services.html')


def news(request):
    news_list = News.objects.all().order_by('-id')
    return render(request, 'main/news.html', {
        'news_list': news_list
    })


def contacts(request):
    return render(request, 'main/contacts.html')


# ===== СТРАНИЦЫ "ПОДРОБНЕЕ" =====

def service_diagnostics(request):
    return render(request, 'main/service_page.html', {
        'title': _("Диагностические исследования"),
        'text': _("Лабораторные исследования для обеспечения ветеринарной безопасности.")
    })


def service_molecular(request):
    return render(request, 'main/service_page.html', {
        'title': _("Молекулярные исследования"),
        'text': _("ПЦР и другие современные методы анализа.")
    })


def service_monitoring(request):
    return render(request, 'main/service_page.html', {
        'title': _("Эпизоотический мониторинг"),
        'text': _("Анализ и контроль ветеринарной ситуации.")
    })


def service_training(request):
    return render(request, 'main/service_page.html', {
        'title': _("Учебно-методическая деятельность"),
        'text': _("Повышение квалификации специалистов.")
    })


def documents(request):
    return render(request, 'main/documents.html')



