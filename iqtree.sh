#!/bin/bash

##Save the initial time for output file
start_time=`date +%s`
##echo $start_time >> output_iqtree.txt

iqtree2 -sp run.nex -nt AUTO -bb 1000

sleep 2
end_time=`date +%s`
##echo $end_time >> output.txt
run_time=$((end_time - start_time))
echo $run_time >> output_iqtree.txt
