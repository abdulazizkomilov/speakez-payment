from django.db import models


class Order(models.Model):
    """Order model"""

    user_id = models.BigIntegerField()
    total = models.BigIntegerField()
    payment_method = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - User: {self.user_id} - Total: {self.total}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-created_at"]
