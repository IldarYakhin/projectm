import random

from mainapp.models import License


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


def raspars(data):
    prom = [el for el in data.split()]
    res = {}
    el, k = 0, 1
    for i in range(int((len(prom)/2))):
        res[prom[el]] = prom[k]
        el += 2
        k += 2
    return res
















