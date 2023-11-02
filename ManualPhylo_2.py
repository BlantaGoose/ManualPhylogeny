##ManualPhylo_1.pyの続き

import sys
from Bio import SeqIO

path = "../231016/ManualPhylo_data/"

fasta_in = sys.argv[1]					#１番目の引数には上記のall_seq.faなどfastaファイルを指定する
query_in = sys.argv[2]					#２番目の引数には上記のOG_list.txtなどオーソログファイルを指定する

for q in open(query_in, "r"):		  		#オーソログファイルを開いて1行づつ読み込む
	query = q.split()				            #スペース毎に切りとってリスト形式でqueryに保存する
	f = open(path + query[0], 'w')			#最初の列(OG名）と同じ名前のファイルを作成する
	for record in SeqIO.parse(fasta_in, 'fasta'):	  #fastaファイルを開くSeqIOを使ってパースする(1項目づつ読み込む）
		id_part = record.id			                      #fastaのID部分を読み込む
		desc_part = record.description		            #fastaのdescription部分を読み込む
		seq = record.seq			                        #fastaの配列部分を読み込む
		for i in range(len(query)):		                #オーソログファイル中の各OGに含まれる配列数を数えて、その分繰り返す(python2の人はrange を x rangeにする)
			if desc_part == query[i] :	                #オーソログファイルの配列descriptionとfastaの配列descriptionが一致したら、、、
				fasta_seq = '>' + desc_part + '\n' + seq + '\n'		  #fasta形式に整え
				print(fasta_seq)                                  	#標準出力にfastaを出力（進行状況把握用）
				f.write(str(fasta_seq))	                            #各OGファイルにfastaを出力
	f.close()

##できたOGファイルは、align.shやOG_list.txtと同じ場所に
##align.shのある場所までいき、作動。cwdを231016/ManualPhylo_dataにしないとtrimalが作動せず、イライラ
