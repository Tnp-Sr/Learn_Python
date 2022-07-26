message='love you'

str_len = len(message) # length str
print(str_len) # th นับรวมสระ

check= 'ก' in message
print(check)

num=message.upper() # message not change
print(num)

insert=message.replace('you','yourself')
print(message)

words=message.split(' ') # str -> list
print(words)

n_msg=", ".join(words) # list -> str
print(n_msg)

### advance String
print("")
## string[index] 
name = "TnpSr"
#[start:before last]
print(name[0:2]) 
#[-num] -> count from last
print(name[-2:]) 
print(len(name))

## delete left-right space 
name = " TnpSr "
print(name,"=",len(name))
name =name.strip() 
print(name,"=",len(name)) 

## replace(old,new,count)
name = "TnpTnpSr"
print(name.replace("Tnp","Ploy"))
print(name.replace("Tnp","Ploy",1))

## check word
name = "Ploy TnpSr"
have_Ploy = "Ploy" in name
if have_Ploy:
    print("have Ploy")

## {}
name = "Tnp Sr"
# {index : .digit}
print("Name : {0}\nMoney : {1:.2f}".format(name,8024.545))

## string.count("word") -> check how many word?
## string.startswith("")
## string.endswith("")