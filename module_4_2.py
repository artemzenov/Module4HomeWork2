def test_function():
    
    def inner_function():
        print(f'Я в области видимости {test_function.__name__}')
    
    inner_function()    


# inner_function() #Будет ошибка,
                   #так как она находится в области видимости 
                   #объемлющей функции test_function
test_function()
