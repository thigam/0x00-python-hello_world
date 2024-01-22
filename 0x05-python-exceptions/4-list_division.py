#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list=[0] * list_length
    counter = 0
    while True:
        if list_length == 0:
            break
        try:
            new_list[counter] = my_list_1[counter] / my_list_2[counter]
        except (ValueError, TypeError):
            print("wrong type")
            new_list[counter] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[counter] = 0
        except IndexError:
            print("out of range")
            new_list[counter] = 0
        finally:
            counter += 1
            list_length -= 1
    return new_list
