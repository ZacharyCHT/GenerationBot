import secrets

class SpecialRandoms:
    # 
    # Generates count number of strings of Len strLength from ASCII characters 33 -> 126. (lowercase, caps, numbers, and specials)
    # 
    def RandString(strLen, count):
        for i in range(count):
            randString = []
            for i in range(strLen):
                randString.append(chr(int(secrets.choice(range(33, 126)))))
            randString = ''.join(randString)
            yield randString
    # 
    # Generates count number of strings of strLen Length from ASCII characters 48 -> 57, 65 -> 90, 97 -> 122. (lowercase, caps, and numbers)
    # 
    def RandStringLegal(strLen, count):
        for i in range(count):
            randString = []
            charsa = [chr(i) for i in range(48, 57)]
            charsb = [chr(i) for i in range(65, 90)]
            charsc = [chr(i) for i in range(97, 122)]
            chars = charsa + charsb + charsc
            for i in range(strLen):
                randString.append(secrets.choice(chars))
            randString = ''.join(randString)
            yield randString
    # 
    # Generates count number of strings of strLen Length from ASCII characters 48 -> 57, 65 -> 90, 97 -> 122. (lowercase, caps, and numbers)
    # Type argument dictates formatting. 1 = formatting, 2 = no formatting
    #    
    def Combo(strLen, type, count):
        for i in range(count):
            if (type == 1):
                for f in SpecialRandoms.RandStringLegal(strLen, 1):
                    username = f
                for f in SpecialRandoms.RandString(strLen, 1):
                    password = f
                cap = '■'
                mid = '▬'
                strLen = strLen + 13
                top = cap + mid*strLen + cap
                bottom = cap + mid*strLen + cap
                combo = ('\n' + top + '\n''Username: ' + username + '\n\n' + 'Password: ' + password + '\n' + bottom)
                strLen = strLen - 13
                yield combo
            elif (type == 2):
                for f in SpecialRandoms.RandStringLegal(strLen, 1):
                    username = f
                for f in SpecialRandoms.RandString(strLen, 1):
                    password = f
                combo = (username + ':' + password)
                yield combo