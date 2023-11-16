fh = open("code.txt")
ms = ""
for line in fh:
    ms += line.strip()
    ms += " "
print(ms)
key= int(input("Give the key"))
key = key % 26
ecdc = input("Encode or decode?")
if ecdc=="Encode":
    ecdc = 0
else:
    ecdc = 1
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
l = 0
org=[]
x = 0
while x<len(ms):
    org += ms[x].lower()
    x += 1
z = 0
y = 1
nv = []
outp = ""
print(org)
for l in org:
    if l in abc:
        nv = abc.index(l)
        if ecdc == 0:
            nv = (nv + key) % 26
            outp += abc[nv]
        else:
            nv = (nv - key) % 26
            outp += abc[nv]
    else:
        outp += " "     
print(outp)
fh.close

