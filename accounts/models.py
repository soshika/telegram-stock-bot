from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class AccountManager(models.Manager):
    def get_queryset(self):
        return super(AccountManager, self).get_queryset()

    def get_account(self):
        return self.get_queryset().order_by('-id')

    def get_account_by_status(self, active):
        return self.get_queryset().filter(status=active)


class Account(models.Model):
    firstName = models.CharField(max_length=32, verbose_name=_('First Name'))
    lastName = models.CharField(max_length=32, verbose_name=_('Last Name'), blank=True)
    username = models.CharField(max_length=32, verbose_name=_('Username'))
    dateRegistered = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Registered'))
    commission = models.FloatField(default=0.0, verbose_name=_('Commission'))
    status = models.BooleanField(default=False, verbose_name=_('Status'))

    objects = AccountManager()

    def set_date(self, new_date_registered):
        self.dateRegistered = new_date_registered
        self.save()

    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
