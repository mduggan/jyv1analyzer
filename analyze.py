import glob
from collections import defaultdict


param_sizes = {
'01': 2,
'02': 1,
'04': 0,
'05': 4, # or 0?
'06': 2,
'08': 0,
'09': 2,
'0A': 1,
'0C': 2,
'0E': 3,
'1': 2,
'2': 1,
'4': 4,
'5': 4, # or 0?
'6': 2,
'8': 0,
'9': 2,
'A': 1,
'C': 3,
'E': 3,
}

def determine_opcodes(values):
    c = defaultdict(int)
    valid = {}
    opcodes = ['01', '02', '04', '05', '06', '08', '09', '0A', '0C', '0E', '1', '2', '4', '5', '6', '8', '9', 'A', 'C', 'E']
    starts = set(['0', '1', '2', '4', '5', '6', '8', '9', 'A', 'C', 'E'])
    for o in opcodes:
        valid[o] = set([0,1,2,3,4])

    for v in values:
        if v[0] != '0':
            opcode = v[0]
        else:
            opcode = v[0:2]
        c[opcode] += 1
        lens = list(valid[opcode])
        if len(lens) == 0:
            continue
        for l in lens:
            if l+len(opcode) > len(v) or v[l+len(opcode)] not in starts:
                #print("discarding len %d for opcode %s" % (l, opcode))
                valid[opcode].discard(l)


    k = list(c.keys())
    k.sort()
    print("opcode counts:")
    for opcode in k:
        print("%s: %d" % (opcode, c[opcode]))
    k = list(valid.keys())
    k.sort()
    print("valid lengths:")
    for opcode in k:
        valids = ','.join(str(x) for x in valid[opcode])
        print("%s: %s" % (opcode, valids))



def main():

    data = {}
    files = glob.glob("*/*.dat")
    files.sort()
    print("reading data from %d files" % (len(files),))
    for f in files:
        dat = open(f, 'rb').read()
        datstr = ''.join('%02X' % ord(x) for x in dat)
        data[f.split('/')[1].split('.')[0]] = datstr

    print("read a total of %d nibbles from %d files" % (sum(len(x) for x in data.values()), len(files)))

    determine_opcodes(data.values())
    """
    k = list(data.keys())
    k.sort()
    for key in k:
        val = data[key *
        if val[0] == '1':
            print("%s - %s" % (val[:10], key))
    """


main()
