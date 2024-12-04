# =========== Call libraries =========== #

import os
import numpy as np
import pandas as pd


# =========== Open file as a pandas data frame =========== #

def open_file(location):
    file = open(os.path.expanduser(location), "r")
    return pd.read_csv(file, sep="\t", header=None)


# =========== Open .csv, then change column name and replace the old version located in the respective directory =========== #

depth_file1 = open_file("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/Depth and Coverage/depth_1.csv")
depth_file2 = open_file("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/Depth and Coverage/depth_2.csv")
depth_file3 = open_file("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/Depth and Coverage/depth_3.csv")

ref_columns = ["reference sequence", "position", "depth"]
depth_file1.columns = ref_columns
depth_file2.columns = ref_columns
depth_file3.columns = ref_columns

print(f"shape: {np.shape(depth_file1), np.shape(depth_file2), np.shape(depth_file3)}")
print(f"headers: {depth_file1.head()}")
print(depth_file1)

output_path1 = ("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/Depth and Coverage/depth_1.csv")
output_path2 = ("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/Depth and Coverage/depth_2.csv")
output_path3 = ("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/Depth and Coverage/depth_3.csv")

depth_file1.to_csv(output_path1, index=False)
depth_file2.to_csv(output_path2, index=False)
depth_file3.to_csv(output_path3, index=False)