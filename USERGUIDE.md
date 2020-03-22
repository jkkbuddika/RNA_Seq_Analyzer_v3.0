# User guide
Please go through this step-by-step guide to setup and begin analysis of your data. This is a ***six*** step process:

### Step 1: Getting started
Set up a conda environment with all necessary packages installed. To set up the conda environment (i.e., dataanalyzer):
```
conda create -n dataanalyzer -c conda-forge -c bioconda python=3.7
conda install -n dataanalyzer -c conda-forge -c bioconda fastqc star qualimap samtools deeptools subread multiqc singularity
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
> add_mat   
> scripts     

### Step 3: Download additional materials
#### Download the singularity image from GoSTRIPES workflow to use TagDust2 for rRNA removal
To do this:
```
cd add_mat
singularity pull --name gostripes.simg shub://BrendelGroup/GoSTRIPES
cd ..
```
Note that the *add_mat* directory by default contain rRNA sequences for *D. melanogaster*, *C. elegans* and *S. cerevisiae* downloaded from Ensembl [BioMart](https://www.ensembl.org/biomart/martview/b1eec568acae1f43251215e8bd8f26fd).
```
cd add_mat
ls
cd ..
```
> Celegans_rRNA.txt	  
> Dro_rRNA.txt		    
> gostripes.simg        
> Yeast_rRNA.txt    

Here is the link to [GoSTRIPES](https://github.com/BrendelGroup/GoSTRIPES) workflow hosted by the [Brendel Group](http://brendelgroup.org/).      

### Step 4: Analysis mode selection and defining additional experiment specific variables
To specify experiment specific variables, open and update "GeneralVariables.py" module using emacs text editor.
```
cd scripts
emacs GeneralVariables.py
```
- **seq_method** : Run-mode. Options are 'single' (single-end data analysis) or 'paired' (paired-end data analysis).
- **rRNA_list** : Name of the rRNA sequence list in *add_mat* directory. Ex: 'Dro_rRNA.txt'
- **snps_file** : Name of the BED file containing SNPs in *add_mat* directory. Ex: 'Dro_snps.bed'
- **genome** : Biomart link to the genome of interest. Ex: Link to the Drosophila genome is "ftp://ftp.ensembl.org/pub/release-99/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.28.dna_sm.toplevel.fa.gz"
- **feature** : Biomart link to the genome annotation of interest. Ex: Link to the Drosophila genome annotation is "ftp://ftp.ensembl.org/pub/release-99/gtf/drosophila_melanogaster/Drosophila_melanogaster.BDGP6.28.99.gtf.gz"
- **stranded** : Strandedness of the library preparation. Options are **0** (unstranded), **1** (stranded) or **2** (reversely stranded)
- **diff_features** : Features to be counted using featureCounts. To check supported features, download and open the annotation file using "less" command.

Once necessary changes are being made:
```
Ctrl+x+s then Ctrl+x+c ## To save and quit emacs
cd ..
ls
```
> add_mat  
> scripts

### Step 5: Input data preparation
The pipeline uses input files in .fastq format for analysis. To upload input data, navigate first to the home directory and create a directory *raw_sequences*.
```
mkdir raw_sequences
ls
```
> add_mat  
> raw_sequences   
> scripts   

Then upload input sequences to the *raw_sequences* directory. Naming of files is ***very important*** and follow the recommended naming scheme. Name of an input fastq file must end in the following order: `_R1.fastq` or/and `_R2.fastq`

If the naming is different than what is required, you can use the following bash command to automatically rename all files to the correct architecture.
```
for i in `ls *R1*`; do
newname="${i/%_001.fastq/.fastq}"
mv -- "$i" "$newname"; 
done
```
> In the above example, running this command will convert a file name from `esg_WT_T1_R1_001.fastq` to `esg_WT_T1_R1.fastq`.    

### Step 6: Executing the pipeline
All executables of the pipeline are written onto *run.py* module. To start analyzing data activate the conda environment above, navigate to the scripts directory and execute *run.py* using python.
```
source activate dataanalyzer
cd scripts
python run.py
```

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

Now that you have carefully read the **USER GUIDE** let's use a publically available dataset to identify A-to-I editing sites, [click here](https://github.com/jkkbuddika/RNA-Seq-Data-Analyzer/blob/master/VIGNETTE.md).
