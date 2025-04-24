__all__ = [
    's7_Syntax_Groundtruth',
    's7_Semantic_Groundtruth',
    's7_commandOffset',
    's7_lengthOffset',
    's7_Semantic_Functions_Groundtruth',
]
# semantic_Types = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Types = ['Static', 'Group', 'String', 'Integer', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

TYPE_STATIC = semantic_Types[0]
TYPE_GROUP = semantic_Types[1]
TYPE_STRING = semantic_Types[2]
TYPE_BIT_FIELD = semantic_Types[3]
TYPE_BYTES = semantic_Types[4]

FN_CMD = semantic_Functions[0]
FN_LEN = semantic_Functions[1]
FN_DELIM = semantic_Functions[2]
FN_CHKSUM = semantic_Functions[3]
FN_ALIGNED = semantic_Functions[4]
FN_FILENAME = semantic_Functions[5]

s7_Syntax_Groundtruth = {}

#format1
s7_Syntax_Groundtruth[0] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Syntax_Groundtruth[1] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,24,26,27,30]
s7_Syntax_Groundtruth[2] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,24,26,27,30,31,32,34,38]
s7_Syntax_Groundtruth[3] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,24,26,27,30,31,32,34,38]
s7_Syntax_Groundtruth[4] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,24,26,27,30]

s7_Syntax_Groundtruth[5] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Syntax_Groundtruth[6] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Syntax_Groundtruth[7] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Syntax_Groundtruth[8] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,38]
s7_Syntax_Groundtruth[9] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Syntax_Groundtruth[10] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Syntax_Groundtruth[11] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Syntax_Groundtruth[12] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Syntax_Groundtruth[13] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[14] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Syntax_Groundtruth[15] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Syntax_Groundtruth[16] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[17] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Syntax_Groundtruth[18] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[19] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[20] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[21] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[22] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Syntax_Groundtruth[23] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Syntax_Groundtruth[24] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Syntax_Groundtruth[25] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Syntax_Groundtruth[26] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Syntax_Groundtruth[27] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Syntax_Groundtruth[28] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[29] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Syntax_Groundtruth[30] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Syntax_Groundtruth[31] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,24,25,34,35,36,42,48]
s7_Syntax_Groundtruth[32] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,246]
s7_Syntax_Groundtruth[33] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,80]
s7_Syntax_Groundtruth[34] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19]
s7_Syntax_Groundtruth[35] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,24,26,27,28,36,37,42]
s7_Syntax_Groundtruth[36] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Syntax_Groundtruth[37] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Syntax_Groundtruth[38] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Syntax_Groundtruth[39] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Syntax_Groundtruth[40] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]


#Groundtruth: based on protocol specifications + Wireshark

s7_Semantic_Groundtruth = {}

s7_Semantic_Functions_Groundtruth = {}

s7_lengthOffset = '8'

s7_commandOffset = '7'

''' Semantic-Type Groudtruth'''

#format1
# s7_Syntax_Groundtruth[0] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Semantic_Groundtruth[0] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # fn
    # '18':TYPE_GROUP,        # reserved
    '19,20':TYPE_GROUP, 
    '21,22':TYPE_GROUP,
    '23,24':TYPE_BIT_FIELD
    }
# s7_Syntax_Groundtruth[1] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30]
s7_Semantic_Groundtruth[1] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # fn
    '18':TYPE_BIT_FIELD,        # item cnt
    '19':TYPE_STATIC,
    '20':TYPE_BIT_FIELD,
    '21':TYPE_STATIC,
    '22':TYPE_BIT_FIELD,
    '23,24':TYPE_BIT_FIELD,
    '25,26':TYPE_BIT_FIELD,
    '27':TYPE_BIT_FIELD,
    '28,30':TYPE_BYTES,
    }
# s7_Syntax_Groundtruth[2] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30,38]
s7_Semantic_Groundtruth[2] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # fn
    '18':TYPE_GROUP,        # reserved
    '19':TYPE_STATIC,
    '20':TYPE_BIT_FIELD,
    '21':TYPE_STATIC,
    '22':TYPE_BIT_FIELD,
    '23,24':TYPE_BIT_FIELD,
    '25,26':TYPE_BIT_FIELD,
    '27':TYPE_BIT_FIELD,
    '28,30':TYPE_BYTES,
    '31':TYPE_GROUP,
    '32':TYPE_BIT_FIELD,
    '33,34':TYPE_BIT_FIELD,
    '35,38':TYPE_STRING,
    }
# s7_Syntax_Groundtruth[3] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30,38]
s7_Semantic_Groundtruth[3]=s7_Semantic_Groundtruth[2]
# s7_Syntax_Groundtruth[4] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30]
s7_Semantic_Groundtruth[4] = s7_Semantic_Groundtruth[1]
# s7_Syntax_Groundtruth[5] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Semantic_Groundtruth[5] = s7_Semantic_Groundtruth[0]
# s7_Syntax_Groundtruth[6] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[6] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_BIT_FIELD,
    '27,28':TYPE_BIT_FIELD,
    '29,30':TYPE_BYTES,
    '31,32':TYPE_GROUP,
    }
# s7_Syntax_Groundtruth[7] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Semantic_Groundtruth[7] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_GROUP,
    '27,28':TYPE_GROUP,
    '29':TYPE_GROUP,
    '30':TYPE_BIT_FIELD,
    # '29,30':TYPE_BYTES,
    '31,32':TYPE_BIT_FIELD,
    }
# s7_Syntax_Groundtruth[8] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,38]
s7_Semantic_Groundtruth[8] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_BIT_FIELD,
    '27,28':TYPE_BIT_FIELD,
    '29':TYPE_BIT_FIELD,
    '30':TYPE_GROUP,
    '31,38':TYPE_STRING,
    # '29,30':TYPE_BYTES,
    # '31,32':TYPE_GROUP,
    }
# s7_Syntax_Groundtruth[9] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[9] = s7_Semantic_Groundtruth[6]
# s7_Syntax_Groundtruth[10] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Semantic_Groundtruth[10] = s7_Semantic_Groundtruth[8]
# s7_Syntax_Groundtruth[11] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Groundtruth[11] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_BIT_FIELD,
    '27,28':TYPE_BIT_FIELD,
    '29,30':TYPE_GROUP,
    '31,34':TYPE_STRING,
    '36':TYPE_STRING,
}
# s7_Syntax_Groundtruth[12] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Groundtruth[12] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_BIT_FIELD,
    '27,28':TYPE_BIT_FIELD,
}
# s7_Syntax_Groundtruth[13] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[13] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_BIT_FIELD,
    '27,28':TYPE_BIT_FIELD,
    '29,30':TYPE_STRING,
}
# s7_Syntax_Groundtruth[14] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Groundtruth[14] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17,19':TYPE_GROUP,        # para head
    '20':TYPE_BIT_FIELD,
    '21':TYPE_GROUP,
    '22':TYPE_BIT_FIELD,
    '23':TYPE_GROUP,
    '24':TYPE_GROUP,
    '25':TYPE_GROUP,
    '26':TYPE_BIT_FIELD,
    '27,28':TYPE_BIT_FIELD,
    '29,30':TYPE_STRING,
    '31,35':TYPE_STRING,
    '36':TYPE_STRING,
}
# s7_Syntax_Groundtruth[15] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Groundtruth[15] = s7_Semantic_Groundtruth[12]
# s7_Syntax_Groundtruth[16] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[16] = s7_Semantic_Groundtruth[13]
# s7_Syntax_Groundtruth[17] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Semantic_Groundtruth[17] = s7_Semantic_Groundtruth[10]
# s7_Syntax_Groundtruth[18] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[18] = s7_Semantic_Groundtruth[16]
# s7_Syntax_Groundtruth[19] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[19] = s7_Semantic_Groundtruth[16]
# s7_Syntax_Groundtruth[20] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[20] = s7_Semantic_Groundtruth[16]
# s7_Syntax_Groundtruth[21] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[21] = s7_Semantic_Groundtruth[16]
# s7_Syntax_Groundtruth[22] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Groundtruth[22] = s7_Semantic_Groundtruth[14]
# s7_Syntax_Groundtruth[23] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Groundtruth[23] = s7_Semantic_Groundtruth[14]
# s7_Syntax_Groundtruth[24] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[24] = s7_Semantic_Groundtruth[9]
# s7_Syntax_Groundtruth[25] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[25] = s7_Semantic_Groundtruth[9]
# s7_Syntax_Groundtruth[26] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Groundtruth[26] = s7_Semantic_Groundtruth[15]
# s7_Syntax_Groundtruth[27] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Groundtruth[27] = s7_Semantic_Groundtruth[15]
# s7_Syntax_Groundtruth[28] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[28] = s7_Semantic_Groundtruth[21]
# s7_Syntax_Groundtruth[29] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Groundtruth[29] = s7_Semantic_Groundtruth[23]
# s7_Syntax_Groundtruth[30] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[30] = s7_Semantic_Groundtruth[25]
# s7_Syntax_Groundtruth[31] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,24,25,34,35,36,42,48]
s7_Semantic_Groundtruth[31] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # fn
    '18':TYPE_BIT_FIELD,        # fn status
    '19,20':TYPE_BYTES,
    '21,24':TYPE_BYTES,
    '25':TYPE_BIT_FIELD,
    '26,34':TYPE_STRING,
    '35':TYPE_BIT_FIELD,
    '36':TYPE_STRING,
    '37,42':TYPE_STRING,
    '43,48':TYPE_STRING,
    }
# s7_Syntax_Groundtruth[32] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,246]
s7_Semantic_Groundtruth[32] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # fn
    '18':TYPE_BIT_FIELD,        # fn status
    '19,20':TYPE_BIT_FIELD, # length
    '21,22':TYPE_BYTES,
    '23,246':TYPE_BYTES,
    }
# s7_Syntax_Groundtruth[33] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,80]
s7_Semantic_Groundtruth[33] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # fn
    '18':TYPE_BIT_FIELD,        # fn status
    '19,20':TYPE_BIT_FIELD, # length
    '21,22':TYPE_BYTES,
    '23,80':TYPE_BYTES,
}
# s7_Syntax_Groundtruth[34] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19]
s7_Semantic_Groundtruth[34] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD ,              # data length
    '17':TYPE_GROUP,        # err class
    '18':TYPE_GROUP,        # err code
    '19':TYPE_GROUP,        # fn
}
# s7_Syntax_Groundtruth[35] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,24,26,27,28,36,37,42]
s7_Semantic_Groundtruth[35] = {
    '0':TYPE_STATIC,       # tpkt version
    '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':TYPE_BIT_FIELD ,  # length
    '4':TYPE_BIT_FIELD,  # cotp length
    '5':TYPE_GROUP,  # cotp pdu type  
    '6':TYPE_BIT_FIELD, # cotp mixed bits
    '7':TYPE_STATIC,       # s7 protocol id
    '8':TYPE_GROUP,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':TYPE_BIT_FIELD,        # para length
    '15,16':TYPE_BIT_FIELD,              # data length
    '17':TYPE_GROUP,        # fn
    '18,24':TYPE_BYTES,     # unknown bytes
    '25,26':TYPE_BIT_FIELD, # block len
    '27':TYPE_BIT_FIELD,    # numb of block
    '28':TYPE_GROUP,        # unknow byte
    '29,36':TYPE_STRING,    # file name'
    '37':TYPE_BIT_FIELD,    # str len
    '38,42':TYPE_STRING, 
}
# s7_Syntax_Groundtruth[36] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[36] = s7_Semantic_Groundtruth[30]
# s7_Syntax_Groundtruth[37] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Groundtruth[37] = s7_Semantic_Groundtruth[27]
# s7_Syntax_Groundtruth[38] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Groundtruth[38] = s7_Semantic_Groundtruth[28]
# s7_Syntax_Groundtruth[39] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Semantic_Groundtruth[39] = s7_Semantic_Groundtruth[0]
# s7_Syntax_Groundtruth[40] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Groundtruth[40] = s7_Semantic_Groundtruth[36]



''' Semantic-Function Groudtruth'''
# s7_Syntax_Groundtruth[0] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Semantic_Functions_Groundtruth[0] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    '17':FN_CMD,        # fn
    # '18':TYPE_GROUP,        # reserved
    # '19,20':TYPE_GROUP, 
    # '21,22':TYPE_GROUP,
    # '23,24':TYPE_BIT_FIELD
    }
# s7_Syntax_Groundtruth[1] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30]
s7_Semantic_Functions_Groundtruth[1] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    '17':FN_CMD,        # fn
    '18':FN_LEN,        # item cnt
    # '19':TYPE_STATIC,
    '20':FN_LEN,
    # '21':TYPE_STATIC,
    # '22':TYPE_BIT_FIELD,
    '23,24':FN_LEN,
    # '25,26':TYPE_BIT_FIELD,
    # '27':TYPE_BIT_FIELD,
    # '28,30':TYPE_BYTES,
    }
# s7_Syntax_Groundtruth[2] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30,38]
s7_Semantic_Functions_Groundtruth[2] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    '17':FN_CMD,        # fn
    '18':FN_LEN,        # item cnt
    # '19':TYPE_STATIC,
    # '20':TYPE_BIT_FIELD,
    # '21':TYPE_STATIC,
    # '22':TYPE_BIT_FIELD,
    '23,24':FN_LEN,
    # '25,26':TYPE_BIT_FIELD,
    # '27':TYPE_BIT_FIELD,
    # '28,30':TYPE_BYTES,
    # '31':TYPE_GROUP,
    # '32':TYPE_BIT_FIELD,
    '33,34':FN_LEN,
    # '35,38':TYPE_STRING,
    }
# s7_Syntax_Groundtruth[3] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30,38]
s7_Semantic_Functions_Groundtruth[3]=s7_Semantic_Functions_Groundtruth[2]
# s7_Syntax_Groundtruth[4] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,30]
s7_Semantic_Functions_Groundtruth[4] = s7_Semantic_Functions_Groundtruth[1]
# s7_Syntax_Groundtruth[5] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Semantic_Functions_Groundtruth[5] = s7_Semantic_Functions_Groundtruth[0]
# s7_Syntax_Groundtruth[6] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[6] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,
    # # # '24':TYPE_GROUP,
    # # '25':TYPE_GROUP,
    # '26':TYPE_BIT_FIELD,
    '27,28':FN_LEN,
    # '29,30':TYPE_BYTES,
    # '31,32':TYPE_GROUP,
    }
# s7_Syntax_Groundtruth[7] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Semantic_Functions_Groundtruth[7] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,
    # '24':TYPE_GROUP,
    # '25':TYPE_GROUP,
    # '26':TYPE_GROUP,
    # '27,28':TYPE_GROUP,
    # '29':TYPE_GROUP,
    # '30':TYPE_BIT_FIELD,
    '31,32':FN_LEN,
    }
# s7_Syntax_Groundtruth[8] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,38]
s7_Semantic_Functions_Groundtruth[8] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,            # para len
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,            # subfn
    # '24':TYPE_GROUP,
    # '25':TYPE_GROUP,
    # '26':TYPE_BIT_FIELD,
    '27,28':FN_LEN,
    # '29':TYPE_BIT_FIELD,
    # '30':TYPE_GROUP,
    # '31,38':TYPE_STRING,
    }
# s7_Syntax_Groundtruth[9] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[9] = s7_Semantic_Functions_Groundtruth[6]
# s7_Syntax_Groundtruth[10] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Semantic_Functions_Groundtruth[10] = s7_Semantic_Functions_Groundtruth[8]
# s7_Syntax_Groundtruth[11] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Functions_Groundtruth[11] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,        #para len
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,        # subfn
    # '24':TYPE_GROUP,
    # '25':TYPE_GROUP,
    # '26':TYPE_BIT_FIELD,
    '27,28':FN_LEN,
    # '29,30':TYPE_GROUP,
    # '31,34':TYPE_STRING,
    # '36':TYPE_STRING,
}
# s7_Syntax_Groundtruth[12] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Functions_Groundtruth[12] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,        # para len
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,
    # '24':TYPE_GROUP,
    # '25':TYPE_GROUP,
    # '26':TYPE_BIT_FIELD,
    '27,28':FN_LEN,
}
# s7_Syntax_Groundtruth[13] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[13] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,        #para len
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,
    # '24':TYPE_GROUP,
    # '25':TYPE_GROUP,
    # '26':TYPE_BIT_FIELD,
    '27,28':FN_LEN,
    # '29,30':TYPE_STRING,
}
# s7_Syntax_Groundtruth[14] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Functions_Groundtruth[14] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17,19':TYPE_GROUP,        # para head
    '20':FN_LEN,        # para len
    # '21':TYPE_GROUP,
    # '22':TYPE_BIT_FIELD,
    '23':FN_CMD,
    # '24':TYPE_GROUP,
    # '25':TYPE_GROUP,
    # '26':TYPE_BIT_FIELD,
    '27,28':FN_LEN,
    # '29,30':TYPE_STRING,
    # '31,35':TYPE_STRING,
    # '36':TYPE_STRING,
}
# s7_Syntax_Groundtruth[15] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Functions_Groundtruth[15] = s7_Semantic_Functions_Groundtruth[12]
# s7_Syntax_Groundtruth[16] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[16] = s7_Semantic_Functions_Groundtruth[13]
# s7_Syntax_Groundtruth[17] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,25,26,28,32]
s7_Semantic_Functions_Groundtruth[17] = s7_Semantic_Functions_Groundtruth[10]
# s7_Syntax_Groundtruth[18] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[18] = s7_Semantic_Functions_Groundtruth[16]
# s7_Syntax_Groundtruth[19] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[19] = s7_Semantic_Functions_Groundtruth[16]
# s7_Syntax_Groundtruth[20] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[20] = s7_Semantic_Functions_Groundtruth[16]
# s7_Syntax_Groundtruth[21] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[21] = s7_Semantic_Functions_Groundtruth[16]
# s7_Syntax_Groundtruth[22] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Functions_Groundtruth[22] = s7_Semantic_Functions_Groundtruth[14]
# s7_Syntax_Groundtruth[23] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Functions_Groundtruth[23] = s7_Semantic_Functions_Groundtruth[14]
# s7_Syntax_Groundtruth[24] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[24] = s7_Semantic_Functions_Groundtruth[9]
# s7_Syntax_Groundtruth[25] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[25] = s7_Semantic_Functions_Groundtruth[9]
# s7_Syntax_Groundtruth[26] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Functions_Groundtruth[26] = s7_Semantic_Functions_Groundtruth[15]
# s7_Syntax_Groundtruth[27] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Functions_Groundtruth[27] = s7_Semantic_Functions_Groundtruth[15]
# s7_Syntax_Groundtruth[28] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[28] = s7_Semantic_Functions_Groundtruth[21]
# s7_Syntax_Groundtruth[29] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,36]
s7_Semantic_Functions_Groundtruth[29] = s7_Semantic_Functions_Groundtruth[23]
# s7_Syntax_Groundtruth[30] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[30] = s7_Semantic_Functions_Groundtruth[25]
# s7_Syntax_Groundtruth[31] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,24,25,34,35,36,42,48]
s7_Semantic_Functions_Groundtruth[31] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    '17':FN_CMD,        # fn
    # '18':TYPE_BIT_FIELD,        # fn status
    # '19,20':TYPE_BYTES,
    # '21,24':TYPE_BYTES,
    '25':FN_LEN,
    '26,34':FN_FILENAME,
    '35':FN_LEN,
    # '36':TYPE_STRING,
    # '37,42':TYPE_STRING,
    # '43,48':TYPE_STRING,
    }
# s7_Syntax_Groundtruth[32] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,246]
s7_Semantic_Functions_Groundtruth[32] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    '17':FN_CMD,        # fn
    # '18':TYPE_BIT_FIELD,        # fn status
    '19,20':FN_LEN,     # length
    # '21,22':TYPE_BYTES,
    # '23,246':TYPE_BYTES,
    }
# s7_Syntax_Groundtruth[33] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,80]
s7_Semantic_Functions_Groundtruth[33] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    '17':FN_CMD,        # fn
    # '18':TYPE_BIT_FIELD,        # fn status
    '19,20':FN_LEN, # length
    # '21,22':TYPE_BYTES,
    # '23,80':TYPE_BYTES,
}
# s7_Syntax_Groundtruth[34] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19]
s7_Semantic_Functions_Groundtruth[34] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN ,              # data length
    # '17':TYPE_GROUP,        # err class
    # '18':TYPE_GROUP,        # err code
    '19':FN_CMD,        # fn
}
# s7_Syntax_Groundtruth[35] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,24,26,27,28,36,37,42]
s7_Semantic_Functions_Groundtruth[35] = {
    # '0':TYPE_STATIC,       # tpkt version
    # '1':TYPE_GROUP,        # reserved # as modbus padding
    '2,3':FN_LEN ,  # length
    '4':FN_LEN,  # cotp length
    # '5':TYPE_GROUP,  # cotp pdu type  
    # '6':TYPE_BIT_FIELD, # cotp mixed bits
    # '7':TYPE_STATIC,       # s7 protocol id
    '8':FN_CMD,        # s7 rosctr
    # '9,10':TYPE_BIT_FIELD,  # reverse
    # '11,12':TYPE_BIT_FIELD,              # pdu refer
    '13,14':FN_LEN,        # para length
    '15,16':FN_LEN,              # data length
    '17':FN_CMD,        # fn
    # '18,24':TYPE_BYTES,     # unknown bytes
    '25,26':FN_LEN,     # para block len
    '27':FN_LEN,    # numb of block
    # '28':TYPE_GROUP,        # unknow byte
    '29,36':FN_FILENAME,    # file name'
    '37':FN_LEN,    # str len
    # '38,42':TYPE_STRING, 
}
# s7_Syntax_Groundtruth[36] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[36] = s7_Semantic_Functions_Groundtruth[30]
# s7_Syntax_Groundtruth[37] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,28]
s7_Semantic_Functions_Groundtruth[37] = s7_Semantic_Functions_Groundtruth[27]
# s7_Syntax_Groundtruth[38] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,30]
s7_Semantic_Functions_Groundtruth[38] = s7_Semantic_Functions_Groundtruth[28]
# s7_Syntax_Groundtruth[39] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22,24]
s7_Semantic_Functions_Groundtruth[39] = s7_Semantic_Functions_Groundtruth[0]
# s7_Syntax_Groundtruth[40] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,19,20,21,22,23,24,32]
s7_Semantic_Functions_Groundtruth[40] = s7_Semantic_Functions_Groundtruth[36]