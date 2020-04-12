#%%
import os
import glob
from pathlib import Path
import re
import argparse
from time import time

datapath = 'data'

parser = argparse.ArgumentParser()
parser.add_argument("-n", action="store", dest="datapath", default='data', required=True, help="Path with files")
results = parser.parse_args()
datapath = str(results.datapath)

#%%
start = time()
se_regex = r'[sS]{1,2}\d{1,2}[eE]\d{1,2}'
timestamp_regex = r'\d{1,2}:\d{1,2}:\d{1,2}'
multimedia_extension = ['ts', 'avi', 'mkv']

# %%
all_files_w_sub = glob.glob(f'{datapath}/*')
all_files = [os.path.basename(path) for path in all_files_w_sub]
all_files = [x for x in all_files if '.' in x]
all_files_se = [x for x in all_files if re.match(se_regex, x)]

txs = [x for x in all_files if '.' in x if x.split('.')[-1] =='tx']



for tx in txs:
    new_file = ''
    tx_name = ''.join(tx.split('.')[:-1])
    tx_se = re.findall(se_regex, tx)[0]
    multimedia_se =  [re.findall(se_regex, x)[0] for x in all_files_se if x.split('.')[-1] in multimedia_extension]
    txt_se =  [re.findall(se_regex, x)[0] for x in all_files_se if x.split('.')[-1] == 'txt']
    if tx_se  in multimedia_se:
        
        if tx_se not in txt_se:
            with open(f'{datapath}/{tx}') as fp:
                line = fp.readline()
                while line:
                    text = line.strip()
                    if re.match(timestamp_regex, text):
                        # print(text)
                        new_file += f'\n{text}'
                    else:
                        new_file += f' {text}'
                    line = fp.readline()
            
            with open(f'{datapath}/{tx_name}.txt', 'w') as the_file:
                the_file.write(new_file)
print(f' Evaluation time: {time() -start}')
