"""
-------------------------------------------------------
Functions
-------------------------------------------------------
"""
# Imports

# Constants

# 1


def get_brightness(wattage):
    """
    -------------------------------------------------------
    Converts watts to lumens for lightbulbs.
    Use: brightness = get_brightness(wattage)
    -------------------------------------------------------
    Parameters:
        wattage - wattage in watts (int >= 0)
    Returns:
        brightness - brightness in lumens (int)
    -------------------------------------------------------
    """

    if wattage == 15:
        brightness = 'Brightness: 125 lumens'
    elif wattage == 25:
        brightness = 'Brightness: 215 lumens'
    elif wattage == 40:
        brightness = 'Brightness: 500 lumens'
    elif wattage == 60:
        brightness = 'Brightness: 880 lumens'
    elif wattage == 75:
        brightness = 'Brightness: 1000 lumens'
    elif wattage == 100:
        brightness = 'Brightness: 1675 lumens'
    else:
        brightness = 'Invalid wattage'

    return brightness

# 2---------------------------------------------------------------------------------


def payment(principal, interest, months):
    """
    -------------------------------------------------------
    Calculates a monthly payment on a loan.
    Use: monthly_payment = payment(principal, interest, months)
    -------------------------------------------------------
    Parameters:
        principal - amount borrowed in $ (float > 0)
        interest - yearly interest rate on loan (float > 0)
        months - number of months for the loan (int > 0)
    Returns:
        monthly_payment - monthly payment on loan in $ (float)
    -------------------------------------------------------
    """
    interest = interest / 100

    monthly_payment = ((interest / 12) * principal) / \
        (1 - ((1 + (interest / 12)) ** -months))

    return monthly_payment

# 3-------------------------------------------------------------------------------


def get_total_change(n, d, q, l, t):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins. Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: tv = get_total_change(n, d, q, l, t)
    -------------------------------------------------------
    Parameters:
        n - number of nickels (int >= 0)
        d - number of dimes (int >= 0)
        q - number of quarters (int >= 0)
        l - number of loonies (int >= 0)
        t - number of toonies (int >= 0)
    Returns:
        tv - total value of coins
    -------------------------------------------------------
    """

    n = n * 0.05

    d = d * .1

    q = q * .25

    l = l * 1

    t = t * 2

    tv = n + d + q + l + t

    return tv

# 4-------------------------------------------------------------------------------


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """

    num = num1 * num2
    den = den1 * den2
    product = num / den

    return num, den, product

# 5---------------------------------------------------------------------------------


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns total_seconds in different formats. Results are
    rounded down to the nearest day, hour, minute.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    days = seconds // 86400

    hours = seconds // 3600

    minutes = seconds // 60

    return days, hours, minutes

# 6----------------------------------------------------------------------------------


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts initial seconds into days, hours, minutes, and seconds.    
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """

    days = initial_seconds // 86400

    hours = (initial_seconds % 86400) // 3600

    minutes = (initial_seconds % 3600) // 60

    seconds = initial_seconds % 60

    return days, hours, minutes, seconds

# 7-------------------------------------------------------------------------------


def wall_area(width, height):
    """
    -------------------------------------------------------
    Calculates rectangular wall area on a painting job.
    Use: area = wall_area(width, height)
    -------------------------------------------------------
    Parameters:
        width - width of wall (ft) (int > 0)
        height - height of wall (ft) (int > 0)
    Returns:
        area - area of wall (sq ft) (int)
    -------------------------------------------------------
    """
    area = width * height

    return area


def paint_required(area, standard_area):
    """
    -------------------------------------------------------
    Calculates paint required on a painting job. Resulting gallons
    are rounded up.
    Use: total = paint_required(area, standard_area)
    -------------------------------------------------------
    Parameters:
        area - area of wall (sq ft) (int > 0)
        standard_area - area covered by 1 gallon of paint (sq ft) (int > 0)
    Returns:
        total - gallons of paint required (int)
    -------------------------------------------------------
    """
    total = (standard_area // area) + 1
    return total


def hours_required(area, area_per_hour):
    """
    -------------------------------------------------------
    Calculates hours required on a painting job. Resulting hours are
    rounded up.
    Use: hours = hours_required(area, area_per_hour)
    -------------------------------------------------------
    Parameters:
        area - area of wall (sq ft) (int > 0)
        area_per_hour - area painted per hour (int > 0)
    Returns:
        hours - hours required to paint area (int)
    -------------------------------------------------------
    """

    hours = (area // area_per_hour) + 1
    return hours


def paint_cost(total_paint, cost):
    """
    -------------------------------------------------------
    Calculates paint cost on a painting job.
    Use: pc = paint_cost(total_paint, cost)
    -------------------------------------------------------
    Parameters:
        total_paint - paint required (gallons) (int > 0)
        cost - cost of paint ($/gallon) (float > 0)
    Returns:
        pc - total paint cost (float)
    -------------------------------------------------------
    """

    pc = total_paint * cost
    return pc
