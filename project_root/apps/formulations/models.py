from djongo import models

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    density = models.FloatField()
    price = models.FloatField()

    class Meta:
        abstract = True

class Formulation(models.Model):
    name = models.CharField(max_length=255)
    raw_materials = models.ArrayModelField(
        model_container=RawMaterial,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total_volume(self):
        total_volume = sum([material.density for material in self.raw_materials])
        return total_volume

    def calculate_total_mass(self):
        total_mass = sum([material.density * material.price for material in self.raw_materials])
        return total_mass

    def __str__(self):
        return self.name