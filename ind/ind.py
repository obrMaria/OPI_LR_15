#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator(func):
    azbuka = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е':
              '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
              'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с':
              '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч':
              '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э':
              '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-···-'}

    def key(v, dict):
        for key, value in dict.items():
            if v == key:
                return value

    def azbuka_morze(*args):
        a = ''
        value = func(*args)
        for i in value:
            if i in azbuka.keys():
                a += key(i, azbuka)
        return a

    return azbuka_morze


@decorator
def strochka(strochka):
    strochka = strochka.lower()
    strochka = ' '.join(strochka.split())
    return strochka


if __name__ == '__main__':
    print(strochka("привет"))
