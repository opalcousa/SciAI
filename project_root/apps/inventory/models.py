from djongo import models

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    density = models.FloatField()
    price = models.FloatField()
    additional_info = models.TextField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.raw_material.name} - {self.quantity}"