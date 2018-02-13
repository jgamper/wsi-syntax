import os
import pickle
import time
import glob

from modules import single_sampler

###

data_dir = '/home/peter/Dropbox/publish-final/WSI_sampler_data'

###

files = glob.glob(os.path.join(data_dir, '*.tif'))

bg_dir = os.path.join(data_dir, 'background')
mask_dir = os.path.join(data_dir, 'annotation')

###

for file in files:
    sampler = single_sampler.Single_Sampler(wsi_file=file, background_dir=bg_dir, annotation_dir=mask_dir, level0=40)
    sampler.save_background_visualization(savedir='./bg_vis')
