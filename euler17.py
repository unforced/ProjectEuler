numsones = {0:"", 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
numsteens = {0:"", 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}
numstens = {0:"", 1:numsteens, 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
numshundreds = {1:'onehundred', 2:'twohundred', 3:'threehundred', 4:'fourhundred', 5:'fivehundred', 6:'sixhundred', 7:'sevenhundred', 8:'eighthundred', 9:'ninehundred'}

def num_of_letters():
    s = ''
    for x in range(1,1001):
        if x>=1000:
            s+='onethousand'
        elif x>=100:
            s+=numshundreds.__getitem__(int(str(x)[0]))
            if int(str(x)[1])>0 or int(str(x)[2]):
                s+='and'
                if int(str(x)[1])==1:
                    s+=numsteens.__getitem__(int(str(x)[2]))
                else:
                    s+=numstens.__getitem__(int(str(x)[1]))
                    s+=numsones.__getitem__(int(str(x)[2]))
        elif x>=20:
            s+=numstens.__getitem__(int(str(x)[0]))
            s+=numsones.__getitem__(int(str(x)[1]))
        elif x>10:
            s+=numsteens.__getitem__(int(str(x)[1]))
        elif x==10:
            s+='ten'
        else:
            s+=numsones.__getitem__(int(str(x)[0]))
    return s            
