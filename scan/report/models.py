from django.db import models

# Create your models here.

#Надо сделать чтобы были каждый класс для каждой метрики av ac au c n
class CVSS2(models.Model):
    base_score = models.CharField('Базовая метрика', max_length= 200)
    AV = models.CharField('Получение доступа', max_length= 200)
    AC = models.CharField('Сложность получение доступа', max_length= 200)
    AU = models.CharField('Показатель аутонтефикации', max_length= 200)
    C = models.CharField('Влияние на конфиденциальность', max_length= 200)
    I = models.CharField('Влияние на целостность', max_length= 200)
    A = models.CharField('Влияние на доступность', max_length= 200)



class CVSS3(models.Model):
    base_score = models.CharField('Базовая метрика', max_length= 200)
    time_score = models.CharField('Временная метрика', max_length= 300)

    AV = models.CharField('Получение доступа', max_length= 200)
    AC = models.CharField('Сложность получение доступа', max_length= 200)
    PR = models.CharField('Взаимодействие с пользователем', max_length= 200)
    UI = models.CharField('Требуемые привилегии', max_length= 200)
    S = models.CharField('Объем', max_length= 200)
    C = models.CharField('Влияние на конфиденциальность', max_length= 200)
    I = models.CharField('Влияние на целостность', max_length= 200)
    A = models.CharField('Влияние на доступность', max_length= 200)
    E = models.CharField('Доступность эксплойда', max_length= 200)
    RL = models.CharField('Уровень исправления', max_length= 200)
    RC = models.CharField('Отчет о достоверности', max_length= 200)


class Vulnerability(models.Model):
    name = models.CharField('Название уязвимости', max_length= 200)
    short_description = models.TextField('Краткое описание')
    description = models.TextField('Описание')
    edit = models.TextField('Как исправить')
    # CVE = models.CharField('CVE', max_length= 50)

    cvss2 = models.ForeignKey(CVSS2, on_delete= models.CASCADE)
    cvss3 = models.ForeignKey(CVSS3, on_delete= models.CASCADE)


class Node(models.Model):
    name = models.CharField('Название узла', max_length= 200)


TCP_UDP = (
    ('tcp', 'TCP'),
    ('udp', 'UDP'),
)


class Group_vulnerability(models.Model):
    vulnerability = models.ManyToManyField(Vulnerability)
    node = models.ForeignKey(Node, on_delete= models.CASCADE)

    port = models.IntegerField('Порт')
    tcp_udp = models.CharField(max_length=3, choices=TCP_UDP, default='tcp')
    # tcp_udp =  models.IntegerField('Транспортный протокол', max_length= 100000)
    name_protocol = models.CharField('Название протокола', max_length=200)

#
# COLOR_CHOICES = (     #https://stackoverflow.com/questions/31130706/dropdown-in-django-model
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# )
#
# class MyModel(models.Model):
#   color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
#
# class MyModelForm(ModelForm):
#   class Meta:
#       model = MyModel
#       fields = ['color']
#
# class CreateMyModelView(CreateView):
#   model = MyModel
#   form_class = MyModelForm
#   template_name = 'myapp/template.html'
#   success_url = 'myapp/success.html'
#
#   < form
#   action = ""
#   method = "post" > { % csrf_token %}
#   {{form.as_p}}
#   < input
#   type = "submit"
#   value = "Create" / >
#
# < / form > b = n.group_vulnerability_set.all()