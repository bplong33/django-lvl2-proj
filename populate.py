import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','lvl2_proj.settings')

import django
django.setup()

import random
from faker import Faker
from accounts.models import User

fakegen = Faker()

DOMAINS = ['gmail.com', 'aol.com', 'yahoo.com']

def populate(n=10):
    for user in range(n):
        first = fakegen.first_name()
        last = fakegen.last_name()
        email = f"{first[0]}{last}@{random.choice(DOMAINS)}".lower()
        
        new_user = User.objects.get_or_create(fname=first, lname=last, email=email)

if __name__ == "__main__":
    print("Populating users table")
    populate(n=50)
    print("Finished populating")