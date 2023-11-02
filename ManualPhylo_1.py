##analysis_manual.pptxの#46も参照

##AFTER you made MSA file(all_seq.fa) in DDBJ with makeMSA.sh

##時間は10secほど

import numpy as np
import pandas as pd
import os

path = "231016"

OGs = pd.read_table("../" + path + "/Original_data/Orthogroups/Orthogroups.tsv")

new = pd.DataFrame()
with open("../" + path + "/Original_data/Orthogroups/Orthogroups_SingleCopyOrthologues.txt") as fin:
	for line in fin:
		li = line.rstrip()
		new = pd.concat([new, OGs[OGs["Orthogroup"] == li]])
print(new)
new.to_csv("../" + path + "/Processed_data/ManualPhylo_data/OG_list.txt", sep = " ", index = False, header = False)

##OG_list.txtと同じ順番の種名リストであるspecies_list.txtを作成
##できたOG_list.txtに、DDBJで作ったall_seq.faで配列情報を与える。

li = []
allspe = OGs.columns.tolist()
allspe2 = allspe[1:len(allspe)]
with open("../" + path + "/ManualPhylo_data/species_list.txt", "w") as file:
   for column_name in allspe2:
       file.write("%s\n" % column_name)
