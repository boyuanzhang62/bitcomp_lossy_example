import numpy as np


data = np.fromfile('/home/bozhan/dataset/00_CESM-ATM_yx_1800x3600=6480000/TSMX_1_1800_3600.f32', dtype=np.float32)  # Load data from binary file
print(data.shape)
data = data.astype(np.float64)  # Convert to float64

data.tofile('tmp.f64')  # Save data to binary file