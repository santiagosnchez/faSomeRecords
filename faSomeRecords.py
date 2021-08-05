#!/usr/bin/env python3
# faSomeRecords.py

import argparse
import textwrap
import sys
<<<<<<< HEAD


def main():
    # parse arguments
    parser = argparse.ArgumentParser(prog="FaSomeRecords.py", formatter_class=argparse.RawTextHelpFormatter,
                                     description="Retrieves some FASTA records provided"
                                                 "a FASTA file and a list or records.", epilog=textwrap.dedent('''\
    Records can be specified providing a list file with --list/-l
    or one by one in the command line using --records/-r.
    The elements in the list must be an exact match as those in the
    master FASTA file, and may or may not include the ">" character at
    the beginning of the header.
    Example of list file:
    sequence1
    sequence2
    sequence3
    ...
    sequenceN
    '''))
    parser.add_argument('--fasta', '-f', metavar='FASTA_FILE', type=str, required=True,
                        help='FASTA file where all the sequences are stored.')
    parser.add_argument('--list', '-l', metavar='LIST', type=str, help='file name of the list.')
    parser.add_argument('--records', '-r', metavar='RECORD', nargs="*", type=str, help='individual FASTA records.')
    parser.add_argument('--outfile', '-o', default="records.fasta", nargs="?", type=str,
                        help='name for output file (default: %(default)s)')
    parser.add_argument('--stdout', '-s', action="store_true", default=False,
                        help='if sequences should be printed to screen.')
    parser.add_argument('--keep', '-k', action="store_true", default=False, help="keep the order in the list.")
    parser.add_argument('--exclude', '-e', action="store_true", default=False,
                        help="Exclude these sequences from the final output.")
    args = parser.parse_args()

    if args.list is None and args.records is None:
        parser.print_usage()
        sys.exit("FaSomeRecords.py: error: argument --list/-l or --records/-r is required")
    if args.list is not None and args.records is None:
        with open(args.list, "r") as l:
            heads = l.read().splitlines()
        if ">" not in heads[0]:
            heads = [">" + h for h in heads]
    elif args.records is not None and args.list is None:
        heads = args.records
        if ">" not in heads[0]:
            heads = [">" + h for h in heads]

    requested = len(heads)
    joinheads = "|" + "|".join(heads) + "|"

    found = 0
    not_found = []

    if args.exclude:
        if args.keep:
            print("--exclude will maintain the order of the original FASTA by default")
        with open(args.outfile, "w") as out:
            with open(args.fasta, "r") as f:
                for line in f:
                    if line.startswith(">") and line.strip("\n") not in heads:
                        seq = 1
                        out.write(line)
                        found += 1
                    elif line.startswith(">"):
                        not_found += [line[1:-1]]
                        seq = 0
                    else:
                        if seq == 1:
                            out.write(line)

    elif args.keep and not args.exclude:
        store = {}
        with open(args.fasta, "r") as f:
            for line in f:
                if line[0] == ">":
                    if "|" + line[:-1] + "|" in joinheads:
                        h = line[:-1]
                        seq = 1
                        store[h] = ''
=======
import gzip
from re import match
from random import choice
from collections import OrderedDict

def write_to_file(store, outfile, found, requested, heads):
    '''
    Function to write fasta to file and print summary message
    to screen.
    '''
    if len(store) > 0:
        with open(outfile, "w") as o:
            for head in heads:
                o.write(">"+head+"\n"+store[head])
        if found == 0:
            print("No sequences found")
        else:
            print(f"Found {found} sequence(s)")
            if found > requested:
                print(f"Found {found-requested} sequence(s) more than requested")
            elif requested > found:
                if requested-found > 0:
                    print(f"Could not find {requested-found} sequence(s)")
                    #print("\n".join(not_found))
            print(f"Sequences saved to: {outfile}")
    else:
        if found == 0:
            print("No sequences found")
        else:
            print(f"Found {found} sequence(s)")
            if found > requested:
                print(f"Found {found-requested} sequence(s) more than requested")
            elif requested > found:
                if requested-found > 0:
                    print(f"Could not find {requested-found} sequence(s)")
                    #print("\n".join(not_found))
            print(f"Sequences saved to: {outfile}")

def parse_fasta(handle, stdout, outfile, order, exclude, requested, joinheads, heads):
    '''
    Main FASTA parser
    '''
    # start seq counter
    found = 0
    # count each record
    total = 0
    # not found list
    not_found = []
    # start ordered dictionary
    store = OrderedDict()
    # check if list order is requested
    if order:
        if exclude:
            for line in handle:
                # checks for header
                if line[0] == ">":
                    # count all
                    total += 1
                    if "|" + line[1:].rstrip() + "|" in joinheads:
                        seq = 0
                    else:
                        h = line[1:].rstrip()
                        seq = 1
                        store[h] = ''
                        found += 1
                else:
                    if seq == 1:
                        store[h] += line
            requested = total - requested
        else:
            for line in handle:
                # checks for header
                if line[0] == ">":
                    # count all
                    total += 1
                    if "|" + line[1:].rstrip() + "|" in joinheads:
                        h = line[1:].rstrip()
                        seq = 1
                        store[h] = ''
>>>>>>> update_exl
                        found += 1
                    else:
                        seq = 0
                else:
                    if seq == 1:
                        store[h] += line
<<<<<<< HEAD
        if found == 0:
            print("No sequences found")
        else:
            if args.stdout:
                for h in heads:
                    if store.get(h):
                        sys.stdout.write(h + "\n" + store[h])
                    else:
                        sys.stdout.write(h + "\n" + "#not found\n")
                        not_found += [h]
            else:
                with open(args.outfile, "w") as o:
                    for h in heads:
                        if store.get(h):
                            o.write(h + "\n" + store[h])
                        else:
                            sys.stdout.write(h + "\n" + "#not found\n")
                            not_found += [h]
                print("Found {} sequence(s)".format(found))
                if found > requested:
                    print("Found {} sequence(s) more than requested".format(found - requested))
                elif requested > found:
                    print("Could not find {} sequence(s)".format(requested - found))
                    print("\n".join(not_found))
                print("Sequences saved to: " + args.outfile)
    else:
        if args.stdout:
            with open(args.fasta, "r") as f:
                for line in f:
=======
        # go through header list and print
        if stdout:
            for head in heads:
                print(">"+head+"\n"+store[head], end='')
        else:
            # write to file
            write_to_file(store, outfile, found, requested, heads)
    else:
        # check if output is to stdout
        if stdout:
            # if the function is to exclude rather than include
            if exclude:
                # it basically inverts the function if exclude is enabled
                for line in handle:
                    # checks for header
                    if line[0] == ">":
                        if "|" + line[1:].rstrip() + "|" in joinheads:
                            # just count matches if found
                            seq = 0
                        else:
                            # print everything else
                            seq = 1
                            print(line, end='')
                            found += 1
                    else:
                        # writes the sequence portion
                        if seq == 1:
                            print(line, end='')
            else:
                for line in handle:
                    # checks for header
>>>>>>> update_exl
                    if line[0] == ">":
                        if "|" + line[1:].rstrip() + "|" in joinheads:
                            # start writing to screen if found
                            seq = 1
<<<<<<< HEAD
                            sys.stdout.write(line)
                            found += 1
                        else:
                            not_found += [line[:-1]]
                            seq = 0
                    else:
                        if seq == 1:
                            sys.stdout.write(line)
            if found == 0:
                print("No sequences found")
        else:
            with open(args.outfile, "w") as o:
                with open(args.fasta, "r") as f:
                    for line in f:
                        if line[0] == ">":
                            if "|" + line[:-1] + "|" in joinheads:
=======
                            print(line, end='')
                            found += 1
                        else:
                            # count missing if no match
                            # not_found += [line[1:].rstrip()]
                            seq = 0
                    else:
                        if seq == 1:
                            print(line, end='')
        else:
            with open(outfile, "w") as o:
                if exclude:
                    # it basically inverts the function if exclude is enabled
                    for line in handle:
                        # checks for header
                        if line[0] == ">":
                            # count all
                            total += 1
                            if "|" + line[1:].rstrip() + "|" in joinheads:
                                # just count matches if found
                                seq = 0
                            else:
                                # print everything else
                                seq = 1
                                o.write(line)
                                found += 1
                        else:
                            # writes the sequence portion
                            if seq == 1:
                                o.write(line)
                    requested = total - requested
                else:
                    for line in handle:
                        # checks for header
                        if line[0] == ">":
                            total += 1
                            if "|" + line[1:].rstrip() + "|" in joinheads:
                                # start writing to screen if found
>>>>>>> update_exl
                                seq = 1
                                o.write(line)
                                found += 1
                            else:
<<<<<<< HEAD
                                not_found += [line[1:-1]]
=======
                                # count missing if no match
                                # not_found += [line[1:].rstrip()]
>>>>>>> update_exl
                                seq = 0
                        else:
                            if seq == 1:
                                o.write(line)
<<<<<<< HEAD
            if found == 0:
                print("No sequences found")
            else:
                print("Found {} sequence(s)".format(found))
                if found > requested:
                    print("Found {} sequence(s) more than requested".format(found - requested))
                elif requested > found:
                    print("Could not find {} sequence(s)".format(requested - found))
                    print("\n".join(not_found))
                print("Sequences saved to " + args.outfile)


if __name__ == '__main__':
=======
                write_to_file(store, outfile, found, requested, heads)

# main function
def main():
    # parse arguments
    parser = argparse.ArgumentParser(prog="FaSomeRecords.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Retrieves some FASTA records provided a FASTA file and a list or records.",
        epilog=textwrap.dedent('''\
    Records can be sepcified providing a list file with --list/-l
    or one by one in the command line using --records/-r.

    All sequences are now kept in the same input order. So the --keep flag no longer applies

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
    help='name for output file (default: %(default)s)')
    parser.add_argument(
    '--stdout', '-s', action="store_true", default=False,
    help='if sequences should be printed to screen.')
    parser.add_argument(
    '--keep-list-order', action="store_true", default=False,
    help="will keep the list order. The default is to keep the fasta order. (defaut:False)")
    parser.add_argument(
    '--exclude', '-e', action="store_true", default=False,
    help="exclude sequences in the list.")
    args = parser.parse_args()

    # check input files and arguments
    if args.list == None and args.records == None:
        parser.print_usage()
        sys.exit("FaSomeRecords.py: error: argument --list/-l or --records/-r is required")
    # get all headers from input
    if args.list is not None:
        with open(args.list, "r") as l:
            heads = l.read().splitlines()
        if heads[0][0] == ">":
            heads = [ h[1:] for h in heads ]
    elif args.records is not None:
        heads = args.records
        if heads[0][0] == ">":
            heads = [ h[1:] for h in heads ]

    # get number of requested records
    requested = len(heads)
    # prepare regex for header lookup
    joinheads = "|" + "|".join(heads) + "|"

    # main function
    with open(args.fasta) as f:
        parse_fasta(f, args.stdout, args.outfile, args.keep_list_order, args.exclude, requested, joinheads, heads)

if __name__ == "__main__":
>>>>>>> update_exl
    main()
