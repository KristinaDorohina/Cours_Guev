from collections import OrderedDict
def custom_sort(order_dict, by_values=False):
    if by_values == True:
        for key, v in sorted(order_dict.items(), key=lambda item: item[1]):
            order_dict.move_to_end(key, last=False)
    elif by_values == False:
        for key in sorted(order_dict):
            order_dict.move_to_end(key)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())