# faSomeRecords
Extracts FASTA records from multiFASTA file based on a list of FASTA headers

Inspired by the C++ version of [faSomeRecords](https://github.com/ENCODE-DCC/kentUtils/tree/master/src/utils/faSomeRecords)  from kentUtils

## Python version:

### Download

    wget https://raw.githubusercontent.com/santiagosnchez/faSomeRecords/master/faSomeRecords.py

### Help message

    python faSomeRecords.py -h
    usage: FaSomeRecords.py [-h] --fasta FASTA_FILE [--list LIST]
                                [--records [RECORD [RECORD ...]]]
                                [--outfile [OUTFILE]] [--wrap [N]] [--stdout ]

    Retrieves some FASTA records provided a FASTA file and a list or records.

    optional arguments:
      -h, --help            show this help message and exit
      --fasta FASTA_FILE, -f FASTA_FILE
                            FASTA file where all the sequences are stored.
      --list LIST, -l LIST  file name of the list.
      --records [RECORD [RECORD ...]], -r [RECORD [RECORD ...]]
                            individual FASTA records.
      --outfile [OUTFILE], -o [OUTFILE]
                            name for output file (default: records.fasta).
      --wrap [N], -w [N]    sequences will be wrapped every N characters (default: False).
      --stdout [], -s []    if sequences should be printed to screen.
    
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
                          
### Example

    python faSomeRecords.py -f allMySeqs.fasta -l IneedTheseSeqs.txt -o filteredSeqs.fasta
    # wrap every 50 characters
    python faSomeRecords.py -f allMySeqs.fasta -r seq1 seq2 seq4409 -w 50
    # print to screen 
    python faSomeRecords.py -f allMySeqs.fasta -r seq1 seq2 -w 100 --stdout

In the list file (e.g. `IneedTheseSeqs.txt`) you must have only the headers without the `>` character. For example:

    seq1
    seq2
    seq3
    seq4
    ...
    seqN

Pretty straightforward.

## Perl version

I recommend using the Python version! Which is the one with will be developed and supported.

### Download

    wget https://raw.githubusercontent.com/santiagosnchez/faSomeRecords/master/faSomeRecords.pl

### Help message

    perl faSomeRecords.pl -h
    
    Try:
    perl faSomeRecords.pl -f multiFASTA   FASTA file with sequences
		                  -l list         A list of headers that match -f
            	          -o outfile      Name your output file 
