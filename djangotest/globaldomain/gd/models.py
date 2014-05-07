from django.db import models

# Create your models here.
class resultdb(models.Model):
	Time=models.DateTimeField()
	Ip=models.CharField(max_length=15)
	Domain=models.CharField(max_length=50)
	Result=models.CharField(max_length=100)
	Usetime=models.CharField(max_length=5)
	def __unicode__(self):
		return '%s %s %s %s %s ' % (self.Time,self.Ip,self.Domain,self.Result,self.Usetime)
