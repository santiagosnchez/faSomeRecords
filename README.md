# faSomeRecords
Extracts FASTA records from multiFASTA file based on a list of FASTA headers

Inspired by the C++ version of [faSomeRecords](https://github.com/ENCODE-DCC/kentUtils/tree/master/src/utils/faSomeRecords)  from kentUtils

## Python version:

### Download just the program

```bash
wget https://raw.githubusercontent.com/santiagosnchez/faSomeRecords/master/faSomeRecords.py
```

### Download the whole repo and install

```bash
git clone https://github.com/santiagosnchez/faSomeRecords.git
cd faSomeRecords
sudo ln -s `pwd`/faSomeRecords.py /usr/local/bin/faSomeRecords
```

### Help message

```
    python faSomeRecords.py -h
    usage: faSomeRecords.py [-h] --fasta FASTA_FILE [--list LIST] [--records [RECORD ...]] [--outfile [OUTFILE]] [--stdout]
                            [--keep-list-order] [--exclude]

    Retrieves some FASTA records provided a FASTA file and a list or records.

    optional arguments:
      -h, --help            show this help message and exit
      --fasta FASTA_FILE, -f FASTA_FILE
                            FASTA file where all the sequences are stored.
      --list LIST, -l LIST  file name of the list.
      --records [RECORD ...], -r [RECORD ...]
                            individual FASTA records.
      --outfile [OUTFILE], -o [OUTFILE]
                            name for output file (default: records.fasta)
      --stdout, -s          if sequences should be printed to screen.
      --keep-list-order     will keep the list order. The default is to keep the fasta order. (defaut:False)
      --exclude, -e         exclude sequences in the list.

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
```

### Examples

```
# print 3 sequences to screen
./faSomeRecords.py -f examples/example_20_seqs.fa -r seq_1 seq_3 seq_5 --stdout
# keep list input order
./faSomeRecords.py -f examples/example_20_seqs.fa -r seq_10 seq_4 seq_15 --stdout --keep-list-order
# take sequences from a list to default output file
./faSomeRecords.py -f examples/example_20_seqs.fa -l examples/get_these.txt
# exclude sequences in list, print the rest to screen
./faSomeRecords.py -f examples/example_1000_seqs.fa -l examples/exclude_these.txt --stdout
# test a bigger file
./faSomeRecords.py -f examples/example_30000_seqs.fa -r seq_1 seq_3 seq_5 --stdout
```

In the list file you must have only the headers without the `>` character. For example:

```
seq_1
seq_2
seq_3
seq_4
...
seq_1000
```

Although you can leave the `>` character and `faSomeRecords` will remove it for you.

Pretty straight forward.

## Perl version

**No longer maintained**

I recommend using the Python version! Which is the one that will be developed and supported further on.

### Download

    wget https://raw.githubusercontent.com/santiagosnchez/faSomeRecords/master/faSomeRecords.pl

### Help message

    perl faSomeRecords.pl -h

    Try:
    perl faSomeRecords.pl -f multiFASTA   FASTA file with sequences
		                  -l list         A list of headers that match -f
            	          -o outfile      Name your output file
