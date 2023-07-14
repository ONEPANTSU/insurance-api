from tortoise import fields, models


class Insurance_History(models.Model):
    id = fields.IntField(pk=True, autoincrement=True)
    declared_price = fields.FloatField()
    date = fields.DateField()
    cargo_type = fields.TextField()
    rate = fields.FloatField()
    insurance_price = fields.FloatField()
