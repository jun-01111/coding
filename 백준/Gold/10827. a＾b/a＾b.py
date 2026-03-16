import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a_str = input_data[0]
    b = int(input_data[1])
    
    dec_idx = a_str.find('.')
    
    if dec_idx != -1:
        dec_places = len(a_str) - dec_idx -1
        
        a_int = int(a_str.replace('.',''))
    else:
        dec_places = 0
        a_int = int(a_str)
        
    res_int = a_int ** b
    
    total_dec = dec_places * b
    
    res_str = str(res_int)
    
    if total_dec > 0:
        if len(res_str) <= total_dec:
            res_str = res_str.zfill(total_dec + 1)
            
        ans = res_str[:-total_dec] + '.' + res_str[-total_dec:]
    else:
        ans = res_str
        
    print(ans)
    
solve()