import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_contar_palabras_basico():
    s = "Hola hola, mundo mundo mundo!"
    d = mod.contar_palabras(s)
    assert d["hola"] == 2
    assert d["mundo"] == 3
