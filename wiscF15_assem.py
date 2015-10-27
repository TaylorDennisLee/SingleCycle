#!/usr/bin/env python

# WISC F-15 Assembler

import re
import sys

iDict = {
    'ADD'    :'0000',
    'PADDSB' :'0001',
    'SUB'    :'0010',
    'NAND'   :'0011',
    'XOR'    :'0100',
    'SLL'    :'0101',
    'SRL'    :'0110',
    'SRA'    :'0111',
    'LW'     :'1000',
    'SW'     :'1001',
    'LHB'    :'1010',
    'LLB'    :'1011',
    'B'      :'1100',
    'CALL'   :'1101',
    'RET'    :'1110',
    'HLT'    :'1111'
}

rDict = {
    'R0' : '0000',
    'R1' : '0001',
    'R2' : '0010',
    'R3' : '0011',
    'R4' : '0100',
    'R5' : '0101',
    'R6' : '0110',
    'R7' : '0111',
    'R8' : '1000',
    'R9' : '1001',
    'R10': '1010',
    'R11': '1011',
    'R12': '1100',
    'R13': '1101',
    'R14': '1110',
    'R15': '1111'
}


cDict = {
    'EQ'    :'001',
    'NEQ'   :'000',
    'GT'    :'010',
    'LT'    :'011',
    'GTE'   :'100',
    'LTE'   :'101',
    'OVFL'  :'110',
    'UNCOND':'111'
}


def hex_to_bin(hex_value, bits):
    binary_rep = bin(int(hex_value,16))[2:]
    binary_length = len(binary_rep)
    sign = binary_rep[0]
    return (bits - binary_length)*sign+binary_rep

def signed_int_to_bin(signed_int,bits):



def assemble(assembly_line, index, jump_dic):
    al = filter(None,re.split('[\s,]+', assembly_line))
    if al[0] in ['ADD','PADDSB','SUB','NAND','XOR']:
        return iDict[al[0]] + rDict[al[1]] + rDict[al[2]] + rDict[al[3]]
    elif al[0] in ['SLL', 'SRL', 'SRA']:
        return iDict[al[0]] + rDict[al[1]] + rDict[al[2]] + rDict[al[3]]
    elif al[0] in ['LW', 'SW']:
        return iDict[al[0]] + rDict[al[1]] + rDict[al[2]] + hex_to_bin(al[3], 4)
    elif al[0] in ['LHB', 'LLB']:
        return iDict[al[0]] + rDict[al[1]] + hex_to_bin(al[2],8)
    elif al[0] in ['B']:
        return iDict[al[0]] + cDict[al[1]] + bin((jump_dic[al[1]] - index - 1)  & int('0b' + '1' * 9, 2))
    elif al[0] in ['CALL']:
        return iDict[al[0]] + bin((jump_dic[al[1]] - index - 1)  & int('0b' + '1' * 12, 2))
    elif al[0] in ['RET']:
        return iDict[al[0]] + '0000' + '1111' + '0000'
    elif al[0] in ['HLT']:
        return iDict[al[0]] + '0000' + '0000' + '0000'



if __name__=='__main__':
    jump_dic = {}
    input_file = open(sys.argv[1]).read().split('\n')
    print input_file
    input_file = filter(None, input_file)
    for line in input_file:
        print line
        if line[0] == '#':
            input_file.remove(line)
    for index, line in enumerate(input_file):
        if ':' in line:
            jump_dic[re.split(':',line)[0]] =  index
            print str(index) + ': ' + re.split(':',line)[0]
        
