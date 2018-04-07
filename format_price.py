import sys
import re


def format_price(price):
    zero_after_dot = re.compile("[0-9]*[.]?[0]*\Z")
    one_dot = re.compile("[0-9]*[.]?[0-9]*\Z")
    price = str(price)

    if bool(one_dot.match(price)):
        if bool(zero_after_dot.match(price)):
            return '{0:,}'.format(round(float(price))).replace(',', ' ')
        else:
            return '{0:,}'.format(float(price)).replace(',', ' ')
    else:
        return None


if __name__ == '__main__':
    try:
        price = sys.argv[1]
        if format_price(price) is not None:
            print(format_price(price))
        else:
            print('Please, use only numbers.')

    except IndexError:
        print('Please, insert the number to apply formatting.')
