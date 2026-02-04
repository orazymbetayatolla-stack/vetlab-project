from django.db import models


class News(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    short_text = models.TextField("Краткое описание")
    image = models.ImageField(
        "Изображение",
        upload_to="news/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class Feedback(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("E-mail")
    message = models.TextField("Вопрос")
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.email}"
