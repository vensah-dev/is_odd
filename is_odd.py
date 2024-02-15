def odd(number, mode="normal"):
    if number % 2 == 1:
        odd = True
    else:
        odd = False

    if mode.lower() == "normal":
        return odd
    elif mode.lower() == "inverse":
        return not odd
    elif mode.lower() == "data":
        return number, odd, number % 2


def is_prime(number, mode="normal"):
    prime = True
    factors = []

    if number == 1:
        prime = False
    elif number > 1:
        for i in range(2, number):

            if mode == "data":
                if (number % i) == 0:
                    factors.append(i)
                    prime = False
            else:
                if (number % i) == 0:
                    factors.append(i)
                    prime = False
                    break;

    if mode.lower() == "normal":
        return prime
    elif mode.lower() == "inverse":
        return not prime
    elif mode.lower() == "data":
        return number, prime, factors

class is_odd:
    def __init__(self, number):
        self.number = number

    def odd(self, mode="normal"):
        return odd(self.number, mode)

    def even(self, mode="normal"):
        if mode == "inverse":
            return odd(self.number)
        elif mode == "normal":
            return odd(self.number, "inverse")
        else:
            return odd(self.number, mode)

    def is_prime(self, mode="normal"):
        return is_prime(self.number, mode)
