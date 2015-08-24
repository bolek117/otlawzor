__author__ = 'bolek117'

if __name__ == '__main__':
    f = open('snow.txt', 'r')

    as_bin = []
    for line in f:
        if line.find(' \n') != -1:
            as_bin.append('1')
        else:
            as_bin.append('0')

    as_bin_str = ''.join(as_bin)

    flag = []
    for i in xrange(len(as_bin_str)/8):
        tmp = []
        for j in xrange(8):
            tmp.append(as_bin_str[i * 8 + j])

        num = ''.join(tmp)
        flag.append(chr(int(num, 2)))

    print ''.join(flag)

    pass
