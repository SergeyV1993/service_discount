from django.db import models
from datetime import *


class DiscountCart(models.Model):
    cart = models.IntegerField(null=True, blank=True, db_index=True)
    code = models.CharField(max_length=20, blank=True, null=True, default=None, db_index=True)
    valid_date_start = models.DateTimeField(auto_now_add=True, auto_now=False)
    valid_date_end = models.DateTimeField(default=datetime.now(timezone.utc) + timedelta(days=90))
    nominal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.code
        except Exception as error:
            print(error)
