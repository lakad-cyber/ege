import math

def programm(salesed, sale_mnzh):
    file = open('26.txt')
    my_file = [] 
    for line in file:
        my_file.append(line)
    
    my_file = [int(i.rstrip()) for i in my_file]
    
    count = my_file[0]
    
    del my_file[0]
    
    not_saled = []
    
    all_items = sorted(my_file)
    
    for item in all_items:
        if item <= salesed:
            not_saled.append(item)
    
    for i in range(len(not_saled)):
        del all_items[0]
    
    with_sales = []
    
    for i in range(len(all_items) // 2):
        with_sales.append(all_items[i])
        
    for i in range(len(with_sales)):
        del all_items[0]
        
        
    all_summ = sum(not_saled) + sum(all_items) + (sum(with_sales) * sale_mnzh)
    max_with_sale = with_sales[-1]
    
    print(math.ceil(all_summ))
    print(max_with_sale)
    
    
salesed = 150
sale_mnzh = 0.8
programm(salesed, sale_mnzh)
