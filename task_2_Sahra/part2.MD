b)
Look at the VCFs; one of these samples looks different. Can you identify which one, and explain why you think it is different?

Sample 1 differs from samples 2 and 3 because it contains indel mutations, while samples 2 and 3 only present SNP mutations.

c) 

Sample 1 exhibits indel variations not present in samples 2 and 3, in addition to SNP mutations common to all three samples. These indels may represent structural genomic mutations or artifacts from contamination. However, to assess their significance, the first step is to evaluate the reliability of the detected indels, especially in relation to coding regions.

Indels are typically caused by mechanisms such as replication slippage, DNA repair errors, transposon activity, or stress-induced events. These mutations can lead to significant genomic changes, especially when they affect coding regions. In comparison to SNPs, indels tend to disrupt gene function or genome stability more severely due to their larger structural impact. Given that the coding status of the regions in Sample 1 is unknown, evaluating the reliability of the indels before drawing any conclusions is essential.

The reliability of the indels in Sample 1 was evaluated using several variant calling metrics:

Indel Depth Value (IDV): This metric reflects the percentage of reads supporting an indel. In Sample 1, the average IDV was 46.9%, suggesting moderate support. However, the total number of reads for each indel should be considered to fully assess confidence.

Indel Maximum Fraction (IMF): The IMF is the fraction of total reads (DP) that support the indel. Sample 1 had an average IMF of 48.8%, which is still not enough to make definitive conclusions about the indels' authenticity.

Depth of Coverage (DP): The depth of coverage in Sample 1 ranged from 80 to 120, which generally indicates high genome representation. However, this alone does not confirm the accuracy of variant calls.

Variant Distance Bias (VDB): This metric is used to identify potential splice-site artifacts. In Sample 1, 20% of variants had a VDB score ≥ 0.5, suggesting that a portion of the indels might be genuine, while others may be splice-related false positives.

Read Position Bias Z-score (RPBZ): This score indicates sequencing bias. In Sample 1, 66% of indels showed significant deviation from a Z-score of 0, suggesting potential technical issues with the sequencing.

Overall, the metrics indicate that while some indels in Sample 1 could be real, there are concerns about their authenticity due to technical biases and insufficient read support for many variants.

Several factors may explain the indels in Sample 1:

Alignment Issues: Short-read misalignment, particularly in repetitive or ambiguous regions, can lead to false indel calls.

Contamination: Splice-site artifacts detected in RNA sequencing data suggest the possibility of contamination. Since Mycobacterium tuberculosis lacks introns and does not undergo RNA splicing, the detected splice events are more likely to come from contaminating organisms, such as host cells or other bacteria.

Splice-site artifacts are common in RNA-seq data when splicing events are misidentified. Since Mycobacterium tuberculosis lacks introns, any splice-site artifacts must originate from contaminating organisms, such as host cells or other bacteria. Further investigation is needed to confirm contamination as the source of these artifacts.

While biological causes like replication slippage, DNA repair errors, transposon activity, or stress-induced mutations could explain the indels, these are less likely given the weak support from the variant annotations. The available metrics suggest that alignment errors or contamination are the more probable causes.

Overall, the indels in Sample 1 could be genuine mutations or artifacts, potentially arising from alignment issues or contamination. Given the moderate support for these indels, further validation is needed to confirm their authenticity, with contamination being a likely cause due to splice-site artifacts.
