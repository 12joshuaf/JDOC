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
		$value =~ s/(\r\n|\n|\r|\f)/<br>/g;
		$FORM{$name} = $value;
	}



# Then sends the emails

open (MESSAGE,"| /usr/sbin/sendmail -t");


	print MESSAGE "Content-type: text/html; cht=iso-8859-1\n";
	print MESSAGE "To: jdayocon\@skidmore.edu\n"; # Don't forget to escape this @ symbol!
	print MESSAGE "From: " . Experimental_results . ", reader\n";
	
	print MESSAGE "Subject: Full experimental results from $FORM{email} \n\n";
	
	print MESSAGE "Sent by: $FORM{name} ($FORM{email}).<br>";
	print MESSAGE "Age: $FORM{age}.<br>";
	print MESSAGE "Gender: $FORM{gender}.<br><br>";
	print MESSAGE "Native language: $FORM{nativeLanguage}.<br>";
	print MESSAGE "Additional languages: $FORM{additionalLanguages}.<br><br>";
	print MESSAGE "Musical background: $FORM{musicalBackground}.<br>";
	print MESSAGE "Vocal experience: $FORM{vocalExperience}.<br><br>";
	print MESSAGE "Payment preference: $FORM{payment}.<br><br>";
	print MESSAGE "Full results here; see also short results below.<br><br>";
	print MESSAGE "$FORM{results}<br><br>";
	print MESSAGE "<br><br>Short results follow.<br><br>";
	print MESSAGE "$FORM{short_results}";

close (MESSAGE);

&confirmation_screen; #method call
} 



#The code then goes on to generate the confirmation screen

sub confirmation_screen {

print "Content-type: text/html\n\n";

print <<EndStart;

	<html>
	<head>
	<title>Thank You</title>
	</head>
	
	<body bgcolor="#ffffff" text="#000000">
	
	
	<br>
	<p>You have completed the experiment.</p>
	
	<hr>
	
	<br>Please take a moment here to add any comments or questions; let us know
	<br>if you encountered any difficulties or would like to offer any feedback
	<br>to help improve future versions of this study.<br><br>
	<form id="post_mortem" method="post" action="//jeremydayoconnell.com/cgi-bin/Post_mortem.cgi"><input type="hidden" name="email" value="$FORM{email}"><input type="hidden" name="validationCode" value="$FORM{validationCode}"><textarea form="post_mortem" name="post_mortem" rows="5" cols="75"></textarea><br><br><br><input type="submit"></form>


	
	
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