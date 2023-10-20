# Force strict variable declaration
use strict;
# Force all warnings
use warnings;

foreach my $key (sort keys %ENV) {
    print "$key = $ENV{$key}\n";
}