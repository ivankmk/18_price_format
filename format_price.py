import sys


def format_price(price):
    price = str(price)
    try:
        if price.count('.') == 1:
            if int(price.split('.')[1]) == 0:
                return '{0:,}'.format(round(float(price))).replace(',', ' ')
            else:
                return '{0:,}'.format(float(price)).replace(',', ' ')
        elif price.count('.') == 0:
            return '{0:,}'.format(int(price)).replace(',', ' ')
        else:
            return None
    except ValueError:
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
