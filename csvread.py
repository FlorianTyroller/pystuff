

lines_per_file = 300
smallfile = None
with open('C:\\Users\Flori\Desktop\ol_dump_2021-11-30\ol_dump_2021-11-30_processed.csv') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()