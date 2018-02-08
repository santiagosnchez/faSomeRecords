#!/usr/bin/perl
# inspired in faSomeRecords

if (grep { /^-he{0,1}l{0,1}p{0,1}$/ } @ARGV){
	die "
Try:
perl faSomeRecords.pl -f multiFASTA   FASTA file with sequences
		      -l list         A list of headers that match -f
            	      -o outfile      Name your output file 
\n";
}

# read arguments and files

my @lines=();
my @list=();
my $outfile;

if (my ($indF) = grep { $ARGV[$_] =~ /^-f$/ } 0 .. $#ARGV){
	open(F,"<",$ARGV[$indF+1]) or die "Cannot open $ARGV[$indF+1]\n";
	while(<F>){
		next if (/^\s*$/);
		chomp($_);
		push @lines, $_;
	}
	close F;
} else {
	die "-f flag not found. Try with: -f your_file\n";
}

if (my ($indO) = grep { $ARGV[$_] =~ /^-o$/ } 0 .. $#ARGV){
	$outfile = $ARGV[$indO+1];
	open(OUT, ">", $outfile) or die "Cannot open $outfile\n";
} else {
	die "-o flag not found. Try with: -o output_file\n";
}

if (my ($indL) = grep { $ARGV[$_] =~ /^-l$/ } 0 .. $#ARGV){
	open(L,"<",$ARGV[$indL+1]) or die "Cannot open $ARGV[$indL+1]\n";
	while(<L>){
		next if (/^\s*$/);
		chomp($_);
		push @list, $_;
	}
	close L;
}

# store seqs in hash table

my %data=();
my @indH = grep { $lines[$_] =~ /^>/ } 0 .. $#lines;
for my $i (0 .. $#indH){
	if ($i != $#indH){
		$data{substr(@lines[$indH[$i]],1,length(@lines[$indH[$i]]))} = join('', @lines[ $indH[$i]+1 .. $indH[$i+1]-1 ]);
	} else {
		$data{substr(@lines[$indH[$i]],1,length(@lines[$indH[$i]]))} = join('', @lines[ $indH[$i]+1 .. $#lines ]);
	}
	print "Reading sequence... $i        \r";
}
print "\n";

# loop through list

my $cf=0;
my $cm=0;
my @miss=();
for my $head (@list){
	if (exists $data{$head}){
		print OUT ">$head\n" . "$data{$head}\n";
		++$cf;
	} else {
		push @miss, $head;
		++$cm;
	}
}
close OUT;

if ($cm == 0){
	print "All $cf found and saved to $outfile\n";
} else {
	print "Found $cf sequences, saved to $outfile\n";
	open(M,">","missing.txt");
	foreach(@miss){ print M $_ . "\n" }
	print "The list of sequences that were not found is saved to \"missing.txt\"\n";
}

