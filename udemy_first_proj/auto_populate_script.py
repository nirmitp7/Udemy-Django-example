import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemy_first_proj.settings')

import django
django.setup()

##FAKE POP SCRIPT 

import random
from firstApp.models import Topic, Webpage, AccessRecord, User
from faker import Faker

fakegen = Faker()


topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        top = add_topic()

        # Create Fake Data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_first_nm = fakegen.name()
        fake_last_nm = fakegen.name()
        fake_email = fakegen.email()


        # Create new Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

        usr = User.objects.get_or_create(first_nm=fake_first_nm,last_nm=fake_last_nm,email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
