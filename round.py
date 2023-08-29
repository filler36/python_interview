from decimal import Decimal

'''
   Syntax: round(number, number_of_digits)
   Parameters: 
   number: number to be rounded
   number_of_digits (Optional): number of digits up to which the given number is to be rounded.
'''

'''
round(x.5) returns the nearest EVEN integer number. 
    round(-2.5) -> -2
    round(-1.5) -> -2
    round(-0.5) -> 0
    round(0.5) -> 0
    round(1.5) -> 2
    round(2.5) -> 2
    round(3.5) -> 4
    round(4.5) -> 4
    round(5.5) -> 6
    round(6.5) -> 6
    round(7.5) -> 8
    round(8.5) -> 8
    round(9.5) -> 10
    round(10.5) -> 10
    round(11.5) -> 12
'''

'''
    round(2.675, 2) -> 2.67    BECAUSE  2.675 float is 2.67499999999999982236 under the hood. You can check it with "{:.20f}".format(2.675)
    
    If you need precision for such calculations you can use Decimal:
    float(round(Decimal('2.675'), 2)) -> 2.68
'''
