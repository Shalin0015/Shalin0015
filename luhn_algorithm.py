#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    lst1=[]
    lst2=[]
    while card_number>0:
       card_number,digit= divmod(card_number,10)
       lst1.append(digit)
    for i in lst1[1::2]:
       lst2.append(i*2)
    lst3=[]
    for i in lst2:
        if i >9:
            sum=0
            while i>0:
                i,divid=divmod(i,10)
                sum=sum+divid
            lst3.append(sum)
        else:
            lst3.append(i)
    del lst2
    sum1=0
    sum2=0
    for i in lst3:
        sum1+=i
    for i in lst1[0::2]:
        sum2+=i
    sum3=sum1+sum2
    if sum3//10==0:
        return True
    else:
        return False

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(5239512608615007)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")