#!/usr/bin/perl

use strict;
use warnings;
use CGI qw(:standard);

my $cgi = CGI->new;

# Output HTML header with UTF-8 charset
print $cgi->header(-charset => 'utf-8');
print $cgi->start_html(
    -title => 'Form Submission',
    -encoding => 'utf-8'
);

# Check if the form has been submitted
if ($cgi->param('status') eq 'send') {
    my $body = $cgi->param('body');
    print $cgi->p("\"$body\" had been submitted.");
}

# Output the form HTML
print $cgi->start_form;
print $cgi->textarea(-name=>'body', -rows=>10, -columns=>50);
print $cgi->br;
print $cgi->submit(-name=>'status', -value=>'send');
print $cgi->end_form;

print $cgi->end_html;
