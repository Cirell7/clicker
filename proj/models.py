from django.db import models
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_core(sender, **kwargs):
    if sender.name == 'proj':  # замените на имя вашего приложения
        if not Core.objects.exists():
            Core.objects.create()

class Core(models.Model):
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    def click(self):
        self.coins += self.click_power
        self.save()
        return self.coins
