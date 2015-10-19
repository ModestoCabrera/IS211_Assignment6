#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temperature Conversions"""


def celcius_to_kelvin(celcius):
    """
    Args:
        conversion (float) : Celcius to Kelvin conversion.

    Returns:
        conversion (float) : Returns Kelvin result.

    Examples:
        >>> celcius_to_kelvin()
        >>>
    """
    conversion = float(celcius) + float('273.15')
    return round(conversion, 3)


def celcius_to_fahrenheit(celcius):
    """
    Args:
        conversion (float) : Celcius to Fahrenheit conversion.

    Returns:
        conversion (float) : Returns Fahrenheit result.

    Examples:
        >>> celcius_to_fahrenheit()
        >>>
    """
    conversion = (((float(celcius)* 9) / 5) + 32)
    return conversion


def fahrenheit_to_celcius(fahrenheit):
    """
    Args:
        conversion (float) : Fahrenheit to Celcius conversion.

    Returns:
        conversion (float) : Returns Celcius result.

    Examples:
        >>> fahrenheit_to_celcius()
        >>>
    """
    conversion = ((float(fahrenheit) - 32) * 5) / 9
    return round(conversion, 3)


def fahrenheit_to_kelvin(fahrenheit):
    """
    Args:
        conversion (float) : Fahrenheit to Kelvin conversion.

    Returns:
        conversion (float) : Returns Kelvin result.

    Examples:
        >>> fahrenheit_to_kelvin()
        >>>
    """
    conversion = ((float(fahrenheit) - 32) * 5) / 9
    conversion += float(273.15)
    return round(conversion, 3)



def kelvin_to_celcius(kelvin):
    """
    Args:
        conversion (float) : Kelvin to Celcius conversion.

    Returns:
        conversion (float) : Returns Celcius results.

    Examples:
        >>> kelvin_to_celcius()
        >>>
    """
    conversion = float(kelvin) - float('273.15')
    return round(conversion, 3)


def kelvin_to_fahrenheit(kelvin):
    """
    Args:
        conversion (float) : Kelvin to Fahrenheit conversion.

    Returns:
        conversion (float) : Returns Fahrenheit result.

    Examples:
        >>> kelvin_to_fahrenheit()
        >>>
    """
    conversion = (((float(kelvin) - float('273.15')) / 5) * 9) + 32
    return round(conversion, 3)
