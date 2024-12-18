import os; os.system("cls")
import math

def napravi_trigonometrijski_rjecnik(n_in_deg):
    n_in_rad = math.radians(n_in_deg)
    ret_val = {"sin":math.sin(n_in_rad), "cos":math.cos(n_in_rad)}
    return ret_val

trig_val = napravi_trigonometrijski_rjecnik(60)
print("sin:", trig_val["sin"])
print("cos:", trig_val["cos"])
