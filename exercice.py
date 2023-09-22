#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a ** 2


def average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    decimal_degrees = (angle_degs + (angle_mins + angle_secs / 60) / 60)
    return (decimal_degrees * math.pi / 180)

def to_degrees(angle_rads: float) -> tuple:
    degrees = (180 / math.pi) * angle_rads
    angle_degs= int(degrees)
    if angle_degs < 0:
        decimal_part = angle_degs - degrees
    else :
        decimal_part = degrees - angle_degs
    degrees_2 = decimal_part * 60
    angles_min = int(degrees_2)
    degree_3 = degrees_2 - angles_min 
    angles_sec = degree_3 * 60
    return angle_degs, angles_min, angles_sec

def to_celsius(temperature: float) -> float:
    deg_celsius = (temperature - 32) / (9 / 5)
    return deg_celsius


def to_farenheit(temperature: float) -> float:
    deg_farhenheit = 32 + (1.8 * temperature)
    return deg_farhenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
