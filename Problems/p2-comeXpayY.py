'''
[Problem]
come x pay y (y<x) find total price customer come n.
'''
### function
def promotion(come,pay,per_head,cus):
    total = ((cus // come)*(pay * per_head)) + ((cus % come)*per_head)
    return total

### main
n = int(input("How many people?\nans : "))
#promotion => come 4 pay 3 
print("Total price is ",promotion(4,3,100,n)," baht")