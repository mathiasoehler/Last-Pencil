import string
nice_to_meet = string.Template("Dear $name! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $name!")
username = str(input())
text = nice_to_meet.substitute(name=username)
print(text)



# put your code here