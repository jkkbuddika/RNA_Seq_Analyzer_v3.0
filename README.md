# RNA-Seq Analyzer
The current version of the RNA-Seq data analyzer is compatible with both single and paired-end (SE and PE) data. The series of python based modules in this repository automate the data analysis process.

## Requirements
The RNA-seq data analyzer requires following tools to be installed for data analysis.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
- [STAR](https://github.com/alexdobin/STAR)
- [QualiMap](http://qualimap.bioinfo.cipf.es/)
- [SAMtools](https://github.com/samtools/samtools)
- [deepTools](https://github.com/deeptools/deepTools/)
- [featureCounts](http://subread.sourceforge.net/)
- [MultiQC](https://github.com/ewels/MultiQC)

We thank developers of these valueble tools!

## Getting started
Start data analysis with setting up a conda environment with all the above tools installed, as it gives you the opportunity to use most updated versions. To set up the conda environment (i.e., dataanalyzer):
```
conda create -n dataanalyzer python=3.7
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

## User guide
### Cloning the repository
To clone the current repository on to your local repository using terminal/commandline, first navigate to the home directory (i.e., where you want analyzed data to be deposited), paste and enter the following command:
```
git clone https://github.com/jkkbuddika/RNA_Seq_Analyzer_v2.0.git
```
Once cloning is completed:
```
mkdir scripts
mv RNA_Seq_Analyzer_v2.0/Modules/*.py scripts/
rm -rf RNA_Seq_Analyzer_v2.0
```
### Download additional materials
In addition to above tools, this pipeline integrates [TagDust2](http://tagdust.sourceforge.net/) to remove rRNAs, the major form of RNA contaminant during early steps of analysis. We will download the singularity image from [GoSTRIPES](https://github.com/BrendelGroup/GoSTRIPES) workflow to use TagDust2 in this analysis. For this:
```
mkdir add_mat
cd add_mat
singularity pull --name gostripes.simg shub://BrendelGroup/GoSTRIPES
```
Now that we have downloaded the singularity image to call and run TagDust2, next step is to download the most updated rRNA sequence list from Ensembl [BioMart](http://useast.ensembl.org/biomart/martview/b56f6bc18af941cb4a61c1ef121b91d1). For example, [click here](https://www.ensembl.org/biomart/martview/67dcc0a3e364a6154fcdfd992dcdbdf2) to download Drosophila rRNA sequence list to your local computer, rename the file name (i.e., "Dro_rRNA.txt") and transfer the file to "add_mat" directory.
### Analysis mode selection and defining experimental design
The pipeline can be used to analyze both single and paired-end (SE and PE) sequencing data. To specify the sequencing method open module "GeneralVariables.py" using emacs text editor. 
```
emacs GeneralVariables.py
```
Change the value of the variable "seq_method" to change the analysis mode. Options include "single" (SE sequencing data analysis mode) and "paired" (PE sequencing data analysis mode). Furthermore, you can specify the strandedness of the experiment. To do this change the value of variable "stranded". Options are 0 (unstranded), 1 (stranded) and 2 (reversely stranded).
Additionally, this module allows you to specify the name of the rRNA sequence file as well. Assign the name of the rRNA sequence file to the variable "rRNA_list".
### Input data preparation
The pipeline uses adapter trimmed input files in .fastq format for analysis. Transfer trimmed raw sequences to a directory named "raw_sequences" on your home directory. 
