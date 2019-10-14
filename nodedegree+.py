import numpy as np
import matplotlib.pyplot as plt
import os
import json
degree = []
value = []
with open('degree+.json', "r") as c:
    dm = json.load(c)
    for i in dm:
        degree.append(i)
        value.append(dm[i])
    print(degree,value)