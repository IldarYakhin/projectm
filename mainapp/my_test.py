import random

from mainapp.models import License


def get_list_of_existed_licenses(self):
    """
    :return: list of codes from db
    """
    result = License.objects.filter('code')
    return result

def generator(qty, duration):  # 10 chars from ABCEFGHKLMNPRSTUVWXYZ23456789
    """
    get needed qty of Licenses and
    :return:
    dict {'License': duration}
    """
    qty, duration = int(qty), int(duration)
    if qty > 50:
        return 'incorrect qty'
    chars = 'ABCEFGHKLMNPRSTUVWXYZ23456789'
    existed = License.objects.all()
    counter = qty
    output = {}
    while len(output) < qty:
        example = ''.join(random.sample(chars, 10))
        if example in output or example in existed:
            print('exist')
            continue
        else:
            output[example] = duration
            counter -= 1
    return output


def get_id_by_code(code):
    """
    get License code and return idLicense
    :return:
    """
    pass

def increase_duration(pk):
    """
    get License № and period in days
    like in example and increase duration on this days

    ABCEFGHKLMNPRSTUVWXYZ23456789 10
    ABCEFGHKLMNPRSTUVWXYZ23456789 5
    ABCEFGHKLMNPRSTUVWXYZ23456789 90
    etc

    :return:
    idLicense --> duration + days
    """

    pk = pk
    pass


ls = ['LMNP565656', 'ABCD123457','ABCD123456']

data = "4UPCEYG8F2 24 5FULWXCK3B 24 MH8GYR7NUX 24 U7LFWAP8VG 24 ECMK85AVRZ 24"

def raspars(data):
    prom = [el for el in data.split()]
    res = {}
    el, k = 0, 1
    for i in range(int((len(prom)/2))):
        res[prom[el]] = prom[k]
        el += 2
        k += 2
    return res
















