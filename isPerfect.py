from functools import reduce

def is_perfect(num):
    new_list = [item for item in range(num)]
    filter_list = [item for item in range(1, num) if num % item == 0]

    def do_sum(x1, x2): return x1 + x2
    reduce_list = reduce(do_sum, filter_list)

    def add_by_1(item): return item + 1
    map_list = list(map(add_by_1, new_list))

    print(new_list,map_list,filter_list,reduce_list,num)
    return sum(filter_list) == num
    
print(is_perfect(28))
print(is_perfect(14))
print(is_perfect(6))
