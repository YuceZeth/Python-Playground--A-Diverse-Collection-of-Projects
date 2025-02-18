def toplama(s1, s2):
    return s1 + s2


def silme(s1, s2):
    return s1 - s2


def carpma(s1, s2):
    return s1 * s2


def bolme(s1, s2):
    try:
        return s1 / s2
    except ZeroDivisionError:
        print("Sayı Sıfıra Bölünmez...")
