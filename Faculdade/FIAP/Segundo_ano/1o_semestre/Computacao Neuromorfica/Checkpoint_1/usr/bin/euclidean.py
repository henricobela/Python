

import pandas as pd
import math
import numpy as np
import warnings
import os


warnings.filterwarnings("ignore")

ALL_PATHS = os.path.abspath(r"/opt/")
RUN_PROGRAM = True


def get_csv_files(path):
	dirs = []
	for arq in os.listdir(path):
		if arq.endswith(".csv"):
			full_dir = os.path.join(path, arq)
			dirs.append(full_dir)
	return dirs


def euclidean_distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def coord_calc(csv_path):
	lista = []

	arquivo = pd.read_csv(csv_path)
	arquivo["x1"] = np.nan
	arquivo["y1"] = np.nan
	arquivo["x2"] = np.nan
	arquivo["y2"] = np.nan

	for i in range(len(arquivo)):
		x1, y1 = arquivo.source[i].split(",")
		x2, y2 = arquivo.destiny[i].split(",")
		arquivo["x1"][i] = x1
		arquivo["y1"][i] = y1
		arquivo["x2"][i] = x2
		arquivo["y2"][i] = y2

	arquivo = arquivo.drop(columns = ["date", "source", "destiny"])
    
	for i in arquivo.index:
		x1, y1, x2, y2 = arquivo.loc[i]
		lista.append(euclidean_distance(int(x1), int(y1), int(x2), int(y2)))
    
	arquivo["distance"] = np.nan
	arquivo["distance"] = lista

	menor_distancia = arquivo.distance.min()
	pontos = arquivo.loc[arquivo['distance'] == menor_distancia, ["x1", "y1", "x2", "y2"]].values.tolist()

	return pontos, menor_distancia


while RUN_PROGRAM:
		try:
			csvs_path = get_csv_files(ALL_PATHS)
			for csv_path in csvs_path:
				pontos, menor_distancia = coord_calc(csv_path)
				print(f"O arquivo: {csv_path}, apresenta a menor distancia: {menor_distancia}, entre os pontos {pontos}")
				if csv_path.endswith(".csv"):
					os.remove(csv_path)

			RUN_PROGRAM = False

		except Exception as error:
			print(error)
		
