# Force strict variable declaration
use strict;
# Force all warnings
use warnings;

my $input = <STDIN>;
chomp($input);

if ($input =~ /^[01]+5$/) {
    print "Your input has been accepted.\n";
} else {
    print "Your input has not been accepted.\n";
}