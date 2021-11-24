from django.db    import models

from core.models  import TimeStampModel
from users.models import User

class Car(TimeStampModel) :
    model = models.CharField(max_length=50)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta :    
        db_table = 'cars'

class Trim(TimeStampModel) :
    name = models.CharField(max_length=50)
    car  = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta :
        db_table = 'trims'

class Tire(TimeStampModel) :
    position     = models.CharField(max_length=20)
    name         = models.CharField(max_length=50)
    width        = models.IntegerField()
    aspect_ratio = models.IntegerField()
    wheel_size   = models.IntegerField()
    trim         = models.ForeignKey(Trim, on_delete=models.CASCADE)

    class Meta :
        db_table = 'tires'