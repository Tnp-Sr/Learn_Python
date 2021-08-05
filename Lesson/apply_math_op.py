def leap_year(year) :
    if year % 4 == 0 :
        return True # True-False
    else :
       return False 
       
def leap_year_bdd(year) :
    if year % 4 == 3 :
        return True # True-False
    else :
       return False 
print("leap year")
print(leap_year(2020))
print(leap_year_bdd(2563))

def is_even(n) :
    #if n%2 == 0 :
    #    return True
    #else : 
    #    return False
    return True if n%2 == 0 else False 

def is_odd(n) :
    #if n%2 == 1 :
    #    return True
    #else : 
    #    return False    
    return not(is_even(n)) # not = ! in C
print("\neven/odd")
print(is_even(5))    
print(is_odd(5))   


def promotion(p_come,p_pay,per_head,come) :
    return (come//p_come)*(p_pay*per_head)+(come-p_come)*per_head

# pro : come 4 pay 2
# real : come 5
print("\npromotion")
print(promotion(4,2,100,5))




            