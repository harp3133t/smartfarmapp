# Create your models here.
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Farm(models.Model):
    farm_name=models.CharField(max_length=200)
    def __str__(self):
        return self.farm_name
        
class Growth(models.Model): # 생장 클래스
    farm_name=models.ForeignKey(Farm,on_delete=models.SET_NULL,null=True)
    pub_date=models.DateTimeField('date published')
    flower_part=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 개화부 경경
    growpoint_shape=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 생장점 엽형태
    leaf_size=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 잎 크기
    geodetic_form=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 측지형태
    stem_color=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) #줄기색
    flower_size=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 꽃 크기
    root_form=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) #뿌리형태/냄새
    weekly_growth=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) #주간절간생장
    
    fruit_load=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 착과부하수/m2
    number_bloom=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 개화 꽃잎수
    growpoint_leafcolor=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 생장점 엽색
    flower_shape=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 꽃자루 형태
    flower_distance=models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)]) # 개화부위 거리
    
    def __str__(self):
        return str(self.pub_date)+"["+str(self.farm_name)+"]"+"[Growth]"
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    
class Manage(models.Model): # 환경관리 클래스
    farm_name=models.ForeignKey(Farm,on_delete=models.SET_NULL,null=True)
    pub_date=models.DateTimeField('date published') # 날짜
    temp=models.FloatField(default=20.0) # 24시간평균온도
    DIF_AM=models.FloatField(default=0) # DIF 오전
    DIF_PM=models.FloatField(default=0) # DIF 오후
    D=models.TimeField(default=timezone.now) # 주간시간
    N=models.TimeField(default=timezone.now) # 야간시간
    HD=models.FloatField(default=0) # HD
    Pband=models.FloatField(default=0) # P-Band
    CO=models.IntegerField(default=0) # CO2
    Light=models.IntegerField(default=0) #차광
    WC=models.IntegerField(default=0) # WC
    StartW=models.IntegerField(default=0) # 급액시작
    EndW=models.IntegerField(default=0) # 급액종료
    WEC=models.FloatField(default=0) # 급액EC
    WRatio=models.IntegerField(default=0) # 배액율
    wtype_choice=[('ds','다량소회'),('sd','소량다회')] #급액방식
    WType=models.CharField(max_length=2, choices=wtype_choice)
    RHead=models.BooleanField() # 적심
    RLeaf=models.BooleanField() # 적엽
    RFruit=models.BooleanField() #적과
    Overload=models.FloatField(default=0) # 착과부하
    geo_choice=[('fs','2~3매'),('sc','1~2매'),('no','무')] # 측지확보
    Geodetic=models.CharField(max_length=2, choices=geo_choice)
    LAI=models.FloatField(default=0) # LAI
    acc_light=models.IntegerField(default=0) # 누적광량
    def __str__(self):
        return str(self.pub_date)+"["+str(self.farm_name)+"]"+"[Manage]"
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class Environment(models.Model): #온실 내부환경 클래스
    farm_name=models.ForeignKey(Farm,on_delete=models.SET_NULL,null=True)
    pub_date=models.DateTimeField('date published') # 날짜
    temp=models.FloatField(default=0) #온도
    CO=models.IntegerField(default=0) #CO2
    humidity=models.FloatField(default=0) #습도
    acc_light=models.IntegerField(default=0) #누적광량
    def __str__(self):
        return str(self.pub_date)+"["+str(self.farm_name)+"]"+"[Environment]"
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
