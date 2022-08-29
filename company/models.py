from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator,MaxLengthValidator

class Industry_type(models.Model):
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class Company(models.Model):
    cname = models.CharField(max_length=200,)
    ownername = models.CharField(max_length=200,)
    address = models.CharField(max_length=200,)
    email= models.EmailField(blank=True, null=True, validators=[MinLengthValidator(0), MaxLengthValidator(20)])
    contact=models.IntegerField(blank=True, null=True)
    Industry_type = models.ForeignKey(Industry_type, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        if self.address:
            return f"{self.cname} ({self.address})"
        return self.cname
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                
                if field.verbose_name != 'industry_type' 
                
                else 
                    (field.verbose_name, 
                    Industry_type.objects.get(pk=field.value_from_object(self)).name)
                
                for field in self.__class__._meta.fields[1:]
            ]

    


