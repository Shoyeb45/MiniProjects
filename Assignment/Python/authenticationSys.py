# length criteria
def pswrdLen(s):
    if(len(s) >= 10):
        return True
    return False

# number of uppercase and lowercase criteria
def pswrdCase(s):
    upperCase, lowerCase = 0, 0
    for i in range(0, len(s)):
        if(s[i] >= 'A' and s[i] <= 'Z'):
            upperCase += 1
        else:
            lowerCase += 1

    if(upperCase >= 2 and lowerCase >= 2):
        return True
    return False

# Digits Criteria
def pswdDigit(s):
    cnt = 0
    for i in range(0, len(s)):
        if(s[i] >= '0' and s[i] <= '9'):
            cnt += 1

    if(cnt >= 2):
        return True
    return False
    
# Special char criteria 
def pswdSpecialChar(s):
    cnt = 0
    for i in range(0, len(s)):
        if((s[i] >= '!' and s[i] <= '/') or (s[i] >= ':' and s[i] <= '@')):
            cnt += 1

    if(cnt >= 2):
        return True
    return False

# repeatation criteria
def pswdCharRepeat(s):
    i = 0
    while(i <= len(s)-1):
        cnt = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                cnt += 1
            else:
                break
        if  cnt > 3:
            return False
        i += cnt
        
    return True

# Username consecutive repeatation
def pswdUserName(username, s):
    i = 0
    while(i <= len(username)-1):
        for j in range(0, len(s)-1):
            if username[i] == s[j]:
                cnt = 1
                for k in range(j+1, len(s)):
                    if s[j] == s[k]:
                        cnt += 1
                    else:
                        break
                
                if cnt > 3:
                    return False
        i += 1

    return True
        

# Main code
username = input("Enter user name:")
pswdList = []
while True:
    ans = True
    pswd = input("Enter password:")

    length = pswrdLen(pswd)
    case = pswrdCase(pswd)
    digit = pswdDigit(pswd)
    specChar = pswdSpecialChar(pswd)
    charRep = pswdCharRepeat(pswd)
    charUser = pswdUserName(username, pswd)

    if len(pswdList) >= 3:
        if pswdList[0] == pswd and pswdList[1] == pswd and pswdList[2] == pswd:
            ans = False
        pswdList.pop(0)

    if ans:
        if length:
            ans = ans and length
            if case:
                ans = ans and case
                if digit:
                    ans = ans and digit
                    if specChar:
                        ans = ans and specChar
                        if charRep:
                            ans = charRep and specChar
                            if charUser:
                                ans = ans and charUser
                            else:
                                ans = False
                                print("The password should not contain any sequence of three or more consecutive characters from the username")
                        else:
                            ans = False
                            print("Your password has characters that is repeating more than three times in a row")
                    else:
                        ans = False
                        print("Please enter atleast 2 special characters(@, #, $, %, &, *, !).")
                else:
                    ans = False
                    print("Please enter atleast 2 digits.")
            else:
                ans = False
                print("Please enter atleast 2 uppercase and lowercase letter.")
        else:
            ans = False
            print("Please enter atleast 10 characters.")
    else:
        print("Your password is same as that of last three password")



    if(ans):
        print("Your password is valid.")
        break
    pswdList.append(pswd)            