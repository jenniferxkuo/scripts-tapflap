#### 2019 TAP/FlAP ULTRASOUND PROJECT ####
## Script for moving acquisitions into folders sorted by the type of tap/flap
## inter-rater disagreement. 
## Jennifer Kuo July 2019

## TO run: python move-for-recoding.py EXPDIR CODEFILE
## Where: EXPDIR is the directory containing the experiment files (acquisitions), 
## and CODEFILE is the csv file with all the coding results.

import argparse
import shutil
import pandas as pd
import os

# read in arguments
parser = argparse.ArgumentParser()
parser.add_argument("expdir",
					help="Experiment directory containing all subjects'\
						  caches and metadata in separate folders"
					)
parser.add_argument("codefile", action="store",
					help="Name of csv file with coding results"
					)

args = parser.parse_args()

expdir = args.expdir
codefile = args.codefile


coding_results = pd.read_csv(codefile,sep=',')

for i,j in coding_results.iterrows():
	acq = j[1]
	err_type = j[15]
	start_dir = os.path.join(expdir,acq)
	out_dir = os.path.join('FL02_recode',err_type)
	if os.path.exists(start_dir):	
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		shutil.move(start_dir,out_dir)
	