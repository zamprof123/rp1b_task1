# =========== Call libraries =========== #

import os
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# =========== Function Accumulator =========== #

def open_file(location):
    file = open(os.path.expanduser(location), "r")
    return pd.read_csv(file, sep="\t", header=None) # Open file as a pd data frame

def vcf_to_csv(vcf_file_path, csv_file_path):
    with open(vcf_file_path, "r") as vcf_file:
        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in vcf_file:
                if line.startswith("##"):
                    continue
                elif line.startswith("#"):
                    header = line.strip("#").strip().split("\t")
                    csv_writer.writerow(header)
                else:
                    data = line.strip().split("\t")
                    csv_writer.writerow(data)

            return data # Covert data in .vcf to .csv

# =========== Coverage files (3 samples) =========== #

coverage_sample1 = open_file("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/coverage_1kb_means.bed")
coverage_sample2 = open_file("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/coverage_1kb_means_2.bed")
coverage_sample3 = open_file("~/Desktop/(MSc) BIOINFORMATICS/MACHINE LEARNING RESEARCH PROJECT (1B)/task2/coverage_1kb_means_3.bed")

column_names = ["reference_genome", "start", "end", "coverage_mean"]
coverage_sample1.columns = column_names
coverage_sample2.columns = column_names
coverage_sample3.columns = column_names
print(coverage_sample1.head()) # Ensure changed headers
print(f"Make sure shape = correct: {np.shape(coverage_sample1), np.shape(coverage_sample2), np.shape(coverage_sample3)}") # ((4412, 4), (4412, 4), (4412, 4))

# =========== Identifying differences between all 3 =========== #

# First, mean depth per 1kb to 3dp
mean_coverage_sample1 = round(coverage_sample1.coverage_mean.mean(), 3) # 50.106
mean_coverage_sample2 = round(coverage_sample2.coverage_mean.mean(), 3) # 49.997
mean_coverage_sample3 = round(coverage_sample3.coverage_mean.mean(), 3) # 49.997
print(f"Samples 1, 2 and 3 mean: {mean_coverage_sample1}, {mean_coverage_sample2}, {mean_coverage_sample3}")

def coverage_mean_to_list(coverage_file):
    coverage_mean_list = coverage_file["coverage_mean"].tolist()
    return coverage_mean_list

# Min and Max average coverage per 1kb (3dp)
print(f"Sample 1 max: {round(coverage_sample1["coverage_mean"].min(), 3)}") # 25.306
print(f"Sample 2 max: {round(coverage_sample2["coverage_mean"].min(), 3)}") # 25.306
print(f"Sample 3 max: {round(coverage_sample3["coverage_mean"].min(), 3)}") # 25.306

print(f"Sample 1 min: {round(coverage_sample1["coverage_mean"].max(), 3)}") # 106.097 #!#
print(f"Sample 2 min: {round(coverage_sample2["coverage_mean"].max(), 3)}") # 62.035
print(f"Sample 3 min: {round(coverage_sample3["coverage_mean"].max(), 3)}") # 63.129

# Let´s have a look in descending order how to the coverage_mean behaves across all 3 samples
# Only print if coverage > mean
sort_sample1 = sorted(coverage_sample1["coverage_mean"]) [::-1]
sort_sample2 = sorted(coverage_sample2["coverage_mean"]) [::-1]
sort_sample3 = sorted(coverage_sample3["coverage_mean"]) [::-1]

print(f"Sample 1 values: {[value for value in sort_sample1 if value > coverage_sample1.coverage_mean.mean()]}") # Top 3 highest: 106.097, 103.016, 101.711
print(f"Sample 2 values: {[value for value in sort_sample2 if value > coverage_sample2.coverage_mean.mean()]}") # Top 3 highest: 62.035, 61.855, 61.808
print(f"Sample 3 values: {[value for value in sort_sample3 if value > coverage_sample3.coverage_mean.mean()]}") # Top 3 highest: 63.129, 61.819, 61.203

# =========== Lets take a closer look on sample 1 =========== #
# We know that there are a couple of outliers in coverage depth per 1kb in sample 1
# Lets for example look at the position where the max value is

max_coverage_mean = coverage_sample1["coverage_mean"].max()
max_row = coverage_sample1.loc[coverage_sample1["coverage_mean"] == max_coverage_mean]
start_pos = max_row["start"].values
end_pos = max_row["end"].values

print(f"Maximum coverage_mean (file1): {max_coverage_mean}, Start: {start_pos}, End: {end_pos}") # For depth = 106.097 - p.1246001 to p.1247000

# =========== Visual representation to see whether sample 1  =========== #

def plot_coverage(depth_file, plot_file=""):

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(depth_file["start"], depth_file["coverage_mean"], marker="o", linestyle="", color="b")
    ax.set_xlabel("Position (start of 1kbp bin)")
    ax.set_ylabel("Mean Depth")
    ax.set_title("Mean Depth of Coverage in 1kbp Bins")
    fig.tight_layout()

    if plot_file:
        fig.savefig(plot_file)
        print(f"Plot saved to '{plot_file}'.")
    else:
        plt.show()

    return fig, ax

fig, ax = plot_coverage(coverage_sample1) # Sample 1 scatterplot - clear visual outliers (positions?)
fig, ax = plot_coverage(coverage_sample2) # Sample 2 scatterplot
fig, ax = plot_coverage(coverage_sample3) # Sample 3 scatterplot

# =========== Calling Variants .vcf to .csv conversion =========== #
# In order to filter through the data frames, it´s easier to do it if .vcf into .csv

vcf_file_path_1 = "~/Desktop/VCFs/variants_1.vcf"
csv_file_path_1 = "~/Desktop/variants_1.csv"

vcf_file_path_2 = "~/Desktop/VCFs/variants_2.vcf"
csv_file_path_2 = "~/Desktop/variants_2.csv"

vcf_file_path_3 = "~/Desktop/VCFs/variants_3.vcf"
csv_file_path_3 = "~/Desktop/VCFs/variants_3.csv"

# =========== .csv conversion (Sample 1) =========== #

vcf_to_csv(os.path.expanduser(vcf_file_path_1), os.path.expanduser(csv_file_path_1))
vcf_csv_path_1 = os.path.expanduser(csv_file_path_1)
vcf_data_1 = pd.read_csv(vcf_csv_path_1)
print(vcf_data_1.head())
print(f"vcf_data_1 type: {type(vcf_data_1)}") # Check it´s changed into a pd data frame
print(f"vcf_data_1 shape: {np.shape(vcf_data_1)}") # Check shape = correct (1847, 10)

# =========== .csv conversion (Sample 2)  =========== #

vcf_to_csv(os.path.expanduser(vcf_file_path_2), os.path.expanduser(csv_file_path_2))
vcf_csv_path_2 = os.path.expanduser(csv_file_path_2)
vcf_data_2 = pd.read_csv(vcf_csv_path_2)
# print(vcf_data_2.head())
# print(type(vcf_data_2))

# =========== .csv conversion (Sample 3) =========== #

vcf_to_csv(os.path.expanduser(vcf_file_path_3), os.path.expanduser(csv_file_path_3))
vcf_csv_path_3 = os.path.expanduser(csv_file_path_3)
vcf_data_3 = pd.read_csv(vcf_csv_path_3)
# print(vcf_data_3.head())
# print(type(vcf_data_3))

# =========== Lets take a closer look on sample 1 AGAIN! =========== #
# Through looking at the vcf files in Bash we know that Sample 1 carries INDELs in the "ALT" allele column
# Identifying positions where "ALT" allele == INDEls

positions_allele = vcf_data_1["ALT"]
indels = [allele for allele, ref in zip(positions_allele, vcf_data_1["REF"]) if len(allele) != len(ref)] # I almost died perfecting this ngl
positions = vcf_data_1.loc[vcf_data_1["ALT"].isin(indels)]
indel_pos_dict = {allele: positions.loc[positions["ALT"] == allele, "POS"].values.tolist() for allele in indels}
print(f"INDEL to Position dictionary: {indel_pos_dict}") # Map each INDEL to it´s respective position

# Now let´s look at how many INDELs are there
# Also, we need to know throughout what distance across sample 1´s genome they occur (in bp, != kbp)
indel_counter = 0
for indel in indels:
    indel_counter += 1

min_distance = [min(value) for key, value in indel_pos_dict.items()]
max_distance = [max(value) for key, value in indel_pos_dict.items()]
first_last_distance = (min(min_distance), max(max_distance))

print(f"Total number of INDELs in sample 1: {indel_counter}") # 57 INDELs in sample 1
print(f"Distance from first to last INDELs: {first_last_distance[0]} to {first_last_distance[1]}") # p.1245282 to p.1255000

# Map between those two regions (p.1245282 to p.1255000)
# See % of INDELs vs non-INDELs (on .csv converted .vcf file)
indel_count = 0
allele_count = 0
start_position = 1245282
end_position = 1255000

for index, row in vcf_data_1.iterrows():
    if start_position <= row["POS"] <= end_position:
        if len(row["ALT"]) > 1:
            indel_count += 1
        else:
            allele_count += 1

percentage_of_indels = (indel_count / (allele_count + indel_count)) * 100
print(f"Percentage of INDELs in rare 10kb region: {round(percentage_of_indels, 3)}% ") # 12.821%

# =========== Certifying 1kb coverage discrepancy =========== #

mean_coverage_1 = coverage_sample1.loc[(coverage_sample1["start"] >= start_position) & (coverage_sample1["end"] <= end_position),"coverage_mean"].mean() # 99.042x (!)
mean_coverage_2 = coverage_sample2.loc[(coverage_sample1["start"] >= start_position) & (coverage_sample1["end"] <= end_position),"coverage_mean"].mean() # 50.25x
mean_coverage_3 = coverage_sample3.loc[(coverage_sample1["start"] >= start_position) & (coverage_sample1["end"] <= end_position),"coverage_mean"].mean() # 50.369x
print(f"Mean coverage in INDEL-dominated region: {round(mean_coverage_1, 3), round(mean_coverage_2, 3), round(mean_coverage_3, 3)}")

# =========== Now let´s look at site specific (1 base) Depth =========== #
# Lets examine the depth from the depth.txt file attained in Bash (for Sample 1)

sample_1_depth = open_file("~/Desktop/depth_1.txt") # Pd data frame for depth of sample 1
sample_1_depth.columns = ["Reference genome", "Position", "Depth"] # Add columns
print(f"Depth file (Sample 1) type: {type(sample_1_depth)}") # Ensure = pd data frame for merging
print(f"Vcf file type (Sample 1): {type(vcf_data_1)}") # # Ensure = pd data frame for merging

# Look at the depth at each INDEL
sample_1_depth["key"] = sample_1_depth["Position"]
vcf_data_1["key"] = vcf_data_1["POS"]
new_df = pd.merge(sample_1_depth, vcf_data_1, on="key", how="inner")
indels_2 = new_df[new_df["ALT"].str.len() > 1]
indel_to_depth = {
    indel: indels_2[indels_2["ALT"] == indel]["Depth"].tolist()
    for indel in indels_2["ALT"].unique()
}

values_indel_to_depth = [min(value) for key, value in indel_to_depth.items()]
coverage_indels = coverage_sample1[(coverage_sample1["start"] >= start_position) & (coverage_sample1["end"] <= end_position)]["coverage_mean"].tolist() # Need to look at coverage too ("&" satisfying combination of two conditions)

print(f"Minimum depth value from all INDELs: {min(values_indel_to_depth), max(values_indel_to_depth)}") # depth = (76, 114)
print(f"INDEL to Depth dictionary: {indel_to_depth}") # Each INDEL mapped to it´s respective depth (if INDEL == repeated more than once, tuple size for key="INDEL" += 1)
print(f"INDEL coverage means: {coverage_indels}") # 9718 bases - ~10kb but not really - so output = 9 values
print(f"Min and max depth per 1kb values within INDELs: {min(coverage_indels), max(coverage_indels)}") # (91.275, 106.097)


# =========== Supplementary code (not really relevant) =========== #
# Computation of One-Way ANOVA f_oneway (Same independent variable - "depth" across > 2 dependent variables)
# Just for fun - we need statistical validation
# Check the VCF file = correct by not mapping the same bp
anova_result = f_oneway(coverage_mean_to_list(coverage_sample1), coverage_mean_to_list(coverage_sample2), coverage_mean_to_list(coverage_sample3))

alignment_counter = 0
null_alignment_counter = 0
for index, row in vcf_data_1.iterrows():
    if row["REF"] == row["ALT"]:
        alignment_counter += 1
    else:
        null_alignment_counter += 1

total_positions = alignment_counter + null_alignment_counter
percentage = (alignment_counter / total_positions) * 100

print(f"Percentage of alignment from Sample 1 per bp: {percentage}%") # 0.0% = GOOD
print(f"One Way ANOVA between 1kbp coverage mean: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}") # F-statistic = 1.2526558619429813, p-value = 0.2857787701020065
