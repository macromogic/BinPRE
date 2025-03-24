
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
dns_Syntax_Groundtruth = {}



dns_Syntax_Groundtruth[0] = [-1,1,3,5,7,9,11,12,14,15,22,23,26,27,29,30,32,34]
dns_Syntax_Groundtruth[1] = [-1,1,3,5,7,9,11,12,14,15,22,23,26,27,29,30,32,34]
dns_Syntax_Groundtruth[2] = [-1,1,3,5,7,9,11,12,17,18,25,26,29,30,32,34]
dns_Syntax_Groundtruth[3] = [-1,1,3,5,7,9,11,12,17,18,25,26,29,30,32,34]
dns_Syntax_Groundtruth[4] = [-1,1,3,5,7,9,11,12,17,18,24,25,28,29,31,33]
dns_Syntax_Groundtruth[5] = [-1,1,3,5,7,9,11,12,17,18,24,25,28,29,31,33]
dns_Syntax_Groundtruth[6] = [-1,1,3,5,7,9,11,12,22,23,32,33,36,37,39,41]
dns_Syntax_Groundtruth[7] = [-1,1,3,5,7,9,11,12,22,23,32,33,36,37,39,41]
dns_Syntax_Groundtruth[8] = [-1,1,3,5,7,9,11,12,16,17,22,23,26,27,29,31]
dns_Syntax_Groundtruth[9] = [-1,1,3,5,7,9,11,12,16,17,22,23,26,27,29,31]
dns_Syntax_Groundtruth[10] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[11] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[12] = [-1,1,3,5,7,9,11,12,16,17,23,24,29,30,33,34,36,38]
dns_Syntax_Groundtruth[13] = [-1,1,3,5,7,9,11,12,16,17,23,24,29,30,33,34,36,38]
dns_Syntax_Groundtruth[14] = [-1,1,3,5,7,9,11,12,16,17,23,24,29,30,33,34,36,38]
dns_Syntax_Groundtruth[15] = [-1,1,3,5,7,9,11,12,16,17,23,24,29,30,33,34,36,38]
dns_Syntax_Groundtruth[16] = [-1,1,3,5,7,9,11,12,18,19,24,25,28,29,31,33]
dns_Syntax_Groundtruth[17] = [-1,1,3,5,7,9,11,12,18,19,24,25,28,29,31,33]
dns_Syntax_Groundtruth[18] = [-1,1,3,5,7,9,11,12,13,14,22,23,26,27,29,31]
dns_Syntax_Groundtruth[19] = [-1,1,3,5,7,9,11,12,13,14,22,23,26,27,29,31]
dns_Syntax_Groundtruth[20] = [-1,1,3,5,7,9,11,12,15,16,22,23,26,27,29,31]
dns_Syntax_Groundtruth[21] = [-1,1,3,5,7,9,11,12,15,16,22,23,26,27,29,31]
dns_Syntax_Groundtruth[22] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[23] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[24] = [-1,1,3,5,7,9,11,12,17,18,21,22,25,26,33,34,37,38,40,42]
dns_Syntax_Groundtruth[25] = [-1,1,3,5,7,9,11,12,17,18,21,22,25,26,33,34,37,38,40,42]
dns_Syntax_Groundtruth[26] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[27] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[28] = [-1,1,3,5,7,9,11,12,16,17,24,25,28,29,31,33]
dns_Syntax_Groundtruth[29] = [-1,1,3,5,7,9,11,12,16,17,24,25,28,29,31,33]
dns_Syntax_Groundtruth[30] = [-1,1,3,5,7,9,11,12,15,16,22,23,26,27,29,31]
dns_Syntax_Groundtruth[31] = [-1,1,3,5,7,9,11,12,15,16,22,23,26,27,29,31]
dns_Syntax_Groundtruth[32] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[33] = [-1,1,3,5,7,9,11,12,18,19,23,24,33,34,37,38,40,42]
dns_Syntax_Groundtruth[34] = [-1,1,3,5,7,9,11,12,17,18,25,26,29,30,32,34]
dns_Syntax_Groundtruth[35] = [-1,1,3,5,7,9,11,12,17,18,25,26,29,30,32,34]
dns_Syntax_Groundtruth[36] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[37] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[38] = [-1,1,3,5,7,9,11,12,17,18,21,22,26,27,34,35,38,39,41,43]
dns_Syntax_Groundtruth[39] = [-1,1,3,5,7,9,11,12,17,18,21,22,26,27,34,35,38,39,41,43]
dns_Syntax_Groundtruth[40] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[41] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[42] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[43] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[44] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[45] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[46] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[47] = [-1,1,3,5,7,9,11,12,14,15,17,18,23,24,27,28,30,32]
dns_Syntax_Groundtruth[48] = [-1,1,3,5,7,9,11,12,15,16,21,22,25,26,28,30]
dns_Syntax_Groundtruth[49] = [-1,1,3,5,7,9,11,12,15,16,21,22,25,26,28,30]

#Groundtruth: based on protocol specifications + Wireshark

dns_Semantic_Groundtruth = {}

dns_Semantic_Functions_Groundtruth = {}

dns_lengthOffset = '4,5'

dns_commandOffset = '7'

''' Semantic-Type Groudtruth'''
# dns_Syntax_Groundtruth[0] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Groundtruth[0] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '15':TYPE_BIT_FIELD,
    '23':TYPE_BIT_FIELD,
    '27':TYPE_BIT_FIELD,
    '31,32':TYPE_GROUP,
    '33,34':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[1] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Groundtruth[1] = dns_Semantic_Groundtruth[0]
# dns_Syntax_Groundtruth[2] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Groundtruth[2] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '26':TYPE_BIT_FIELD,
    '31,32':TYPE_GROUP,
    '33,34':TYPE_GROUP,
    }

# dns_Syntax_Groundtruth[3] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Groundtruth[3] = dns_Semantic_Groundtruth[2]
# dns_Syntax_Groundtruth[4] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Groundtruth[4] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '25':TYPE_BIT_FIELD,
    '30,31':TYPE_GROUP,
    '32,33':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[5] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Groundtruth[5] = dns_Semantic_Groundtruth[4]
# dns_Syntax_Groundtruth[6] = [-1,1,3,5,7,9,11,37,39,41]
dns_Semantic_Groundtruth[6] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '23':TYPE_BIT_FIELD,
    '33':TYPE_BIT_FIELD,
    '38,39':TYPE_GROUP,
    '40,41':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[7] = [-1,1,3,5,7,9,11,37,39,41]
dns_Semantic_Groundtruth[7] = dns_Semantic_Groundtruth[6]
# dns_Syntax_Groundtruth[8] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[8] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '17':TYPE_BIT_FIELD,
    '23':TYPE_BIT_FIELD,
    '28,29':TYPE_GROUP,
    '30,31':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[9] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[9] = dns_Semantic_Groundtruth[8]
# dns_Syntax_Groundtruth[10] = [-1,1,3,5,7,9,11,28,40,42]
dns_Semantic_Groundtruth[10] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '19':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '34':TYPE_BIT_FIELD,
    '39,40':TYPE_GROUP,
    '41,42':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[11] = [-1,1,3,5,7,9,11,28,40,42]
dns_Semantic_Groundtruth[11] = dns_Semantic_Groundtruth[10]
# dns_Syntax_Groundtruth[12] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Groundtruth[12] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '17':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '30':TYPE_BIT_FIELD,
    '35,36':TYPE_GROUP,
    '37,38':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[13] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Groundtruth[13] = dns_Semantic_Groundtruth[12]
# dns_Syntax_Groundtruth[14] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Groundtruth[14] = dns_Semantic_Groundtruth[12]
# dns_Syntax_Groundtruth[15] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Groundtruth[15] = dns_Semantic_Groundtruth[12]
# dns_Syntax_Groundtruth[16] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Groundtruth[16] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '19':TYPE_BIT_FIELD,
    '25':TYPE_BIT_FIELD,
    '30,31':TYPE_GROUP,
    '32,33':TYPE_GROUP,
    }

# dns_Syntax_Groundtruth[17] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Groundtruth[17] = dns_Semantic_Groundtruth[16]
# dns_Syntax_Groundtruth[18] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[18] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '14':TYPE_BIT_FIELD,
    '23':TYPE_BIT_FIELD,
    '28,29':TYPE_GROUP,
    '30,31':TYPE_GROUP,
    }

# dns_Syntax_Groundtruth[19] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[19] = dns_Semantic_Groundtruth[18]
# dns_Syntax_Groundtruth[20] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[20] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '16':TYPE_BIT_FIELD,
    '23':TYPE_BIT_FIELD,
    '28,29':TYPE_GROUP,
    '30,31':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[21] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[21] = dns_Semantic_Groundtruth[20]
# dns_Syntax_Groundtruth[22] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[22] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '19':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '34':TYPE_BIT_FIELD,
    '39,40':TYPE_GROUP,
    '41,42':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[23] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[23] = dns_Semantic_Groundtruth[22]
# dns_Syntax_Groundtruth[24] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[24] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '22':TYPE_BIT_FIELD,
    '26':TYPE_BIT_FIELD,
    '34':TYPE_BIT_FIELD,
    '39,40':TYPE_GROUP,
    '41,42':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[25] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[25] = dns_Semantic_Groundtruth[24]
# dns_Syntax_Groundtruth[26] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[26] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '19':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '34':TYPE_BIT_FIELD,
    '39,40':TYPE_GROUP,
    '41,42':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[27] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[27] = dns_Semantic_Groundtruth[26]
# dns_Syntax_Groundtruth[28] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Groundtruth[28] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '17':TYPE_BIT_FIELD,
    '25':TYPE_BIT_FIELD,
    '30,31':TYPE_GROUP,
    '32,33':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[29] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Groundtruth[29] = dns_Semantic_Groundtruth[28]
# dns_Syntax_Groundtruth[30] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[30] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '16':TYPE_BIT_FIELD,
    '23':TYPE_BIT_FIELD,
    '28,29':TYPE_GROUP,
    '30,31':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[31] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Groundtruth[31] = dns_Semantic_Groundtruth[30]
# dns_Syntax_Groundtruth[32] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[32] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '19':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '34':TYPE_BIT_FIELD,
    '39,40':TYPE_GROUP,
    '41,42':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[33] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Groundtruth[33] = dns_Semantic_Groundtruth[32]
# dns_Syntax_Groundtruth[34] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Groundtruth[34] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '26':TYPE_BIT_FIELD,
    '31,32':TYPE_GROUP,
    '33,34':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[35] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Groundtruth[35] = dns_Semantic_Groundtruth[34]
# dns_Syntax_Groundtruth[36] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[36] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '15':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '29,30':TYPE_GROUP,
    '31,32':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[37] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[37] = dns_Semantic_Groundtruth[36]
# dns_Syntax_Groundtruth[38] = [-1,1,3,5,7,9,11,39,41,43]
dns_Semantic_Groundtruth[38] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '22':TYPE_BIT_FIELD,
    '27':TYPE_BIT_FIELD,
    '35':TYPE_BIT_FIELD,
    '40,41':TYPE_GROUP,
    '42,43':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[39] = [-1,1,3,5,7,9,11,39,41,43]
dns_Semantic_Groundtruth[39] = dns_Semantic_Groundtruth[38]
# dns_Syntax_Groundtruth[40] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[40] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '15':TYPE_BIT_FIELD,
    '18':TYPE_BIT_FIELD,
    '24':TYPE_BIT_FIELD,
    '29,30':TYPE_GROUP,
    '31,32':TYPE_GROUP,
}
# dns_Syntax_Groundtruth[41] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[41] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[42] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[42] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[43] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[43] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[44] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[44] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[45] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[45] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[46] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[46] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[47] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Groundtruth[47] = dns_Semantic_Groundtruth[40]
# dns_Syntax_Groundtruth[48] = [-1,1,3,5,7,9,11,26,28,30]
dns_Semantic_Groundtruth[48] = {
    '0,1':TYPE_STATIC,
    '2,3':TYPE_BIT_FIELD,
    '4,5':TYPE_BIT_FIELD,
    '6,7':TYPE_BIT_FIELD,
    '8,9':TYPE_BIT_FIELD,
    '10,11':TYPE_BIT_FIELD,
    '12':TYPE_BIT_FIELD,
    '16':TYPE_BIT_FIELD,
    '22':TYPE_BIT_FIELD,
    '27,28':TYPE_GROUP,
    '29,30':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[49] = [-1,1,3,5,7,9,11,26,28,30]
dns_Semantic_Groundtruth[49] = dns_Semantic_Groundtruth[48]


''' Semantic-Function Groudtruth'''
# dns_Syntax_Groundtruth[0] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Functions_Groundtruth[0] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '15':FN_LEN,
    '23':FN_LEN,
    '27':FN_LEN,
    # '31,32':TYPE_GROUP,
    # '33,34':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[1] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Functions_Groundtruth[1] = dns_Semantic_Functions_Groundtruth[0]
# dns_Syntax_Groundtruth[2] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Functions_Groundtruth[2] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '18':FN_LEN,
    '26':FN_LEN,
}
# dns_Syntax_Groundtruth[3] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Functions_Groundtruth[3] = dns_Semantic_Functions_Groundtruth[2]
# dns_Syntax_Groundtruth[4] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Functions_Groundtruth[4] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,

    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '18':FN_LEN,
    '25':FN_LEN,
    # '30,31':TYPE_GROUP,
    # '32,33':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[5] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Functions_Groundtruth[5] = dns_Semantic_Functions_Groundtruth[4]
# dns_Syntax_Groundtruth[6] = [-1,1,3,5,7,9,11,37,39,41]
dns_Semantic_Functions_Groundtruth[6] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '23':FN_LEN,
    '33':FN_LEN,
    }
# dns_Syntax_Groundtruth[7] = [-1,1,3,5,7,9,11,37,39,41]
dns_Semantic_Functions_Groundtruth[7] = dns_Semantic_Functions_Groundtruth[6]
# dns_Syntax_Groundtruth[8] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[8] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '17':FN_LEN,
    '23':FN_LEN,
    # '28,29':TYPE_GROUP,
    # '30,31':TYPE_GROUP,
    }
# dns_Syntax_Groundtruth[9] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[9] = dns_Semantic_Functions_Groundtruth[8]
# dns_Syntax_Groundtruth[10] = [-1,1,3,5,7,9,11,28,40,42]
dns_Semantic_Functions_Groundtruth[10] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '19':FN_LEN,
    '24':FN_LEN,
    '34':FN_LEN,
    }
# dns_Syntax_Groundtruth[11] = [-1,1,3,5,7,9,11,28,40,42]
dns_Semantic_Functions_Groundtruth[11] = dns_Semantic_Functions_Groundtruth[10]
# dns_Syntax_Groundtruth[12] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Functions_Groundtruth[12] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '17':FN_LEN,
    '24':FN_LEN,
    '30':FN_LEN,
    }
# dns_Syntax_Groundtruth[13] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Functions_Groundtruth[13] = dns_Semantic_Functions_Groundtruth[12]
# dns_Syntax_Groundtruth[14] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Functions_Groundtruth[14] = dns_Semantic_Functions_Groundtruth[12]
# dns_Syntax_Groundtruth[15] = [-1,1,3,5,7,9,11,34,36,38]
dns_Semantic_Functions_Groundtruth[15] = dns_Semantic_Functions_Groundtruth[12]
# dns_Syntax_Groundtruth[16] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Functions_Groundtruth[16] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '19':FN_LEN,
    '25':FN_LEN,
}
# dns_Syntax_Groundtruth[17] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Functions_Groundtruth[17] = dns_Semantic_Functions_Groundtruth[16]
# dns_Syntax_Groundtruth[18] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[18] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '14':FN_LEN,
    '23':FN_LEN,
}
# dns_Syntax_Groundtruth[19] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[19] = dns_Semantic_Functions_Groundtruth[18]
# dns_Syntax_Groundtruth[20] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[20] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '16':FN_LEN,
    '23':FN_LEN,
}
# dns_Syntax_Groundtruth[21] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[21] = dns_Semantic_Functions_Groundtruth[20]
# dns_Syntax_Groundtruth[22] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[22] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '19':FN_LEN,
    '24':FN_LEN,
    '34':FN_LEN,
}
# dns_Syntax_Groundtruth[23] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[23] = dns_Semantic_Functions_Groundtruth[22]
# dns_Syntax_Groundtruth[24] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[24] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '18':FN_LEN,
    '22':FN_LEN,
    '26':FN_LEN,
    '34':FN_LEN,
}
# dns_Syntax_Groundtruth[25] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[25] = dns_Semantic_Functions_Groundtruth[24]
# dns_Syntax_Groundtruth[26] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[26] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '19':FN_LEN,
    '24':FN_LEN,
    '34':FN_LEN,
}
# dns_Syntax_Groundtruth[27] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[27] = dns_Semantic_Functions_Groundtruth[26]
# dns_Syntax_Groundtruth[28] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Functions_Groundtruth[28] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '17':FN_LEN,
    '25':FN_LEN,
}
# dns_Syntax_Groundtruth[29] = [-1,1,3,5,7,9,11,29,31,33]
dns_Semantic_Functions_Groundtruth[29] = dns_Semantic_Functions_Groundtruth[28]
# dns_Syntax_Groundtruth[30] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[30] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '16':FN_LEN,
    '23':FN_LEN,
}
# dns_Syntax_Groundtruth[31] = [-1,1,3,5,7,9,11,27,29,31]
dns_Semantic_Functions_Groundtruth[31] = dns_Semantic_Functions_Groundtruth[30]
# dns_Syntax_Groundtruth[32] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[32] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '19':FN_LEN,
    '24':FN_LEN,
    '34':FN_LEN,
}
# dns_Syntax_Groundtruth[33] = [-1,1,3,5,7,9,11,38,40,42]
dns_Semantic_Functions_Groundtruth[33] = dns_Semantic_Functions_Groundtruth[32]
# dns_Syntax_Groundtruth[34] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Functions_Groundtruth[34] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '18':FN_LEN,
    '26':FN_LEN,
}
# dns_Syntax_Groundtruth[35] = [-1,1,3,5,7,9,11,30,32,34]
dns_Semantic_Functions_Groundtruth[35] = dns_Semantic_Functions_Groundtruth[34]
# dns_Syntax_Groundtruth[36] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[36] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '15':FN_LEN,
    '18':FN_LEN,
    '24':FN_LEN,
    }
# dns_Syntax_Groundtruth[37] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[37] = dns_Semantic_Functions_Groundtruth[36]
# dns_Syntax_Groundtruth[38] = [-1,1,3,5,7,9,11,39,41,43]
dns_Semantic_Functions_Groundtruth[38] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '18':FN_LEN,
    '22':FN_LEN,
    '27':FN_LEN,
    '35':FN_LEN,
    }
# dns_Syntax_Groundtruth[39] = [-1,1,3,5,7,9,11,39,41,43]
dns_Semantic_Functions_Groundtruth[39] = dns_Semantic_Functions_Groundtruth[38]
# dns_Syntax_Groundtruth[40] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[40] = {
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '15':FN_LEN,
    '18':FN_LEN,
    '24':FN_LEN,
}
# dns_Syntax_Groundtruth[41] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[41] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[42] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[42] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[43] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[43] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[44] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[44] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[45] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[45] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[46] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[46] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[47] = [-1,1,3,5,7,9,11,28,30,32]
dns_Semantic_Functions_Groundtruth[47] = dns_Semantic_Functions_Groundtruth[40]
# dns_Syntax_Groundtruth[48] = [-1,1,3,5,7,9,11,26,28,30]
dns_Semantic_Functions_Groundtruth[48] = {
    # '0,1':TYPE_STATIC,
    # '2,3':TYPE_BIT_FIELD,
    '4,5':FN_LEN,
    '6,7':FN_LEN,
    '8,9':FN_LEN,
    '10,11':FN_LEN,
    '12':FN_LEN,
    '16':FN_LEN,
    '22':FN_LEN,
    }
# dns_Syntax_Groundtruth[49] = [-1,1,3,5,7,9,11,26,28,30]
dns_Semantic_Functions_Groundtruth[49] = dns_Semantic_Functions_Groundtruth[48]