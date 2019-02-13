cd DataHw1b
awk {'print;'} file3.txt
awk '/Física/' file3.txt
awk {'print $3,$5;'} file3.txt
awk 'BEGIN {print "Email\t Name\t Age\t Career";}
 {print $2,"\t",$3,"\t",$4,"\t",$NF;}
 ' file3.txt
awk '$4>20' file3.txt | wc -l
