b)
Look at the VCFs; one of these samples looks different. Can you identify which one, and explain why you think it is different?
Sample 1 is different to sample 2 and 3 because sample 1 presents Indel mutations whereas sample 2 and 3 present SNP mutations only.

c) What do you think could explain this?

Sample 1 shows unique variations at indel positions not found in Samples 2 and 3, though it also presents SNP mutations similar to the other samples. SNPs are more common than indels and generally result from chemical changes at the molecular level.

SNPs occur at single base positions and are more common in genetically stable regions, typically under weak selective pressure. They arise through mechanisms such as replication errors, spontaneous mutations (e.g., deamination or oxidative damage), and environmental factors like UV radiation or chemical mutagens. Horizontal gene transfer (HGT) and stress-induced mutagenesis can also contribute by introducing mismatches or activating error-prone DNA polymerases. SNPs may also arise through natural selection, with advantageous mutations, such as those conferring antibiotic resistance, becoming fixed. These processes explain the SNP mutations in all three samples. 

But what about the indels in sample 1?

Indels (insertions or deletions of nucleotides) are typically caused by replication slippage, DNA repair mechanisms, transposon activity, or stress-induced errors. Compared to single nucleotide polymorphisms (SNPs), indels are generally more likely to cause significant changes to a genome's function. This is because indels can lead to larger structural alterations in the DNA sequence, potentially having broader and more impactful consequences on gene function and genome stability, especially when occurring in coding regions. However, in this case, we are uncertain about the location of the coding regions, so we cannot definitively determine whether the indels have caused significant changes to the sample’s genome.

The inferences drawn are based on the data provided by the variant calling commands used, focusing on the IDV, IMF, DP, VDB, and RPBZ for each indel in Sample 1.

Indel Depth Value (IDV) represents the maximum number of raw reads supporting each indel, reflecting how many sequencing reads align with the identified indel. A high IDV means greater support for the indel, increasing confidence in its presence. On average, the IDV was around 45-50% across all 50 indels identified. However, to fully assess whether this is a strong value, we would need to know the total number of reads for each indel.

The next variant annotation, Indel Maximum Fraction (IMF), represents the maximum fraction of raw reads supporting the indel at a specific position. Calculating the average IMF across all indels provides more context for assessing the reliability of the indel calls than just looking at IDV alone. IMF expresses IDV as a fraction of the total reads (DP), adjusting for coverage depth, which is crucial for evaluating variant call accuracy. Higher IMF values indicate stronger support for the indel, suggesting greater confidence that the variant is real rather than a result of sequencing errors or contamination. On average, the IMF across all 50 indels in Sample 1 was approximately 50%. This value alone does not definitively confirm or refute the reliability of the indels but provides useful context.

Depth of Coverage (DP) refers to the total number of sequencing reads that cover a specific position in the genome, indicating how well the position is represented in the sequencing data compared to a reference genome. A higher DP typically correlates with greater confidence in variant calling. In this case, the DP ranges from 80-120, suggesting high confidence in the data.

VDB is the variant distance bias for filtering splice-site artifacts in RNA sequencing data which is caused by splicing events that can cause misleading results. Only 20% (10 out of 50) of the variants have a VDB score of 0.5 or higher, suggesting these are more likely to be genuine variants. Higher VDB values indicate a lower likelihood of splice-site artifacts, while the remaining 80% may be false positives caused by splicing. 

Lastly, I examined the Read Position Bias Z-score (RPBZ), which results from a Mann-Whitney U-test assessing any bias in the position of reads supporting a variant. This can indicate sequencing errors or biases, such as alignment issues, that may affect variant accuracy. The closer the RPBZ value is to 0, the better. Essentially, RPBZ measures the influence of technical factors, like read alignment and sequencing methods, on the variant calling process. I've defined a significant deviation from zero as a value less than -0.5 or greater than 0.5. In Sample 1, 17 out of the 50 indels exceed this threshold. This means that only about 34% of the indels can be confidently considered genuine variant calls, while the remaining 66% may be influenced by technical factors.

The analysis of the indels in Sample 1 presents mixed results. VDB and RPBZ suggest that many variants may not be genuine, with 20% likely real and 66% potentially influenced by technical biases. While Depth of Coverage (DP) indicates a wide spread of the genome, it does not necessarily support genuine variant calling. Indel Maximum Fraction (IMF) and Indel Depth Value (IDV) provide around 50% support, offering some context but not definitive confidence. Overall, technical factors raise concerns about the authenticity of many variants, though some annotations show moderate reliability.

So back to the question. What could cause the indels occurring in sample 1.

1.	Alignment Issues: The mapping of short reads to the reference genome can sometimes be inaccurate if the reads align to multiple regions of the genome or if there are repetitive regions in the genome.
2.	The presence of splice-site artifacts in Mycobacterium tuberculosis (M.tb) RNA sequencing data could potentially indicate contamination, particularly if M.tb itself does not exhibit traditional splice-site events.

Here is my argument for reason 2:
Splice-site artifacts refer to errors in RNA sequencing (RNA-seq) data that occur due to the misinterpretation of splicing events. Mycobacterium tuberculosis (M.tb) does not have introns in its DNA genome, and therefore, it does not require traditional RNA splicing during transcription. Any splice-site events detected in RNA-seq data would not be due to M.tb's own transcriptional processes, but rather could be caused by contamination from other organisms (such as host cells or other bacteria) that do undergo RNA splicing. However, further investigation would need to be conducted to see if this is due to contamination.

There is a chance of the indel mutations occurring because of replication slippage, DNA repair mechanisms, transposon activity, or stress-induced errors but the chances of this happening are less likely than errors in alignment or contamination because the variant annotations do not confidently support the reads behind due to actual mutations.
