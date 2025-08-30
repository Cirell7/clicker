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
    temporary_coins =models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    def click(self):
        self.temporary_coins+=self.click_power
        self.save()
    def get_temporary_coins(self):
        return self.temporary_coins
    def get_coins(self):
        return self.coins
    def get_click_power(self):
        return self.click_power
    def core_save(self):
        self.coins = self.temporary_coins
