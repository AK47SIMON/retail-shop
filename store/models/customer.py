from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255, default="yor address/location")
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, default="your city")
    state = models.CharField(max_length=50, default="county")
    postal_code = models.CharField(max_length=20,default="if you have one")
    country = models.CharField(max_length=50, default="country")

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return False

    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()

