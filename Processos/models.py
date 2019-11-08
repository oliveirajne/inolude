from django.db import models

class Processo(models.Model):

    nu_Processo = models.BigIntegerField()
    dt_Processo = models.CharField(max_length=45)
    ar_Processo = models.CharField(max_length=45)
    vl_Processo = models.DecimalField(max_digits=9, decimal_places=2)
    cod_TipoProcesso = models.IntegerField()
    cod_Materia = models.IntegerField()
    cod_Forma = models.IntegerField()


