#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);

# The following accepts the data from the form and splits it into its component parts

if ($ENV{'REQUEST_METHOD'} eq 'POST') {

	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	
	@pairs = split(/&/, $buffer);
	
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$FORM{$name} = $value;
	}



# Then sends the email 

open (MESSAGE,"| /usr/sbin/sendmail -t");


	print MESSAGE "Content-type: text/html; cht=iso-8859-1\n";
	print MESSAGE "To: $FORM{email}\n";
	print MESSAGE "BCC: jdayocon\@skidmore.edu\n";
	print MESSAGE "From: " . Validation . "\n";
	print MESSAGE "Reply-to: " . Validation . "\n";
	
	print MESSAGE "Subject: Validation code for experiment \n\n";
	
	print MESSAGE "<br><br>Please use the following one-time validation code to continue the experiment:<br><br>$FORM{validationCode}<br><br>";


close (MESSAGE);

&confirmation_screen; #method call
} 



# The code then goes on to generate the confirmation screen

sub confirmation_screen {

print "Content-type: text/html\n\n";

print <<EndStart;

	<html>
	<head>
	<title>Thank You</title>
	</head>
	
	<body bgcolor="#ffffff" text="#000000">
	
	<h1>Thank You</h1>
	
	<p>Validation code has been sent.</p>
	
	<hr>
	
	
EndStart

# here's some more stuff i could have but don't
#	print "<p>You wrote:</p>\n";
#	print "<blockquote><em>$FORM{comment}</em></blockquote>\n\n";
#	print "<p>Hidden field was:</p>\n";
#	print "$FORM{hidden_field}";
	
print <<EndHTML;
	
	</body>
	</html>

EndHTML

exit(0);
}