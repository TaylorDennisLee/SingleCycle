#!/usr/bin/env python

# WISC F-15 Assembler

import re
import sys
import binascii

iDict = 
{
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

rDict = 
{
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


cDict =
{
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
    return bin(int(hex_value,16))[2:]

def assemble(assembly_line):
    al = filter(None,re.split('[\s,]+',cool))
    if al[0] in ['ADD','PADDSB','SUB','NAND','XOR']:
        return iDict[al[0]] + rDict[al[1]] + rDict[al[2]] + rDict[al[3]]
    elif al[0] in ['SLL', 'SRL', 'SRA']:
        return iDict[al[0]] + rDict[al[1]] + rDict[al[2]] + rDict[al[3]]
    elif al[0] in ['LW', 'SW']:
        return iDict[al[0]] + rDict[al[1]] + rDict[al[2]] + hex_to_bin(al[3], 4)
    elif al[0] in ['LHB', 'LLB']:
        return iDict[al[0]] + rDict[al[1]] + hex_to_bin(al[2],8)
    elif al[0] in ['B', 'CALL', 'RET', 'HLT']:

