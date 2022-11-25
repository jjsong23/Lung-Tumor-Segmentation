# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:49:23 2022

@author: Fred
"""

import dicom2nifti
import nibabel as nib
import numpy as np
import pydicom
import os

def seg2nifti(seg_path, ct_path):
    
    seg_path = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\Small Batch\LUNG1-001\09-18-2008-StudyID-NA-69331\300.000000-Segmentation-9.554\1-1.dcm'

    ct_path = r'C:\Users\Fred\Desktop\Tumor Segmentation Project\Small Batch\LUNG1-001\09-18-2008-StudyID-NA-69331\0.000000-NA-82046'

    seg = pydicom.read_file(seg_path)
         
    mask3D = seg.pixel_array;

    def collapse_seg_array(array, ct_path):
            
        mask3D = array;
            
        ct_files = os.listdir(ct_path)
            
        arrays_per_slice = int(len(mask3D[:,1,1])/len(ct_files));

        collapsed_array = np.zeros((len(ct_files),512,512));

        s = 0;

        for i in range(arrays_per_slice,len(mask3D[:,1,1]),arrays_per_slice):
            
            collapsed_slice = np.zeros((512,512))
                                       
            for j in range(i- arrays_per_slice, i):
                
                collapsed_slice = collapsed_slice + mask3D[j,:,:];
                
            collapsed_array[s] = collapsed_slice;
            
            s += 1;
        
        return collapsed_array

    collapsed_array = collapse_seg_array(mask3D, ct_path)

    transposed = collapsed_array.transpose(1,2,0)

    return nib.Nifti1Image(transposed, affine=np.eye(4))

    

