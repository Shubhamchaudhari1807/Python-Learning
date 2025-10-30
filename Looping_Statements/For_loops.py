n=4
for i in range(0, n):
    print(i)

# Iterating List  ,Tuple String and Dictionary By Using  For  loop

# For List
li = ["shubham", "chaudhari", "from", "shirpur"]
for l in  li:
     
    print(l)
 
# For  Tuple     
tup = ("goal", "Indian Navy", "Post", "Sublieutenant")
for t in tup:
    print(t)

# for String

s = "shubhu"
for st in s:
    print(st)           
    
# for Dictionary

d = dict({'Dream': 'Navy', 'Destiny': 'Struggling to get in IT'})
for dct in  d:
    print("%s  %s" % (dct, d[dct]))

# For Set 
set1 = {10, 20, 39}
for  set in set1:
    print(set)

# Iterating by Index of Sequences 

li = ["shubham", "remember Bajirao Statement", "Waqt Ki GArdisho Ka Gum na Karo...", "Hosale Mushkilo Se palte Hai !!...🚩🚩🚩"]

for index in range(len(li)):
    print(li[index])
    