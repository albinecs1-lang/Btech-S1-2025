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


#sum of all elements in a list
given_list = [1,2,3,4,5,6]
print(sum(given_list))
