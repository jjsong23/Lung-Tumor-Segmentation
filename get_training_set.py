# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:38:04 2022

@author: Fred
"""

import dicom2nifti
import nibabel as nib
import numpy as np
import pydicom
import os
from convert_to_nifti import seg2nifti

train_raw = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\raw data\train_raw'

train_patients = os.listdir(train_raw)

test_folder = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\Dataset\imagesTs'

label_folder = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\Dataset\labelsTr'

train_folder = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\Dataset\imagesTr'

for patient in train_patients:

    print(patient)
    
    rejoinder = os.listdir(os.path.join(train_raw,patient))[0]
    
    path = os.path.join(train_raw,patient,rejoinder)
    
    dicoms = os.listdir(path)
    
    serial = patient[6:10]
    
    name = "lung_"+str(serial)+".nii.gz"
    
    ct = os.path.join(path,dicoms[0]);
    
    output_path_ct = os.path.join(train_folder,name)
    
    dicom2nifti.dicom_series_to_nifti(ct, output_path_ct)
    
    seg = seg2nifti(os.path.join(path,dicoms[2]),os.path.join(path,dicoms[0]))
    
    nib.save(seg, os.path.join(label_folder,name))
    
    print(patient + " Complete")