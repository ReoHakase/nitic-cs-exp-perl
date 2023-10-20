#!/usr/bin/perl

use strict;
use warnings;
use CGI qw(:standard);

# Specify the file to store the counter
my $counter_file = 'counter.txt';

# Retrieve and update the counter
open my $fh, '+<', $counter_file or die "Can't open $counter_file: $!";
my $count = <$fh>;
chomp($count);  # Remove any newline character
$count = 0 unless $count =~ /^\d+$/;  # Reset count if it's not a valid number
$count++;
seek $fh, 0, 0;
print $fh $count;
truncate $fh, tell($fh);  # Truncate the file to the current position
close $fh;

# Output HTML
print header;
print start_html('Counter Page');
print "This page has been viewed $count times.";
print end_html;
