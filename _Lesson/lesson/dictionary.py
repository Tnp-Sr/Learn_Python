book = {
    'name': 'C', 
    'price':299,
    'page':490
    } 
print('name : ' + book['name']) # book[name data]

book['price']=200 
print(book)

book['color']='black' # add [color : black] in book
print(book)

book.pop('color') # remove
print(book)