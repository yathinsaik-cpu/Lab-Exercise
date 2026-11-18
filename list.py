#list1 = ["family",("father","mother","son"),18,12,21,{city:"mumbai"}]
#print(list[-1:-5:-1])
#print(list[2:1:-1])
#print(list1[1][0])

string = "jain university"
#print(string[-1:10:-1])
#print(string[10:-1])
#print(string[11:0])
#print(string[4:5])



string = "jain university"

for letter in string:
    if letter != " ":
        print(letter)
        
        
        
        
string = "jain university"

result = '("' + '","'.join(string) + '")'

print(result)        

string="jain university"




string = "jain university"

list1 = list(string)

print(list1)


string = "jain university"

for char in set(string):
    print(char, ":", string.count(char))
    
    
string = "jain university"

result = string.replace("a", "A")

print(result)    



text = "jain university"

result = text[0:4]

print(result)





print(text.split("\n")[0].split()[:2])