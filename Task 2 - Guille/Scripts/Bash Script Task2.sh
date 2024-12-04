jovyan:~$
jovyan:~$ mkdir task2_guille/
jovyan:~$ cd shared-team/
jovyan:~/shared-team$ ls
jovyan:~/shared-team$ cp -R task2q2/ task2_guille/
jovyan:~/shared-team$ cd ~
jovyan:~$ cd task2_guille/
jovyan:~/task2_guille$ conda create -y -n varcall minimap2 samtools bcftools bedtools
(varcall) jovyan:~/task2_guille$ conda activate varcall
(varcall) jovyan:~/task2_guille$ pip install pandas matplotlib 
(varcall) jovyan:~/task2_guille$ cd task2q2/ 
(varcall) jovyan:~/task2_guille$/task2q2$ ls
 NC_000962.3.fa       README~                      sample.2.reads1.fq.gz   sample.3.reads2.fq.gz
 NC_000962.3.fa.fai   sample.1.reads1.fq.gz   sample.2.reads2.fq.gz   'Untitled Folder'
 README               	 sample.1.reads2.fq.gz   sample.3.reads1.fq.gz
(varcall) jovyan:~/task2_guille$/task2q2$ minimap2 -a -x sr NC_000962.3.fa sample.1.reads1.fq.gz sample.1.reads2.fq.gz | samtools view -h -F 0x900 - | samtools sort -O bam > mapped_reads_1.bam
(varcall) jovyan:~/task2_guille$/task2q2$ minimap2 -a -x sr NC_000962.3.fa sample.2.reads1.fq.gz  sample.2.reads2.fq.gz | samtools view -h -F 0x900 - | samtools sort -O bam > mapped_reads_2.bam
(varcall) jovyan:~/task2_guille$/task2q2$ minimap2 -a -x sr NC_000962.3.fa sample.3.reads1.fq.gz  sample.3.reads2.fq.gz | samtools view -h -F 0x900 - | samtools sort -O bam > mapped_reads_3.bam
(varcall) jovyan:~/task2_guille$/task2q2$ ls
 mapped_reads_1.bam   NC_000962.3.fa.fai      sample.1.reads2.fq.gz   sample.3.reads2.fq.gz
 mapped_reads_2.bam   README                      sample.2.reads1.fq.gz   'Untitled Folder'
 mapped_reads_3.bam   README~                    sample.2.reads2.fq.gz
 NC_000962.3.fa             sample.1.reads1.fq.gz  sample.3.reads1.fq.gz
(varcall) jovyan:~/task2_guille$/task2q2$ mkdir Vcf_files
(varcall) jovyan:~/task2_guille$/task2q2$ mkdir Bam_files
(varcall) jovyan:~/task2_guille$/task2q2$ mv  mapped_reads_1.bam  mapped_reads_2.bam  mapped_reads_3.bam /home/jovyan/task2_guille/task2q2/Bam_files
(varcall) jovyan:~/task2_guille$/task2q2$ cd Bam_files/
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools flagstat mapped_reads_1.bam 
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools flagstat mapped_reads_2.bam 
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools flagstat mapped_reads_3.bam 
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ cd ../
(varcall) jovyan:~/task2_guille/task2q2$ cp -R NC_000962.3.fa /home/jovyan/task2_guille/task2q2/Bam_files
(varcall) jovyan:~/task2_guille/task2q2$ cd Bam_files/
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ bcftools mpileup -Ou -f NC_000962.3.fa mapped_reads_1.bam  | bcftools call -vc -Ov > variants_1.vcf
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ bcftools mpileup -Ou -f NC_000962.3.fa mapped_reads_2.bam  | bcftools call -vc -Ov > variants_2.vcf
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ bcftools mpileup -Ou -f NC_000962.3.fa mapped_reads_3.bam  | bcftools call -vc -Ov > variants_3.vcf
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ cp -R variants_1.vcf variants_2.vcf variants_3.vcf /home/jovyan/task2_guille/task2q2/Vcf_files
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ cd ../
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ cd Vcf_files/
(varcall) jovyan:~/task2_guille/task2/Vcf_files ls
variants_1.vcf  variants_2.vcf  variants_3.vcf
(varcall) jovyan:~/task2_guille/task2q2/Vcf_files$ less -S variants_1
(varcall) jovyan:~/task2_guille/task2q2/Vcf_files$ less -S variants_2
(varcall) jovyan:~/task2_guille/task2q2/Vcf_files$ less -S variants_3
(varcall) jovyan:~/task2_guille/task2q2/Vcf_files$ cd /home/jovyan/task2_guille/task2q2/Bam_files
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools index mapped_reads_1.bam
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools index mapped_reads_2.bam
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools index mapped_reads_3.bam
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools tview mapped_reads_1.bam NC_000962.3.fa
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools tview mapped_reads_2.bam NC_000962.3.fa
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools tview mapped_reads_3.bam NC_000962.3.fa
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools depth -a mapped_reads_1.bam > depth_1.txt
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools depth -a mapped_reads_2.bam > depth_2.txt
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ samtools depth -a mapped_reads_3.bam > depth_3.txt
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ cd /home/jovyan/shared-team/wed20th_var
(varcall) jovyan:~/shared-team/wed20th_var$\cf2  cp -R get_depths.py /home/jovyan/task2_guille/task2q2/Bam_files
(varcall) jovyan:~/shared-team/wed20th_var$ cd /home/jovyan/task2_guille/task2q2/Bam_files
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ python ~/shared-team/wed20th_var/get_depths.py -i depth_1.txt -o coverage_1_1kb_means.bed
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ python ~/shared-team/wed20th_var/get_depths.py -i depth_2.txt -o coverage_2_1kb_means.bed
(varcall) jovyan:~/task2_guille/task2q2/Bam_files$ python ~/shared-team/wed20th_var/get_depths.py -i depth_3.txt -o coverage_3_1kb_means.bed
