
import re

def passCheker(takinString):
    if len(takinString) >= 7:
        valPtn = r"([0-9])"
        valPtn2 = r"(['!', '@', '#', '$', '%', '&', '*'])"

        x = re.findall(valPtn, takinString)
        y = re.findall(valPtn2, takinString)

        if len(x) >=2:
            if len(y) >=2:
                return "Strong"
            else:
                return "Weak"
        else:
            return "Not Valid add Some Special Chars"
    else:
        return "Too Short"

takinString = input()
print(passCheker(takinString))

