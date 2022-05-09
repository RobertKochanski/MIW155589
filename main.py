# punkt w 14-wymiarowej przestrzeni
# w głowie mamy ograniczenie do 3 wymiarów, żyjemy w 4,
# przewstrzeń metryczna, potrzebna para zbiór i element
# d - odległość
# 1. d(a,b)= 0 => a=b
# 2. d(a,b) = d(b,a)
# 3. if d(a,b) + d(b,c) >= d(a,c) nierówność trókąta
# jeżeli coś spełnia te warunki to jest to metryka, a zbiór przestrzenią metryczną
# żeby obliczyć odległość dwóch pkt od siebie korzystamy z twierdzenia pitagorasa
# c = pierw(a^2 + b^2)
# (Ax - Bx)^2 + (Ay-By)^2 i im więcej wymiarów tym więcej nawiasów
# ^rzutowanie na oś x ^rzutowanie na OY

import copy
import math
import random
from collections import defaultdict
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

