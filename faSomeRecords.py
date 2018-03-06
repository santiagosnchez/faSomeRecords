# faSomeRecords.py

import argparse
from re import match

def main():
    # parse arguments
    parser = argparse.ArgumentParser(prog="FaSomeRecords.py",
        description="Retrieves some FASTA records provided a FASTA file and a list/records.",
        epilog="""Files can be sepcified one by one with --files
        or by specifying a directory --dir with the files.
        Additionally, a --suffix suffix can be combined with --dir to
        filter out other files.""")
    parser.add_argument(
    '--fasta', '-f', metavar='FASTA_FILE', nargs="*", type=str,
    help='FASTA file where all the sequences are stored.')
    parser.add_argument(
    '--dir', '-d', nargs="?", default=".", type=str,
    help='directory where FASTA files to concatenate are (default: %(default)s).')
    parser.add_argument(
    '--suffix', '-s', nargs="?", type=str,
    help='suffix for FASTA files.')
    parser.add_argument(
    '--outfile', '-o', default="concat.fasta", nargs="?", type=str,
    help='name for output file (default: %(default)s).')
    parser.add_argument(
    '--part', '-q', const=True, nargs="?", type=bool, default=False, metavar="",
    help='will print a partition table.')
    parser.add_argument(
    '--wrap', '-w', const=True, nargs="?", type=bool, default=False, metavar="",
    help='sequences will be wrapped every 100 characters.')
    parser.add_argument(
    '--nexus', '-n', const=True, nargs="?", type=bool, default=False, metavar="",
    help='export in NEXUS format.')
    parser.add_argument(
    '--phylip', '-p', const=True, nargs="?", type=bool, default=False, metavar="",
    help='export in PHYLIP format.')
  
# functions

def readfasta(file):
    data = {}
    with open(file, "r") as f:
        for line in f:
            line = line.rstrip()
            if match("^>",line):
                head = line[1:]
                data[head] = ''
            else:
                data[head] += line
        return data

def wrapseq(seq):
    chunks = []
    interval = map(lambda x: x*100, range((len(seq)/100)+2))
    for i in interval:
        if i != interval[-1]:
            chunks.append(seq[i:interval[interval.index(i)+1]-1])
    return("\n".join(chunks))

def ifkeyisfound(x, key):
    try:
        x[key]
        return True
    except KeyError:
        return False
  
if __name__ == '__main__':
    main()
