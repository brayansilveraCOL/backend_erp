# Model
from erp_backend.inventorys.models import Movement


def generate_code():
    initial = 'M-'
    ult_movement_pk = Movement.objects.filter(state=True).last()
    increment = ult_movement_pk.pk + 1
    new = str(increment)
    new_code = initial + new
    return new_code
