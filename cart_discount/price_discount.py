def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    try:
        item_prices.sort()
        if len(item_prices) >= 3:
            if item_prices[0] >= 0:
                return item_prices[0]
            else:
                raise Exception('Prices must not be negative.')
        else:
            return 0
    except:
        raise Exception('Enter a valid array of number prices')


if __name__ == '__main__':
    main()