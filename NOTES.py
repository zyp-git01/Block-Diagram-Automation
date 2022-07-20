


word_height = 3
width = 12

def get_max_len(inlist,outlist):
    max = 0
    for i in range(0, len(inlist)):
        if len(inlist[i]) > max:
            max = len(inlist[i])
        else:
            continue
    for i in range(0, len(outlist)):
        if len(outlist[i]) > max:
            max = len(outlist[i])
        else:
            continue
    return max
def produc_char(input_ports, output_ports,input_num,output_num,i,max_word_len):
    ind = i//3 - 1
    print("ind is %d",ind)
    str_str = ''
    if ind < input_num:
        str_str = str_str + (max_word_len-len(input_ports[ind]))*' '+input_ports[ind]+'|'+(width-2)*' '+'|'
    else:
        str_str = str_str + max_word_len*' '+'|'+(width-2)*' '+'|'
    
    if ind < output_num:
        str_str = str_str + output_ports[ind] + (max_word_len-len(output_ports[ind]))*' ' + '\n'
    else:
        str_str = str_str + '\n'

    return str_str

def draw(input_ports,output_ports,file_name):
    input_num = len(input_ports)
    output_num = len(output_ports)
    max_num = max(output_num, input_num)
    max_word_len = max(get_max_len(input_ports, output_ports),6)
    height = word_height*(max_num + 1)
    
    with open(file_name, 'w') as f:
        for i in range(1, height):
            if i == 1:
                f.write(max_word_len*' '+width*'-'+'\n')
            elif i <= 3: 
                f.write((max_word_len - 5)*' '+'Input'+'|'+(width-2)*' '+'|'+'Output'+'\n')
            elif i % 3 == 1:
                f.write(produc_char(input_ports, output_ports, input_num, output_num, i,max_word_len))
            elif i % 3 == 2:
                f.write(max_word_len*'-'+'|'+(width-2)*' '+'|'+max_word_len*'-'+'\n')
            elif i % 3 == 0:
                f.write((max_word_len)*' '+'|'+(width-2)*' '+'|'+(max_word_len)*' '+'\n')
        f.write(max_word_len*' '+width*'-'+'\n')

def find_io(filename):
    with open(filename, 'r') as f:
        
input_ports = ['apb_data', 'apb_write', 'apb_read','apb_address','apb_proc']
output_ports = ['reg_0x112', 'reg_0x113', 'reg_0x114', 'jijijwidjiawdadw']
draw(input_ports, output_ports,'./module.txt')

