__all__ = [
    'ftp_Syntax_Groundtruth',
    'ftp_Semantic_Groundtruth',
    'ftp_commandOffset',
    'ftp_lengthOffset',
    'ftp_Semantic_Functions_Groundtruth',
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

ftp_Syntax_Groundtruth = {}

# #format1
# ftp_Syntax_Groundtruth[b'\x01'] = [-1,1,3,5,6,7,9]
# ftp_Syntax_Groundtruth[b'\x02'] = [-1,1,3,5,6,7,9]
# ftp_Syntax_Groundtruth[b'\x03'] = [-1,1,3,5,6,7,9]
# ftp_Syntax_Groundtruth[b'\x04'] = [-1,1,3,5,6,7,9]
# ftp_Syntax_Groundtruth[b'\x05'] = [-1,1,3,5,6,7,9]
# ftp_Syntax_Groundtruth[b'\x06'] = [-1,1,3,5,6,7,9]
# #format2
# ftp_Syntax_Groundtruth[b'\x0f'] = [-1,1,3,5,6,7,9,11,12]
# ftp_Syntax_Groundtruth[b'\x10'] = [-1,1,3,5,6,7,9,11,12]
# #format3
# ftp_Syntax_Groundtruth[b'\x0f'] = [-1,1,3,5,6,7,9,11,12]
# ftp_Syntax_Groundtruth[b'\x10'] = [-1,1,3,5,6,7,9,11,12]

# msg fmt by index
ftp_Syntax_Groundtruth[0] = [-1,3,4,13,14,15]
# ftp_Syntax_Groundtruth[0] = [-1,3,13,15]
ftp_Syntax_Groundtruth[1] = [-1,3,4,14,15,16]
# ftp_Syntax_Groundtruth[1] = [-1,3,14,16]
ftp_Syntax_Groundtruth[2] = [-1,3,4,24,25,26]
# ftp_Syntax_Groundtruth[2] = [-1,3,24,26]
ftp_Syntax_Groundtruth[3] = [-1,3,4,24,25,26]
# ftp_Syntax_Groundtruth[3] = [-1,3,24,26]
ftp_Syntax_Groundtruth[4] = [-1,3,4,24,25,26]
# ftp_Syntax_Groundtruth[4] = [-1,3,24,26]
ftp_Syntax_Groundtruth[5] = [-1,3,4,24,25,26]
# ftp_Syntax_Groundtruth[5] = [-1,3,24,26]
ftp_Syntax_Groundtruth[6] = [-1,3,4,24,25,26]
# ftp_Syntax_Groundtruth[6] = [-1,3,24,26]
ftp_Syntax_Groundtruth[7] = [-1,3,4,24,25,26]
# ftp_Syntax_Groundtruth[7] = [-1,3,24,26]
ftp_Syntax_Groundtruth[8] = [-1,3,4,13,14,15]
# ftp_Syntax_Groundtruth[8] = [-1,3,13,15]
ftp_Syntax_Groundtruth[9] = [-1,3,4,14,15,16]
# ftp_Syntax_Groundtruth[9] = [-1,3,14,16]
ftp_Syntax_Groundtruth[10] = [-1,3,4,5]
ftp_Syntax_Groundtruth[11] = [-1,2,3,14,15,16]
# ftp_Syntax_Groundtruth[11] = [-1,2,14,16]
ftp_Syntax_Groundtruth[12] = [-1,3,4,5]
ftp_Syntax_Groundtruth[13] = [-1,3,4,5]
ftp_Syntax_Groundtruth[14] = [-1,2,3,9,10,11]
# ftp_Syntax_Groundtruth[14] = [-1,2,9,11]
ftp_Syntax_Groundtruth[15] = [-1,3,4,5]
ftp_Syntax_Groundtruth[16] = [-1,3,4,5]
ftp_Syntax_Groundtruth[17] = [-1,3,4,5,6,7]
# ftp_Syntax_Groundtruth[17] = [-1,3,5,7]
ftp_Syntax_Groundtruth[18] = [-1,3,4,5]
ftp_Syntax_Groundtruth[19] = [-1,3,4,17,18,19]
# ftp_Syntax_Groundtruth[19] = [-1,3,17,19]
ftp_Syntax_Groundtruth[20] = [-1,3,4,13,14,15]
# ftp_Syntax_Groundtruth[20] = [-1,3,13,15]
ftp_Syntax_Groundtruth[21] = [-1,3,4,14,15,16]
# ftp_Syntax_Groundtruth[21] = [-1,3,14,16]
ftp_Syntax_Groundtruth[22] = [-1,3,4,5,6,7]
# ftp_Syntax_Groundtruth[22] = [-1,3,5,7]
ftp_Syntax_Groundtruth[23] = [-1,3,4,5,6,7]
# ftp_Syntax_Groundtruth[23] = [-1,3,5,7]
ftp_Syntax_Groundtruth[24] = [-1,2,3,4,5,6]
# ftp_Syntax_Groundtruth[24] = [-1,2,4,6]
ftp_Syntax_Groundtruth[25] = [-1,3,4,5,6,7]
# ftp_Syntax_Groundtruth[25] = [-1,3,5,7]
ftp_Syntax_Groundtruth[26] = [-1,3,4,25,26,27]
# ftp_Syntax_Groundtruth[26] = [-1,3,25,27]
ftp_Syntax_Groundtruth[27] = [-1,3,4,9,10,11]
# ftp_Syntax_Groundtruth[27] = [-1,3,9,11]
ftp_Syntax_Groundtruth[28] = [-1,3,4,5,6,7]
# ftp_Syntax_Groundtruth[28] = [-1,3,5,7]
ftp_Syntax_Groundtruth[29] = [-1,3,4,5]
ftp_Syntax_Groundtruth[30] = [-1,3,4,13,14,15]
# ftp_Syntax_Groundtruth[30] = [-1,3,13,15]
ftp_Syntax_Groundtruth[31] = [-1,3,4,14,15,16]
# ftp_Syntax_Groundtruth[31] = [-1,3,14,16]
ftp_Syntax_Groundtruth[32] = [-1,3,4,5]
ftp_Syntax_Groundtruth[33] = [-1,3,4,5]
ftp_Syntax_Groundtruth[34] = [-1,3,4,13,14,15]
# ftp_Syntax_Groundtruth[34] = [-1,3,13,15]
ftp_Syntax_Groundtruth[35] = [-1,3,4,14,15,16]
# ftp_Syntax_Groundtruth[35] = [-1,3,14,16]
ftp_Syntax_Groundtruth[36] = [-1,3,4,5]
ftp_Syntax_Groundtruth[37] = [-1,3,4,5]


#Groundtruth: based on protocol specifications + Wireshark

ftp_Semantic_Groundtruth = {}

ftp_Semantic_Functions_Groundtruth = {}

ftp_lengthOffset = ''

ftp_commandOffset = '7'

''' Semantic-Type Groudtruth'''

#format1
# ftp_Syntax_Groundtruth[0] = [-1,4,13,15]
ftp_Semantic_Groundtruth[0] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,13':TYPE_STRING,
    '5,13':TYPE_STRING,
    '14,14':TYPE_STATIC,
    '15,15':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[1] = [-1,4,14,16]
ftp_Semantic_Groundtruth[1] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,14':TYPE_STRING,
    '5,14':TYPE_STRING,
    '15,15':TYPE_STATIC,
    '16,16':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[2] = [-1,4,24,26]
ftp_Semantic_Groundtruth[2] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,24':TYPE_STRING,
    '5,24':TYPE_STRING,
    '25,25':TYPE_STATIC,
    '26,26':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[3] = [-1,4,24,26]
ftp_Semantic_Groundtruth[3] = ftp_Semantic_Groundtruth[2]
# ftp_Syntax_Groundtruth[4] = [-1,4,24,26]
ftp_Semantic_Groundtruth[4] = ftp_Semantic_Groundtruth[2]
# ftp_Syntax_Groundtruth[5] = [-1,4,24,26]
ftp_Semantic_Groundtruth[5] = ftp_Semantic_Groundtruth[2]
# ftp_Syntax_Groundtruth[6] = [-1,4,24,26]
ftp_Semantic_Groundtruth[6] = ftp_Semantic_Groundtruth[2]
# ftp_Syntax_Groundtruth[7] = [-1,4,24,26]
ftp_Semantic_Groundtruth[7] = ftp_Semantic_Groundtruth[2]
# ftp_Syntax_Groundtruth[8] = [-1,4,13,15]
ftp_Semantic_Groundtruth[8] = ftp_Semantic_Groundtruth[0]
# ftp_Syntax_Groundtruth[9] = [-1,4,14,16]
ftp_Semantic_Groundtruth[9] = ftp_Semantic_Groundtruth[1]
# ftp_Syntax_Groundtruth[10] = [-1,3,5]
ftp_Semantic_Groundtruth[10] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    '5,5':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[11] = [-1,3,14,16]
ftp_Semantic_Groundtruth[11] = {
    '0,2':TYPE_GROUP,
    '3,3':TYPE_STATIC,
    # '3,14':TYPE_STRING,
    '4,14':TYPE_STRING,
    '15,15':TYPE_STATIC,
    '16,16':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[12] = [-1,3,5]
ftp_Semantic_Groundtruth[12] = ftp_Semantic_Groundtruth[10]
# ftp_Syntax_Groundtruth[13] = [-1,3,5]
ftp_Semantic_Groundtruth[13] = ftp_Semantic_Groundtruth[10]
# ftp_Syntax_Groundtruth[14] = [-1,3,9,11]
ftp_Semantic_Groundtruth[14] = {
    '0,2':TYPE_GROUP,
    '3,3':TYPE_STATIC,
    '4,9':TYPE_STRING,
    '10,10':TYPE_STATIC,
    '11,11':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[15] = [-1,3,5]
ftp_Semantic_Groundtruth[15] = ftp_Semantic_Groundtruth[13]
# ftp_Syntax_Groundtruth[16] = [-1,3,5]
ftp_Semantic_Groundtruth[16] = ftp_Semantic_Groundtruth[13]
# ftp_Syntax_Groundtruth[17] = [-1,4,5,7]
ftp_Semantic_Groundtruth[17] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,5':TYPE_STRING,
    '5,5':TYPE_STRING,
    '6,6':TYPE_STATIC,
    '7,7':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[18] = [-1,3,5]
ftp_Semantic_Groundtruth[18] = ftp_Semantic_Groundtruth[16]
# ftp_Syntax_Groundtruth[19] = [-1,4,17,19]
ftp_Semantic_Groundtruth[19] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,17':TYPE_STRING,
    '5,17':TYPE_STRING,
    '18,18':TYPE_STATIC,
    '19,19':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[20] = [-1,4,13,15]
ftp_Semantic_Groundtruth[20] = ftp_Semantic_Groundtruth[8]
# ftp_Syntax_Groundtruth[21] = [-1,4,14,16]
ftp_Semantic_Groundtruth[21] = ftp_Semantic_Groundtruth[9]
# ftp_Syntax_Groundtruth[22] = [-1,4,5,7]
ftp_Semantic_Groundtruth[22] = ftp_Semantic_Groundtruth[17]
# ftp_Syntax_Groundtruth[23] = [-1,4,5,7]
ftp_Semantic_Groundtruth[23] = ftp_Semantic_Groundtruth[17]
# ftp_Syntax_Groundtruth[24] = [-1,3,4,6]
ftp_Semantic_Groundtruth[24] = {
    '0,2':TYPE_GROUP,
    '3,3':TYPE_STATIC,
    # '3,4':TYPE_STRING,
    '4,4':TYPE_STRING,
    '5,5':TYPE_STATIC,
    '6,6':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[25] = [-1,4,5,7]
ftp_Semantic_Groundtruth[25] = ftp_Semantic_Groundtruth[17]
# ftp_Syntax_Groundtruth[26] = [-1,4,25,27]
ftp_Semantic_Groundtruth[26] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,25':TYPE_STRING,
    '5,25':TYPE_STRING,
    '26,26':TYPE_STATIC,
    '27,27':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[27] = [-1,4,9,11]
ftp_Semantic_Groundtruth[27] = {
    '0,3':TYPE_GROUP,
    '4,4':TYPE_STATIC,
    # '4,9':TYPE_STRING,
    '5,9':TYPE_STRING,
    '10,10':TYPE_STATIC,
    '11,11':TYPE_STATIC,
}
# ftp_Syntax_Groundtruth[28] = [-1,4,5,7]
ftp_Semantic_Groundtruth[28] = ftp_Semantic_Groundtruth[17]
# ftp_Syntax_Groundtruth[29] = [-1,3,5]
ftp_Semantic_Groundtruth[29] = ftp_Semantic_Groundtruth[16]
# ftp_Syntax_Groundtruth[30] = [-1,4,13,15]
ftp_Semantic_Groundtruth[30] = ftp_Semantic_Groundtruth[8]
# ftp_Syntax_Groundtruth[31] = [-1,4,14,16]
ftp_Semantic_Groundtruth[31] = ftp_Semantic_Groundtruth[21]
# ftp_Syntax_Groundtruth[32] = [-1,3,5]
ftp_Semantic_Groundtruth[32] = ftp_Semantic_Groundtruth[29]
# ftp_Syntax_Groundtruth[33] = [-1,3,5]
ftp_Semantic_Groundtruth[33] = ftp_Semantic_Groundtruth[29]
# ftp_Syntax_Groundtruth[34] = [-1,4,13,15]
ftp_Semantic_Groundtruth[34] = ftp_Semantic_Groundtruth[30]
# ftp_Syntax_Groundtruth[35] = [-1,4,14,16]
ftp_Semantic_Groundtruth[35] = ftp_Semantic_Groundtruth[31]
# ftp_Syntax_Groundtruth[36] = [-1,3,5]
ftp_Semantic_Groundtruth[36] = ftp_Semantic_Groundtruth[33]
# ftp_Syntax_Groundtruth[37] = [-1,3,5]
ftp_Semantic_Groundtruth[37] = ftp_Semantic_Groundtruth[33]


''' Semantic-Function Groudtruth'''
# ftp_Syntax_Groundtruth[0] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[0] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[1] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[1] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[2] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[2] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[3] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[3] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[4] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[4] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[5] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[5] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[6] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[6] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    # '25,26':FN_DELIM,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[6] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[6] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    # '25,26':FN_DELIM,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[7] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[7] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    # '25,26':FN_DELIM,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[8] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[8] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[9] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[9] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[10] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[10] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[11] = [-1,2,3,14,16]
ftp_Semantic_Functions_Groundtruth[11] = {
    '0,2':FN_CMD,
    '3,3':FN_DELIM,
    # '4,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[12] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[12] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[13] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[13] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
    # '4,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[14] = [-1,2,3,9,11]
ftp_Semantic_Functions_Groundtruth[14] = {
    '0,2':FN_CMD,
    '3,3':FN_DELIM,
    # '4,9':TYPE_STRING,
    '10,10':FN_DELIM,
    '11,11':FN_DELIM,
}
# ftp_Syntax_Groundtruth[15] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[15] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[16] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[16] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
    # '4,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[17] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[17] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[18] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[18] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[19] = [-1,3,4,17,19]
ftp_Semantic_Functions_Groundtruth[19] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,17':TYPE_STRING,
    '18,18':FN_DELIM,
    '19,19':FN_DELIM,
}
# ftp_Syntax_Groundtruth[20] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[20] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[21] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[21] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[22] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[22] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[23] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[23] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    # '6,7':FN_DELIM,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[24] = [-1,2,3,4,6]
ftp_Semantic_Functions_Groundtruth[24] = {
    '0,2':FN_CMD,
    '3,3':FN_DELIM,
    # # '4,4':TYPE_STRING,
    '5,5':FN_DELIM,
    '6,6':FN_DELIM,
}
# ftp_Syntax_Groundtruth[25] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[25] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[26] = [-1,3,4,25,27]
ftp_Semantic_Functions_Groundtruth[26] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,25':TYPE_STRING,
    '26,26':FN_DELIM,
    '27,27':FN_DELIM,
}
# ftp_Syntax_Groundtruth[27] = [-1,3,4,9,11]
ftp_Semantic_Functions_Groundtruth[27] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,9':TYPE_STRING,
    '10,10':FN_DELIM,
    '11,11':FN_DELIM,
}
# ftp_Syntax_Groundtruth[28] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[28] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[29] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[29] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[30] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[30] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[31] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[31] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[32] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[32] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
    # '4,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[33] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[33] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
    # '4,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[34] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[34] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[35] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[35] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[36] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[36] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[37] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[37] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}

# ftp_Syntax_Groundtruth[7] = [-1,3,4,24,26]
ftp_Semantic_Functions_Groundtruth[7] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,24':TYPE_STRING,
    '25,25':FN_DELIM,
    '26,26':FN_DELIM,
}
# ftp_Syntax_Groundtruth[8] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[8] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[9] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[9] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[10] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[10] = {
    '0,3':FN_CMD,
    '4,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[11] = [-1,2,3,14,16]
ftp_Semantic_Functions_Groundtruth[11] = {
    '0,2':FN_CMD,
    # '3,3':FN_DELIM,
    # '4,14':TYPE_STRING,
    '15,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[12] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[12] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[13] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[13] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[14] = [-1,2,3,9,11]
ftp_Semantic_Functions_Groundtruth[14] = {
    '0,2':FN_CMD,
    '3,3':FN_DELIM,
    # '4,9':TYPE_STRING,
    '10,10':FN_DELIM,
    '11,11':FN_DELIM,
}
# ftp_Syntax_Groundtruth[15] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[15] = {
    '0,3':FN_CMD,
    '4,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[16] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[16] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[17] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[17] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[18] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[18] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[19] = [-1,3,4,17,19]
ftp_Semantic_Functions_Groundtruth[19] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,17':TYPE_STRING,
    '18,18':FN_DELIM,
    '19,19':FN_DELIM,
}
# ftp_Syntax_Groundtruth[20] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[20] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[21] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[21] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[22] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[22] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[23] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[23] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    # '6,7':FN_DELIM,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[24] = [-1,2,3,4,6]
ftp_Semantic_Functions_Groundtruth[24] = {
    '0,2':FN_CMD,
    '3,3':FN_DELIM,
    # # '4,4':TYPE_STRING,
    '5,5':FN_DELIM,
    '6,6':FN_DELIM,
}
# ftp_Syntax_Groundtruth[25] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[25] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    # '6,7':FN_DELIM,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[26] = [-1,3,4,25,27]
ftp_Semantic_Functions_Groundtruth[26] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,25':TYPE_STRING,
    '26,26':FN_DELIM,
    '27,27':FN_DELIM,
}
# ftp_Syntax_Groundtruth[27] = [-1,3,4,9,11]
ftp_Semantic_Functions_Groundtruth[27] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,9':TYPE_STRING,
    '10,10':FN_DELIM,
    '11,11':FN_DELIM,
}
# ftp_Syntax_Groundtruth[28] = [-1,3,4,5,7]
ftp_Semantic_Functions_Groundtruth[28] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,5':TYPE_STRING,
    '6,6':FN_DELIM,
    '7,7':FN_DELIM,
}
# ftp_Syntax_Groundtruth[29] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[29] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[30] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[30] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[31] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[31] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    # '15,16':FN_DELIM,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[32] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[32] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[33] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[33] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[34] = [-1,3,4,13,15]
ftp_Semantic_Functions_Groundtruth[34] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,13':TYPE_STRING,
    '14,14':FN_DELIM,
    '15,15':FN_DELIM,
}
# ftp_Syntax_Groundtruth[35] = [-1,3,4,14,16]
ftp_Semantic_Functions_Groundtruth[35] = {
    '0,3':FN_CMD,
    '4,4':FN_DELIM,
    # '5,14':TYPE_STRING,
    '15,15':FN_DELIM,
    '16,16':FN_DELIM,
}
# ftp_Syntax_Groundtruth[36] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[36] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
# ftp_Syntax_Groundtruth[37] = [-1,3,5]
ftp_Semantic_Functions_Groundtruth[37] = {
    '0,3':FN_CMD,
    # '4,5':FN_DELIM,
    '4,4':FN_DELIM,
    '5,5':FN_DELIM,
}
