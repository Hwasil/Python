#!/bin/bash

mkdir practice
touch practice_1.txt; chmod 475 practice_1.txt
touch practice_2.txt; chmod 464 practice_2.txt
touch practice_3.txt; chmod 575 practice_3.txt
touch practice_4.txt; chmod 755 practice_4.txt
touch practice_5.txt; chmod 700 practice_5.txt

for ((i=1;i<=100;i++));do touch test_${i}_file;done
for ((i=1;i<=100;i++));do chmod 700 test_${i}_file;done

for ((i=1;i<=50;i++));do mkdir d_${i}test;done
for ((i=1;i<=50;i++));do sudo chown root:root d_${i}test;done 
