import pandas as pd
import os

complete = pd.DataFrame()

directories = ["1H/", '1H_obstacle/', '2nd/', '2nd_obstacle/', '3rd/', '3rd_obstacle/', 'CA/', 'CA_doubles/', 'CA_move/', 'CA_obstacle/']
LoS = [1,0,1,0,1,0,1,1,1,0]

for d in range(len(directories)):
	files = os.listdir(directories[d])	
	for i in files:
		antennaPosition = i.split('_')[0]
		distance = i.split('_')[1]
		df = pd.read_csv(directories[d] + i, delimiter='\t')
		df['distance'] = distance
		df['antenna'] = antennaPosition
		df['LoS'] = LoS[d]
		df.to_csv(directories[d] + i, sep='\t', index=False)
		complete = pd.concat([complete, df])
	complete.to_csv(directories[d] + "complete_data.csv", sep='\t', index=False)
	complete = pd.DataFrame()
