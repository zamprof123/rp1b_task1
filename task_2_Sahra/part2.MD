b)
Look at the VCFs; one of these samples looks different. Can you identify which one, and explain why you think it is different?
Sample 1 is different to sample 2 and 3 because sample 1 presents Indel mutations whereas sample 2 and 3 present SNP mutations only.

c) What do you think could explain this?

Sample 1 exhibits unique indel variations absent in Samples 2 and 3, alongside SNP mutations similar to the other samples. These indels could represent structural mutations in the genome or artifacts caused by contamination. However, without knowing if these regions fall within coding sequences, the first step is to evaluate the reliability of the detected indels.

Indels and Their Potential Impact
Indels—caused by mechanisms like replication slippage, DNA repair errors, transposon activity, or stress-induced events—can lead to significant genomic changes, particularly when affecting coding regions. Compared to SNPs, indels are more likely to disrupt gene function or genome stability due to larger structural changes. Since the coding status of these regions in Sample 1 is unknown, assessing the reliability of the variant calls is crucial before making further interpretations.

Variant Calling Metrics
The reliability of indels in Sample 1 was evaluated using metrics such as IDV, IMF, DP, VDB, and RPBZ:

Indel Depth Value (IDV): Reflects the number of reads supporting an indel. The average IDV for Sample 1 was 46.9%, indicating moderate support. However, knowing the total reads for each indel is necessary to fully evaluate confidence.
Indel Maximum Fraction (IMF): Expresses IDV as a fraction of total reads (DP). The average IMF of 48.8% offers further context but remains insufficient for definitive conclusions.
Depth of Coverage (DP): Ranged between 80–120, suggesting high genome representation, though not necessarily validating variant authenticity.
Variant Distance Bias (VDB): Aimed at identifying splice-site artifacts, only 20% of variants had a VDB score ≥0.5, suggesting potential reliability for these indels, while the rest might reflect splicing-related false positives.
Read Position Bias Z-score (RPBZ): Measures sequencing biases. Values closer to 0 indicate higher confidence; however, 66% of indels showed significant deviation, indicating technical factors may compromise reliability.
Overall, the metrics indicate that while some indels might be genuine, technical biases and low support for many variants raise doubts about their authenticity.

Potential Causes of Indels in Sample 1
Alignment Issues: Short-read misalignment, especially in repetitive or ambiguous regions, could lead to spurious indel calls.
Contamination: Splice-site artifacts detected in RNA sequencing may indicate contamination. Mycobacterium tuberculosis (M.tb) lacks introns and does not undergo RNA splicing, so splice-site artifacts likely stem from host cells or other contaminating organisms.
Argument for Contamination

Splice-site artifacts in RNA-seq data arise from errors in detecting splicing events. Since M.tb’s genome lacks introns, it does not undergo RNA splicing, meaning any detected splice events likely originate from contaminating organisms (e.g., host cells or other bacteria). Further investigation is necessary to confirm contamination as a source.

Likelihood of Biological Causes
Although replication slippage, DNA repair errors, transposon activity, or stress-induced mutations could explain the indels, these scenarios are less plausible given the weak support from variant annotations. The metrics more strongly point to alignment errors or contamination as the primary causes.
