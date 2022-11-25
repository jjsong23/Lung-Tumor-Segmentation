# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:39:55 2022

@author: Fred
"""

import dicom2nifti
import nibabel as nib
import numpy as np
import pydicom
import os
from convert_to_nifti import seg2nifti


test_raw = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\raw data\test_raw'

test_patients = os.listdir(test_raw)

test_folder = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\Dataset\imagesTs'

for patient in test_patients:

    print(patient)
    
    rejoinder = os.listdir(os.path.join(test_raw,patient))[0]
    
    path = os.path.join(test_raw,patient,rejoinder)
    
    dicoms = os.listdir(path)
    
    serial = patient[6:10]
    
    name = "lung_"+str(serial)+".nii.gz"
    
    ct = os.path.join(path,dicoms[0]);
    
    output_path_ct = os.path.join(test_folder,name)
    
    dicom2nifti.dicom_series_to_nifti(ct, output_path_ct)
    
    print(patient + " Complete")