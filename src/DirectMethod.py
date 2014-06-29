# numpyの利用
import numpy as np
from numpy import genfromtxt

# モジュール属性 argv を取得するため
import sys

# 各種デバッグモード
DEBUG_ALL = 0
DEBUG_FILE_INPUT = 0
DEBUG_MAKE_MATRIX = 0
DEBUG_CALC = 0
DEBUG_OUTPUT = 0

# コマンドライン引数の使用準備とエラー処理
argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数
if(argc != 3):
	print("usage: python DirectMethod.py FILENAME YATSUHASHI_NUM")
dataFileName = argvs[1]
yatsuhashi_num = int(argvs[2])

# ファイルからの入力をrawDataに格納
dataFilePath = "../data/" + dataFileName
rawData = genfromtxt(dataFilePath, delimiter='\t')
if(DEBUG_ALL or DEBUG_FILE_INPUT):
	print(rawData)

# rawDataを行列に変換
prefernceMatrix = np.zeros([yatsuhashi_num, yatsuhashi_num]) # 対角成分も0
# prefernceMatrix = np.identity(yatsuhashi_num) # 対角成分は1
for dataOneRow in rawData[1:]:
	prefernceMatrix[dataOneRow[0] - 1][dataOneRow[1] - 1] += 1

prefernceMatrix = np.transpose(rawData)

if(DEBUG_ALL or DEBUG_MAKE_MATRIX):
	print(prefernceMatrix)

# 解の計算
rankingVector = np.ones([yatsuhashi_num, 1]) # r_0 = (1, 1, ..., 1)^T とする
normRankingVector = np.linalg.norm(rankingVector)
normPrefernceMatrix = np.linalg.norm(prefernceMatrix)

rankingVector /= normRankingVector # r_0 / |r_0| を計算

for i in range(100):
	rankingVector = np.dot(prefernceMatrix, rankingVector) / normPrefernceMatrix
if(DEBUG_ALL or DEBUG_CALC):
	print(rankingVector)

# 出力
for i in range(yatsuhashi_num):
	sys.stdout.write("No.")
	print('%2d' % (i + 1), ":", '%2d' % (rankingVector.argmax() + 1), end = " ")
	if(DEBUG_ALL or DEBUG_OUTPUT):
		print("->" , rankingVector[rankingVector.argmax()])
	else:
		print("")
	rankingVector[rankingVector.argmax()] *= -1

