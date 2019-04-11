#!/usr/bin/perl

=pod

=head1 NAME

gb2bed.pl -- Genbank -> BED

=head1 SYNOPSIS

gb2bed.pl [options] filename

Options:
--help -h display this message
--input -i NCBI GenBank file
--out -o filename of bed output. [STDOUT]
--filter -f GenBank primary tag that will be filtered, may be set to 'gene', 'CDS', 'rRNA', etc.
--keep -k GenBank primary tag will be keep. Default is CDS. [CDS]

Examples:

perl gb2bed.pl -i seq.gb -o seq.bed
perl gb2bed.pl -i seq.gb -k CDS -o seq.bed
perl gb2bed.pl seq.gb > seq.bed

=head1 DESCRIPTION

Use this program to generate bioconductor friendly BED files from NCBI GenBank.
Six columns will be extracted:
1. chrom - name of the chromosome or scaffold. Any valid seq_region_name can be used, and chromosome names can be given with or without the 'chr' prefix.
2. chromStart - Start position of the feature in standard chromosomal coordinates (i.e. first base is 0).
3. chromEnd - End position of the feature in standard chromosomal coordinates
4. name - Label to be displayed under the feature, if turned on in "Configure this page". [locus_tag]
5. score - A score between 0 and 1000. [0]
6. strand - defined as + (forward) or - (reverse).

=head1 AUTHOR

Chun-Hui, Gao (gaoch@thelifesciencecentury.com)
Copyright (c) 2015 www.thelifesciencecentury.com.

=cut

use strict;
use Data::Dumper;
use Pod::Usage;
use Bio::SeqIO;
use Getopt::Long;

my ($help, $genbank_input, $output, @filters, @keep);

my $ok= GetOptions( 'help|h' => \$help,
'input|i=s' => \$genbank_input,
'filter|f=s' => \@filters,
'keep|k=s' => \@keep,
'out|o=s' => \$output );
pod2usage(2) if $help || !$ok;

$genbank_input = shift @ARGV unless ($genbank_input );

@keep = ('gene') unless $#keep >= 0;

open *IN, "< $genbank_input " or die pod2usage(2); my $out; if ($output) { open $out, "> $output" or die "Can't open file $output:$@\n";
}
else {
$out = *STDOUT;
}

my %filter;
map {$filter{$_}++} @filters;
my %keep;
map {$keep{$_}++} @keep;
my $in = Bio::SeqIO->new(-fh => \*IN, -format => "genbank");
while ( my $seq = $in->next_seq() ) {
my $chr = join(".", $seq->accession, $seq->version); #modifiquei para juntar n_de_acesso e versao

my @all_SeqFeatures = $seq->get_all_SeqFeatures;

#~ warn "# working on $chr\n";
if ($#filters >= 0){
@all_SeqFeatures = grep { !defined $filter{$_->primary_tag} } @all_SeqFeatures;
}
if ($#keep >= 0) {
@all_SeqFeatures = grep { defined $keep{$_->primary_tag} } @all_SeqFeatures;
}

# abort if there are no features
warn "$chr has no features, skipping\n" and next
if $#all_SeqFeatures < 0; for my $feature ( @all_SeqFeatures ) { my ($start, $end, $name, $strand); $start = $feature->start - 1; # bed base is 0, while genbank is 1
$end = $feature->end;
($name) = $feature->get_tag_values('locus_tag');
$strand = $feature->strand;
$strand = $strand < 0 ? '-' : '+'; print $out join("\t", $chr, $start, $end, $name, 0, $strand), "\n"; } } 
