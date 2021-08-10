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