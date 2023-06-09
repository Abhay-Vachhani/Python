class Amazon:
    def add_product(self, *args): # Take all args
        length = len(args)
        if length == 0:
            print('0 Args supply')
        elif length == 1:
            print('1 Args supply')
            print(args[0])
        elif length == 2:
            print('2 Args supply')
            print(args[0], args[1], sep=', ')
        else:
            print('More than 2 args\n')
            # a, b = 10, 20
            # [
            #     (0, 'Laptop'),
            #     (1, 'PC'),
            #     (2, 'Calc'),
            # ]
            for i, pro in zip(range(len(args)), args): 
                print('Id: ', i, ', Name: ', pro, sep='')
            
            # for elem in zip(range(len(args)), args): 
            #     print('Id: ', elem[0], ', Name: ', elem[1], sep='')


    
    # def add_product(self, first, second, *args): # Take all args but two compulsory
    #     print('Products')

amazon = Amazon()
print('- - - - - - - - - - - - - - - - - - - -')
amazon.add_product()
print('- - - - - - - - - - - - - - - - - - - -')
amazon.add_product('Laptop')
print('- - - - - - - - - - - - - - - - - - - -')
amazon.add_product('Laptop', 'PC')
print('- - - - - - - - - - - - - - - - - - - -')
amazon.add_product('Laptop', 'PC', 'Calc')
print('- - - - - - - - - - - - - - - - - - - -')