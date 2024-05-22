frutas= ["banana","manzana","ciruela","pera","uva","durazno"]

# evitando que se coma una manzana con la sentencia continue  
for fruta in frutas:
    if fruta == 'uva':
     continue
    print (f'me voy a comer una {fruta}')
    
#
for fruta in frutas:
    print (f'me voy a comer una {fruta}')
    if fruta == 'uva':
     break
else: 
  print("terminado") 