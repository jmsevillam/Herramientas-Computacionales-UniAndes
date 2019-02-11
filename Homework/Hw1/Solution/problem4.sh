wget https://github.com/jmsevillam/Herramientas-Computacionales-UniAndes/raw/master/Data/DataHw1b.zip
unzip DataHw1b.zip
cd DataHw1b
cat file*
grep 'the' file1.txt > new_file1
wc new_file1
grep -i 'the' file1.txt > new_file2
wc new_file2
grep -iw 'the' file1.txt > new_file3
wc new_file3
