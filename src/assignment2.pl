# Force strict variable declaration
use strict;
# Force all warnings
use warnings;
# Use feature say
use feature qw(say);

# Declare array of days of the week
my @week = qw(Monday Tuesday Wednesday Thursday Friday Saturday Sunday);
my @input;
my $index = 0;

# Insert user input into array until user presses Ctrl+D
while (<STDIN>) {
    chomp;
    push @input, $_;
}

# Print the day of the week for each input in ascending order
foreach my $input (sort {$a <=> $b} @input) {
    say "week[$input]: $week[$input - 1]";
}