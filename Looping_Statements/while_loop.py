# While Loops
# cnt = 0
# while(cnt < 3):
#     cnt = cnt + 1
#     print("Shubham Loves GeoPolitics ..")

#Nested Loops

from __future__ import print_function
for i in range(1,5):
    for j in range(1):
        print(i, end= ' ')
    print() 
 
# Loop COntrol  Statements
# 1) Continue Statements

for letter in 'geeksforgeeks':
    if letter =='e' or letter =='s':
        continue
    print('Current Letter : ', letter)
    
# 2) Break Statement

for break_Statement in "geeksforgeeks":
    if break_Statement == 'e' or break_Statement == 's':
        break
    print('Current B  Letter : ', break_Statement)  
      
for pass_Statement in "geeksforgeeks":
        pass
print('Last Letter : ', pass_Statement)  
          