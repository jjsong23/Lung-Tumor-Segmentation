# Extracts all image data from a given 3D CT image set
# Inputs: Path to the 3D CT image folder, path to desired output folder

import os
from dicompylercore import dicomparser

def dicom_to_jpg(path, output_path):
    
    files = os.listdir(path)
    
    for i in range(len(files)):
        
        dcm = dicomparser.DicomParser(os.path.join(path,files[i]))
        
        img = dcm.GetImage();
        
        img_name = 'slice_' + str(i) + '.jpg'
        
        img.point(lambda i:i*(1./256)).convert('L').save(os.path.join(output_path,img_name))
        
def dicom_to_tif(path, output_path):
    
    files = os.listdir(path)
    
    for i in range(len(files)):
        
        dcm = dicomparser.DicomParser(os.path.join(path,files[i]))
        
        img_name = 'slice_' + str(i) + '.jpg'
        
        img = dcm.GetImage();
        
        img.save(os.path.join(output_path,img_name))
