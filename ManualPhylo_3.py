##align.shした後

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO

path = "../231016/ManualPhylo_data/"

query_in = sys.argv[1]                            #1番目の引数には上記のOG_list.txtなどオーソログファイルを指定する
species_in = sys.argv[2]                          #2番目の引数にはOG_list.txtと同じ順番で種名を記述したファイルを指定する

sp_list = []
for sp in open(species_in, "r"):                     #種名ファイルを開く
	sp_list.extend(sp.split())                            #スペース毎に切りとってリスト形式でsp_listに保存する

for q in open(query_in, "r"):                     #オーソログファイルを開いて1行づつ読み込む
	query = q.split()                             #スペース毎に切りとってリスト形式でqueryに保存する

	f = open(path + query[0]+".maffted.trimed.edit.fa", 'w')
	for record in SeqIO.parse(path + query[0]+".maffted.trimed.fa", 'fasta'): #fastaファイルを開くSeqIOを使ってパースする(1項目づつ読み込む）
		desc_part = record.description            #fastaのdescription部分を読み込む
		seq = record.seq                          #fastaの配列部分を読み込む
		desc_part_new = desc_part.split()[0]

		for i in range(len(query)-1):              #オーソログファイル中の各OGに含まれる配列数を数えて、その分繰り返す

			if desc_part_new == query[i+1] :            #オーソログファイルの配列descriptionとfastaの配列descriptionが一致したら、、、
				fasta_seq = '>' + sp_list[i] + '\n' + seq + '\n'     #配列名を該当する種名に置き換えて、fasta形式に整えて
				print(fasta_seq)                  #標準出力にfastaを出力（進行状況把握用）
		f.write(str(fasta_seq))           #各OGファイルにfastaを出力
	f.close()

##scorpionでnano run.nexを変更し、以下を実行
##iqtree –sp run.nex –nt AUTO –bb 1000
