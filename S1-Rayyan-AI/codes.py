#1
#to check the length of the string
words = "abcedefgh"
print(len(words))

#2
#replacing text
name = "gf fjgdfkjg ksdgjfdjg"
print(name.replace("gf","replaced"))

#3
#to count num of words in a string
string_value = "hellow who how why by"
c = string_value.split()
print(len(c))

#4
#to check if its a palindrome
string = "asddsa"
rever = string[::-1]
if rever == string:
  print("yes it isa palindrome")
else:
  print("no its not a palindrome")



#5
#slicing a word
slised = "malayalam"
print(slised[0:4])


#6
#reversing a string
reverserr = "stringgg"
print(reverserr[::-1])


#7
#sum of all elements in a list
given_list = [1,2,3,4,5,6]
print(sum(given_list))


#8
#largest and smallest elements in a list
given_list_one = [1,2,3,4,5,6]
print(f'the least is {min(given_list_one)} and maximum in {max(given_list_one)}')


#9 
#to find second lagest 
list_given = [1,2,3,4,5,6]
list_given.remove(max(list_given))
print(max(list_given))


#10
#reverce a list
ls = [1,2,3,4,5,6]
rve = list(reversed(ls))
print(rve)
