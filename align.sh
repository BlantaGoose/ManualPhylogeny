#!/bin/sh
#$ -S /bin/bash
#$ -cwd
#$ -v PATH
awk '{print($1)}' $1 | while read x; do #引数に前述のOG_list.txtなどのOGリストを指定する。
#	mafft --auto $x > $x.maffted.fa
	mafft --anysymbol $x > $x.maffted.fa
	trimal -in $x.maffted.fa -out $x.maffted.trimed.fa -htmlout $x.maffted.trimed.fa.html -automated1
done
