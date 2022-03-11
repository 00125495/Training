

def soultion(s):
    i,k = 0,0
    chars=list(s)
    while i<len(s):
        if( chars[i]=='A' and (k>0 and chars[k-1]=='B') or chars[i]=='B' and (k>0 and chars[k-1]=='A')):
            k=k-1
            i=i+1
        elif (chars[i]=='C' and (k>0 and chars[k-1]=='D') or chars[i]=='D' and (k>0 and chars[k-1]=='C')):
            k=k-1
            i=i+1
        else:
            chars[i]=chars[k]
            k=k+1
            i=i+1
    return ''.join(chars[:k])

s="CABABD"
print(soultion(s))

