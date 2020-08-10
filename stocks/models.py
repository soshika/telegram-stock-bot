from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account

# Create your models here.


class Stock(models.Model):
    shortName = models.CharField(max_length=8, verbose_name=_('Name'))
    fullName = models.CharField(max_length=32, verbose_name=_('Full Name'))
    price = models.FloatField(verbose_name=_('Price'))
    priceRate = models.FloatField(verbose_name=_('Price Rate'))
    lastPrice = models.FloatField(verbose_name=_('Last Price'))
    lastPriceRate = models.FloatField(verbose_name=_('Last Price Rate'))

    def __str__(self):
        return self.fullName

    def __init__(self, *args, **kwargs):
        super(Stock, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')


class UserStock(models.Model):
    user = models.ForeignKey(Account, verbose_name=_(''), on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, verbose_name=_(''), on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name=_(''), default=True)

    def __init__(self, *args, **kwargs):
        super(UserStock, self).__init__(*args, **kwargs)
