import random
import string
from django.db import models

def generate_random_code(size, chars=string.ascii_lowercase + string.digits + "-" + "_"):
    return "".join(random.choice(chars) for element in range(size))

def is_unique(shortCode, instance):   
    addressModel = instance.__class__
    alreadyExists = addressModel.objects.filter(short=shortCode).exists()
    if alreadyExists:
        return False
    #else:    
    return True

def get_short_code(size, instance):
    #First, we check that there are no other Addresses with the same short code:
    shortCode = generate_random_code(size)
    isUnique = is_unique(shortCode, instance)
    while not isUnique:
        shortCode = generate_random_code(size)
        isUnique = is_unique(shortCode)
    
    return shortCode

def get_counter(code):
    counter = Counter.objects.filter(addressId=Address.objects.filter(short=code)[0])[0]
    return counter
