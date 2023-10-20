#!/usr/bin/perl

use strict;
use warnings;
use CGI qw(:standard);
use Fcntl qw(:flock SEEK_END);

my $cgi = CGI->new;
my $board_file = 'board.txt';

# Output HTML header with UTF-8 charset
print $cgi->header(-charset => 'utf-8');
print $cgi->start_html(
    -title => 'Simple Board',
    -encoding => 'utf-8',
    -style => {-src => 'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css'}
);

# Check if the form has been submitted
if ($cgi->param('send') eq 'Submit') {
    my $name = $cgi->param('name');
    my $message = $cgi->param('message');
    my $timestamp = localtime;
    my $entry = "$name\t$timestamp\t$message\n";

    # Write the new entry at the beginning of the file
    open my $fh, "+<", $board_file or die "Can't open $board_file: $!";
    flock($fh, LOCK_EX);
    my $content = do {local $/; <$fh>};
    seek($fh, 0, 0);
    print $fh $entry, $content;
    truncate($fh, tell($fh));
    flock($fh, LOCK_UN);
    close $fh;
}

# Read and display the contents of the board
open my $fh, "<", $board_file or die "Can't open $board_file: $!";
my @lines = <$fh>;
close $fh;

print $cgi->h1({
    -class => 'text-5xl font-bold my-4'
}, 
    'Simple Board'
);
print $cgi->start_form(
    -class => 'space-y-4',
);

print $cgi->textfield(
    -name => 'name',
    -placeholder => 'Your Name',
    -class => 'border border-gray-300 p-2 rounded w-full'
);

print $cgi->textarea(
    -name => 'message',
    -placeholder => 'Your Message',
    -rows => 5,
    -columns => 40,
    -class => 'border border-gray-300 p-2 rounded w-full'
);

print $cgi->submit(
    -name => 'send',
    -value => 'Submit',
    -class => 'bg-blue-500 text-white px-4 py-2 rounded'
);

print $cgi->end_form;

print $cgi->div({-class => 'space-y-4'}, 
    map {
        my ($name, $timestamp, $message) = split /\t/;
        $cgi->div(
            {-class => 'border border-gray-300 p-4 rounded'},
            $cgi->strong($name),
            $cgi->span({-class => 'text-gray-500 text-sm ml-2'}, $timestamp),
            $cgi->p($message)
        );
    } @lines
);

print $cgi->end_html;
