# ManualPhylogeny
Script for creating phylogeny by yourself

# The Order you run those scripts
You got two files from DDBJ.
1. OrthoFinder/Results_XXXXXX/Orthogroups/
2. all_seq.fa: `sh OrthoFinder/MSA/makeMSA.sh` (Multiple Sequence Alignment from many fasta files)

You receive these two files and do below in your local.
1. `python3 ManualPhylo_1.py`: you get OG_list.txt & species_list.txt
2. `python3 ManualPhylo_2.py all_seq.fa OG_list.txt`
3. `sh ~/<your OGs directory>/align.sh OG_list.txt`: MAFFT and Trimal
4. `python3 ManualPhylo_3.py OG_list.txt species_list.txt`

If you run all of above four steps, then you send all of your `OGXXXXXX.maffted.trimed.edit.fa` to scorpion.
`rsync -avz ../project/231016/ManualPhylo_data/OG*.maffted.trimed.edit.fa scorpion:~/tree/231016/`

In `~/tree/<your project>/` directory on scorpion, there are `OGXXXXXX.maffted.trimed.edit.fa`, `makerun.py` and `iqtree.sh`
1. `python3 makerun.py`: all `*.maffted.trimed.edit.fa` file whose size is equal to 0 and make `run.nex` file, which is input for iqtree2
2. `sh iqtree2`: run ML tree.
