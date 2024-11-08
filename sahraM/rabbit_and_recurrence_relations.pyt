n = int(input("Number of months: " ))
k = int(input("k rabbit pairs: " ))

#Fn = Fn-1 + k (Fn-2)
def fibonacci_seq (n,k):
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    
    fn_minus_2 = 1
    fn_minus_1 = 1
    
    for i in range (3,(n+1)):
        fn = fn_minus_1 + k *(fn_minus_2)
        print(f"F({i}) = {fn}")
        
        fn_minus_2 = fn_minus_1
        fn_minus_1 = fn
    
    return fn

result = fibonacci_seq(n, k)
print(f"The value of F({n}) is {result}")


