Go to the “home”/start:
cd ~

Create a directory:
mkdir task_2_varcall

Get a reference genome and copy to your directory:
cp ~/shared-team/task2q2/NC_* .
cp ~/shared-team/task2q2/sample.* .
cp ~/shared-team/task2q2/README .

Download conda stuff:
conda create -y -n varcall minimap2 samtools bcftools bedtools
conda activate varcall
pip install pandas matplotlib

Map reads for each sample against the reference genome:
minimap2 -a -x sr NC_000962.3.fa sample.1.reads1.fq.gz sample.1.reads2.fq.gz | samtools view -h -F 0x900 - | samtools sort -O bam > mapped_reads1.bam

minimap2 -a -x sr NC_000962.3.fa sample.2.reads1.fq.gz sample.2.reads2.fq.gz | samtools view -h -F 0x900 - | samtools sort -O bam > mapped_reads2.bam

minimap2 -a -x sr NC_000962.3.fa sample.3.reads1.fq.gz sample.3.reads2.fq.gz | samtools view -h -F 0x900 - | samtools sort -O bam > mapped_reads3.bam

Check if everythings right:
samtools flagstat mapped_reads.bam

Call variants:
bcftools mpileup -Ou -f NC_000962.3.fa mapped_reads1.bam | bcftools call -vc -Ov > variants1.vcf 
bcftools mpileup -Ou -f NC_000962.3.fa mapped_reads2.bam | bcftools call -vc -Ov > variants2.vcf 
bcftools mpileup -Ou -f NC_000962.3.fa mapped_reads3.bam | bcftools call -vc -Ov > variants3.vcf 

Expand: 
less -S variants1.vcf
less -S variants2.vcf
less -S variants3.vcf

q to quit this

Index the bam file:
samtools index mapped_reads1.bam
samtools index mapped_reads2.bam
samtools index mapped_reads3.bam



Look at the pileup evidence:
samtools tview mapped_reads1.bam NC_000962.3.fasta
samtools tview mapped_reads2.bam NC_000962.3.fasta
samtools tview mapped_reads3.bam NC_000962.3.fasta

Hit g to go to a specific position

? for information

Generate depth reads using:
samtools depth -a mapped_reads.bam > depth.txt (#change mapped_reads1/2/3.bam depending on which one it is)
python ~/shared-team/wed20th_var/get_depths.py -i depth.txt -o coverage_1kb_means.bed
