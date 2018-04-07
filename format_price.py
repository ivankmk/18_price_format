import sys


def format_price(price):
    try:
        price = float(price)
        if price.is_integer():
            return '{0:,}'.format(round(float(price))).replace(',', ' ')
        else:
            return '{0:,}'.format(float(price)).replace(',', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    try:
        price = sys.argv[1]
    except IndexError:
        print('Please, insert the number to apply formatting.')
    if format_price(price) is not None:
        print(format_price(price))
    else:
        print('Please, use only numbers.')
