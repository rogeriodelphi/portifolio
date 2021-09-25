from django.db import models


class Divisao(models.Model):
    codigo = models.CharField(max_length=1, null=False, blank=False, verbose_name='Código')
    descricao = models.CharField(max_length=50)

    class Meta:
        db_table = 'Divisao'
        ordering = ['codigo']
        verbose_name = 'Divisão'
        verbose_name_plural = 'Divisões'

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.descricao)


class Grupo(models.Model):
    codigo = models.CharField(max_length=3, null=False, blank=False, verbose_name='Código')
    divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE, verbose_name='Divisão')
    descricao = models.CharField(max_length=110)

    class Meta:
        db_table = 'grupo'
        ordering = ['divisao']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return '{}-{}-{}'.format(self.codigo, self.divisao, self.descricao)


class SubGrupo(models.Model):
    codigo = models.CharField(max_length=6, null=False, blank=False, verbose_name='Código')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo')
    descricao = models.CharField(max_length=50)

    class Meta:
        db_table = 'subgrupo'
        ordering = ['grupo']
        verbose_name = 'SubGrupo'
        verbose_name_plural = 'SubGrupos'

    def __str__(self):
        return '{} - {}'.format(self.grupo, self.descricao)

class Unidade_Medida(models.Model):
    und_medida_desc = models.CharField(max_length=255, verbose_name='Unidade de Medida')

    class Meta:
        db_table = 'unidade_medida'
        ordering = ['und_medida_desc']
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.und_medida_desc


class Tipologia(models.Model):
    codigo = models.CharField(max_length=6, null=False, blank=False, verbose_name='Código')
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, verbose_name='Código e Descrição do SubGrupo')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    und_medida_desc = models.ForeignKey(Unidade_Medida, on_delete=models.CASCADE, verbose_name='Unidade de Medida')
    # und_medida_valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Unidade de Medida(Valor)')
    p_poluidor = models.CharField(max_length=1, verbose_name='Potencial Poluidor')
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, verbose_name='SubGrupo')
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipologia'
        ordering = ['subgrupo']
        verbose_name = 'Tipologia'
        verbose_name_plural = 'Tipologias'

    def __str__(self):
        return self.codigo