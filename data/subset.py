import h5py
import numpy as np
import matplotlib.pyplot as plt

# download So2Sat full data set (https://mediatum.ub.tum.de/1454690)

# pick one data set: training.h5 or validation.h5
fileOfChoice = '~/git/lcz42/validation.h5'

# load the data set
fin = h5py.File(fileOfChoice, 'r')

# create new subset
fout = h5py.File('subset_lcz42.h5', 'w')

samples = 2400

sen1 = np.array(fin['sen1'])
fout.create_dataset('sen1', data=sen1[0:samples,:,:,:])

sen2 = np.array(fin['sen2'])
fout.create_dataset('sen2', data=sen2[0:samples,:,:,:])

lab = np.array(fin['label'])
fout.create_dataset('label', data=lab[0:samples,:])

