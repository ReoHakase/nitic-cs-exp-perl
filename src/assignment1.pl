# Force strict variable declaration
use strict;
# Force all warnings
use warnings;

# Print a message to the user
print "Enter an integer N1: ";
my $n1 = <STDIN>;
print "Enter an integer N2: ";
my $n2 = <STDIN>;

# Omit the newline character from the end of the input
chomp($n1);
chomp($n2);

#  Calculate sum of integers between N1 and N2
my $sum = 0;
for (my $i = $n1; $i <= $n2; $i++) {
    $sum += $i;
}

print "Sum of integers between N1 $n1 and N2 $n2 is equal to $sum.\n";