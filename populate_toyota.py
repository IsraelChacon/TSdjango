import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Tdjango.settings')

import django
django.setup()

from mi_app.models import ToyotaLegacy
from faker import Faker

faker_generator = Faker()

def populate(N=5):
    for entry in range(N):
        fake_primer_nombre = faker_generator.first_name()
        fake_apellido = faker_generator.last_name()
        fake_email = faker_generator.email()
        fake_telefono = faker_generator.phone_number()

        # Crear registro falso
        toyotaLegacy = ToyotaLegacy.objects.get_or_create(primer_nombre = fake_primer_nombre, apellido = fake_apellido, email = fake_email, telefono = fake_telefono)[0]

if __name__ == '__main__':
    print('Comenso a poblar')
    populate(30)
    print('Se acabo de poblar')