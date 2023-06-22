

def integer_to_english(number):
    #difining the array of numbers
    ones=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    twenties=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety","hundred"]
    
    #if number is 1000
    if number==1000:
        return ("one thousand")
        
    #if number is less than 20
    
    elif number<20:
        return(ones[number])
        
    # if number is between 20 to 100
    
    elif 20<=number<=100:
        if number==100:
            return(twenties[10])
        else:
            num,divisor=divmod(number,10)
            if divisor==0:
                return twenties[num]
            str1=ones[divisor]
            str2=twenties[num]
            return " ".join([str2,str1])
            
    #if number is between 100 and 1000
    
    elif 100<number<1000:
            num,divisor=divmod(number,10)
            str1=divisor
            num,divisor=divmod(num,10)
            str2=divisor
            if str1==0 and str2!=0:
              return (f'{ones[num]} hundred and {twenties[str2]}')
            elif str1==0 and str2==0:
              return  (f'{ones[num]} hundred')
            elif str2==0 and str1!=0:
              return  (f'{ones[num]} hundred and {ones[str1]}')
            else:
              return (f'{ones[num]} hundred and {twenties[str2]} {ones[str1]}')
              
    #number greater than 100 return -1
    
    else:
        return -1
number=700
print(integer_to_english(number))