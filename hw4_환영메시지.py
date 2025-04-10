def rep_char(c,n):
    print(c*n)

def draw_line_string(msg1, msg2):
    
    msg1 = 'Hello' +' ' +msg1
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    
    print(f'Input his/her name : {msg1}')
    
    
    rep_char('-',nstr)
    print(msg1)
    print(msg2)
    rep_char('-',nstr)


msg1 = input('Input his/her name: ')
msg2 = 'Welcom to Seoul.'


draw_line_string(msg1,msg2)

