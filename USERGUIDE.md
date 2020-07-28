# User guide
Please go through this step-by-step guide to setup and begin analysis of your data. This is a ***six*** step process:

### Step 1: Getting started
Set up a conda environment with all necessary packages installed. To set up the conda environment (i.e., dataanalyzer):
```
conda create -n dataanalyzer -c conda-forge -c bioconda python=3.7
conda install -n dataanalyzer -c conda-forge -c bioconda fastqc star qualimap samtools deeptools subread multiqc
```
To update your conda environment:
```
conda update -n dataanalyzer -c conda-forge -c bioconda --all
```
To activate the enironment:
```
source activate dataanalyzer
```
To deactivate the environment:
```
source deactivate
```

For more details on managing conda enviroments [click here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

### Step 2: Cloning the repository
To clone the current repository on to your local repository using terminal, first navigate to the ***home directory*** (i.e., where you want analyzed data to be deposited), paste and enter the following command:

```
git clone https://github.com/jkkbuddika/RNA-Seq-Data-Analyzer.git
ls
```
> RNA-Seq-Data-Analyzer   

Once cloning is completed:
```
mv RNA-Seq-Data-Analyzer/*/ ./
rm -rf RNA-Seq-Data-Analyzer
ls
```
> environment           
> scripts     

### Step 3: Input data preparation
The pipeline uses input files in .fastq format for analysis. To upload input data, navigate first to the home directory and create a directory *raw_sequences*.
```
mkdir raw_sequences
ls
```
> environment         
> raw_sequences   
> scripts   

Then upload input sequences to the *raw_sequences* directory. Naming of files is ***very important*** and ***must*** follow the recommended naming scheme. Name of an input fastq file must end in the following order: `_R1.fastq` or/and `_R2.fastq`

If the naming is different than what is required, you can use a bash command like below to automatically rename all files to the correct architecture.
```
for i in `ls *R1*`; do
newname="${i/%_001.fastq/.fastq}"
mv -- "$i" "$newname"; 
done
```
> In the above example, running this command will convert a file name from `esg_WT_T1_R1_001.fastq` to `esg_WT_T1_R1.fastq`.

### Step 4: Executing the pipeline
All executables of the pipeline are written onto *run.py* module. To start analyzing data, activate the conda environment above, navigate to the scripts directory and execute *run.py* using python.
```
source activate dataanalyzer
cd scripts
python run.py
```
This should intiate running the analysis pipeline. Immediately you will get a couple questions that you have to answer.
- **Enter the species code (Options: hs, mm, dm, ce, dr or custom):** Answer based on the species, **hs**: human, **mm**: mouse, **dm**: fruit fly, **ce**: *C. elegans*, **dr**: zebra fish or **custom**: any other model organism
- **Enter the Run Mode (Options: 0 for single-end or 1 for paired-end):** Pipeline supports analysis of both single-end or paired-end data. Answer **0** if single-end. Answer **1** if paired-end.
- **Deduplication (Options: TRUE or FALSE):** The pipeline allows deduplication using Samtools. Choice is yours! Answer **TRUE** to activate or **FALSE** to deactivate deduplication.

Note if the species is **custom** this will prompt two more additional questions:
- **FTP link to the genome to download:** Enter the link to the genome FASTA to download. For instance, if the custom species is yeast here is the Ensembl url to download the genome, ftp://ftp.ensembl.org/pub/release-100/fasta/saccharomyces_cerevisiae/dna/Saccharomyces_cerevisiae.R64-1-1.dna_sm.toplevel.fa.gz
- **FTP link to the annotation to download:** Enter the link to the corresponding GTF to download. For instance, if the custom species is yeast here is the Ensembl url to download the GTF, ftp://ftp.ensembl.org/pub/release-100/gtf/saccharomyces_cerevisiae/Saccharomyces_cerevisiae.R64-1-1.100.gtf.gz

You are all set!!! Let it run. Depending on the size of each file and the number of datasets run time can vary so much!

### Retrieve additional information
It is important to track the number of sequences retained after each step. You can use following bash commands to acheive this.

1. If the directory of interest have a series of *.fastq* files, you can use the following bash command to get read counts saved into a *.txt* file in the same directory. As an example let's save read counts of the *raw_sequences* directory.
```
cd raw_sequences

for i in `ls *.fastq`; do
c=`cat $i | wc -l`
c=$((c/4))
echo $i $c
done > raw_readCounts.txt
```
> Executing the above bash command will save a file named *raw_readCounts.txt* in the *raw_sequences* directory with file name and number of reads in each file.

2. If the directory of interest have a series of *.bam* files, you can use the following bash command that uses [SAMtools](https://github.com/samtools/samtools). As an example let's save mapped read counts of the *star_aligned* directory.
```
cd star_aligned

for i in `ls *.bam`; do
echo ${i} $(samtools view -F 4 -c $i)
done > bam_readCounts_aligned.txt
```
> Executing the above bash command will save a file named *bam_readCounts_aligned.txt* in the *star_aligned* directory with bam file names and number of reads that are mapped to the reference genome. Note that the [sam flag](https://broadinstitute.github.io/picard/explain-flags.html) ***4*** eliminates unmapped sequences from the count, thus giving the total number of sequences that are successfully aligned.     

Now that you have carefully read the **USER GUIDE** let's use a publically available dataset to analyze, [click here](https://github.com/jkkbuddika/RNA-Seq-Data-Analyzer/blob/master/VIGNETTE.md).
