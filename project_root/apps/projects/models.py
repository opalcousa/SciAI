from djongo import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    formulations = models.ArrayModelField(
        model_container='Formulation',
        model_form_class='FormulationForm'
    )

    def __str__(self):
        return self.name

class Formulation(models.Model):
    name = models.CharField(max_length=200)
    raw_materials = models.ArrayModelField(
        model_container='RawMaterial',
        model_form_class='RawMaterialForm'
    )
    total_volume = models.FloatField()
    total_mass = models.FloatField()

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=200)
    density = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name