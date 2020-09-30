import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","my_first_project.settings")
# above two lines are for configuring the projec for the settings

import django
django.setup()
#above line would setup and configure the project settings


import random
from basic_app.models import AccessRecord,WebPage,Topic
from faker import Faker # This is just an external Lib. Nothing to do with python

fakegen = Faker()
topics = ["Search","Social","News"]

def add_topic():
    """
    This functions is to add topics
    """
    t = Topic.objects.get_or_create(Top_name=random.choice(topics))[0] #This will retrieve the topic, if it already exists in the model or it will create, if not
    t.save()
    return t

def populate(N):
    for i in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date=fakegen.date()

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        access = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=="__main__":
    populate(10)
