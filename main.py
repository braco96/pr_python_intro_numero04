# -*- coding: utf-8 -*-
import re
def contar_palabras(s):
    palabras = re.findall(r"\w+", s.lower())
    d = {}
    for p in palabras:
        d[p] = d.get(p,0)+1
    return d

