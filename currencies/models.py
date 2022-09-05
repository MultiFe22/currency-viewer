from django.db import models

class Currency(models.Model):
    # the currency has a name, a date, and a value, only one register per date
    name = models.CharField(max_length=3)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.date} {self.value}'
    
    class Meta:
        unique_together = ('name', 'date')
        ordering = ['date']
    
    
