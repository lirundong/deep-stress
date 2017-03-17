# -*- coding: utf8 -*-
import src.prepare_data as Data
import numpy as np

if __name__ == '__main__':
    print('Loading data...')
    temp, stress, max_temp, max_stress = Data.load_and_interp()
    print('Cropping samples...')
    temp, stress = Data.crop_samples(temp, stress)
    print('Dumping data set to binary...')
    np.savez_compressed('../Data/consol_crops',
                        temp=temp,
                        stress=stress,
                        max_temp=max_temp,
                        max_stress=max_stress,)
