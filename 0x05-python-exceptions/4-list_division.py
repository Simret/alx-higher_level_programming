#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    d = 0.0
    f = 0
    for i in range(0, list_length):
        d = 0
        try:
            d = my_list_1[i] / my_list_2[i]
            f = 1
        except ZeroDivisionError:
            print("division by 0")
            a += [0]
        except (TypeError):
            print("wrong type")
            a += [0]
        except IndexError:
            print("out of range")
            a += [0]
        finally:
            if f == 1:
                f = 0
                a += [d]
    return a
