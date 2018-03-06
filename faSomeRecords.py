#!/usr/bin/env python
# faSomeRecords.py

import argparse, textwrap
from sys import exit
from re import match

def main():
    # parse arguments
    parser = argparse.ArgumentParser(prog="FaSomeRecords.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Retrieves some FASTA records provided a FASTA file and a list or records.",
        epilog=textwrap.dedent('''\
Records can be sepcified providing a list file with --list/-l
or one by one in the command line using --records/-r.

The elements in the list must be an exact match as those in the
master FASTA file, and may or may not include the ">" character at
the begining of the header.

Example of list file:
sequence1
sequence2
sequence3
...
sequenceN
'''))
    parser.add_argument(
    '--fasta', '-f', metavar='FASTA_FILE', type=str, required=True,
    help='FASTA file where all the sequences are stored.')
    parser.add_argument(
    '--list', '-l', metavar='LIST', type=str,
    help='file name of the list.')
    parser.add_argument(
    '--records', '-r', metavar='RECORD', nargs="*", type=str,
    help='individual FASTA records.')
    parser.add_argument(
    '--outfile', '-o', default="records.fasta", nargs="?", type=str,
    help='name for output file (default: %(default)s).')
    parser.add_argument(
    '--wrap', '-w', const=100, metavar='N', nargs="?", type=int, default=False,
    help='sequences will be wrapped every N characters (default: %(default)s).')
    parser.add_argument(
    '--stdout', '-s', const=True, metavar="", nargs="?", type=bool, default=False,
    help='if sequences should be printed to screen.')
    args = parser.parse_args()
    if args.list == None and args.records == None:
        parser.print_usage()
        exit("FaSomeRecords.py: error: argument --list/-l or --records/-r is required")
    fasta = readfasta(args.fasta)
    request = {}
    notfound = []
    mylist = []
    if args.list is not None:
        with open(args.list, "r") as l:
            for head in l:
                head = head.rstrip()
                if head[0] == ">":
                    head = head[1:]
                if ifkeyisfound(fasta, head):
                    mylist.append(head) # to preserve order
                    request[head] = fasta[head]
                else:
                    notfound.append(head)
    elif args.records is not None:
        for head in args.records:
            if head[0] == ">":
                head = head[1:]
            if ifkeyisfound(fasta, head):
                mylist.append(head) # to preserve order
                request[head] = fasta[head]
            else:
                notfound.append(head)
    notfound = set(notfound)
    if args.stdout:
        for head in mylist:
            print ">"+head
            if not args.wrap:
                print request[head]
            else:
                print wrapseq(request[head], args.wrap)
    else:
        with open(args.outfile, "w") as o:
            for head in mylist:
                if not args.wrap:
                    o.write(">"+head+"\n")
                    o.write(request[head]+"\n")
                else:
                    o.write(">"+head+"\n")
                    o.write(wrapseq(request[head], args.wrap)+"\n")
                    
        if len(mylist) == 0:
            print "No sequences found"
        else:
            print "%s sequence(s) found" % len(mylist)
            print "%s sequence(s) not found" % len(notfound)
            print "Sequences saved to: "+args.outfile

                

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

def wrapseq(seq, w):
    chunks = []
    interval = map(lambda x: x*w, range((len(seq)/w)+2))
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
