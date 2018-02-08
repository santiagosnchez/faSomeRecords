# faSomeRecords
Extracts FASTA records from multiFASTA file based on a list of FASTA headers

Inspired by the C++ version of faSomeRecords[https://github.com/ENCODE-DCC/kentUtils/tree/master/src/utils/faSomeRecords]  from kentUtils

## Download

    wget https://raw.githubusercontent.com/santiagosnchez/faSomeRecords/master/faSomeRecords.pl

## Help message

    perl faSomeRecords.pl -h
    
    Try:
    perl faSomeRecords.pl -f multiFASTA   FASTA file with sequences
		                      -l list         A list of headers that match -f
            	            -o outfile      Name your output file 
                          
## Example

    perl faSomeRecords -f allMySeqs.fasta -l IneedTheseSeqs.txt -o filteredSeqs.fasta

In the list file (e.g. `IneedTheseSeqs.txt`) you must have only the headers without the `>` character. For example:

    seq1
    seq2
    seq3
    seq4
    ...
    seqN

Pretty straightforward.
