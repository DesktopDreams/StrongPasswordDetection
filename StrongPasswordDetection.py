import re
print('Hi, please create a strong password \
that consists of atleast 1 Lower and 1 Uppercase, \
1 Digit and password length of minimum 8 characters.')

def meetEachRequirement(requirement, theirPass):
    theReqs = re.compile(requirement)
    checkReqs = theReqs.search(theirPass)
    if (checkReqs == None) == False:
        return True
    else:
        (checkReqs == None) == True
        return False

while True:
    try:
        myPass = str(input())
    except:
        pass
    if len(myPass) < 8: #Check the length of password to be atleast 8.
        print('Your password does not meet a minimum of 8 characters')
        continue
    if meetEachRequirement(r'.*[a-z]+.*', myPass) == False: #Check if there is atleast 1 lowercase character.
        print('Your password does not have atleast 1 lowercase character')
        continue
    if meetEachRequirement(r'.*[A-Z]+.*', myPass) == False:
        print('Your password does not have atleast 1 uppercase character') #Check if there is atleast 1 uppercase character.
        continue
    if meetEachRequirement(r'.*[0-9]+.*', myPass) == False:
        print('Your password does not have atleast 1 digits') #Check if there is atleast 1 digits.
        continue
    else:
        print('You have a strong password')
        break
