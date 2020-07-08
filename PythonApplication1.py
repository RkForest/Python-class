# types int,float,None,bool
# str, bytes, list[1,2,3], dict d{k1:v1,k2:v2}
# substring > x[4] zero based, list.append(), d{k1]
# == equal != not equal 

# if expression: > indented block elif expression: else: > blank line
# While expression true: > indented block (optional break) > blank line
# For item in collection : > indented block > blank line

# modules - collection of resusable functions

def ordinal_suffix(value):
    """ Returns th,st,nd,rd """
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

 
def ordinal(value):
    return str(value) + ordinal_suffix(value)
 

def main(value):
    #obj = ordinal(value)
    print (obj)
 

#if __name__ == '__main__':
for value in [1,2,3]:
    obj = ordinal(value)
    if __name__ == '__main__':
        main(value)
    
value = 1
while value <= 10:
    obj = ordinal(value)
    if __name__ == '__main__':
        main(value)

    value +=1




