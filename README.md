# RNA-Seq Analyzer
The current version of the RNA-Seq data analyzer is compatible with both single and paired-end (SE and PE) data. The series of python based modules in this repository automate the data analysis process. I ***highly recommend*** reading through this step-by-step manual *carefully* before you start analyzing your data.

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

## Analysis process
All analyzed data will be saved onto the home directory where you deposited the *scripts* directory. The pipeline first use [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess the quality of raw input files. Next [TagDust2](http://tagdust.sourceforge.net/) is being used to remove rRNA contaminants from individual datasets. A datamining module in the pipeline will summarize TagDust2 rRNA removal logs and deposit mined data onto a file named **TagDust_summary.csv** which will be saved onto a directory named *summary_files*. Subsequently, user defined genome and annotation files will be downloaded and a reference genome will be created. Subsequently, rRNA-depleted sequences are mapped to the given genome using [STAR](https://github.com/alexdobin/STAR) genome aligner. The pipeline use [QualiMap](http://qualimap.bioinfo.cipf.es/) to assess the quality of sequence alignment. Note that the pipeline do not do a adaptor trimming at the begining as STAR can inherently soft clip adaptors. If the alignment percentages are low consider trimming adaptors using a program such as [Cutadapt](https://cutadapt.readthedocs.io/en/stable/). The analysis scheme use [SAMtools](https://github.com/samtools/samtools) to coordinate sort, remove potential duplicates and index alignment output files. The sorted alignment file and the index will be used by [deepTools](https://github.com/deeptools/deepTools/) to generate bigwig files for [IGV](https://software.broadinstitute.org/software/igv/) visualization. Next subread package [featureCounts](http://subread.sourceforge.net/) will be called to quantify user defined set of features. Finally, the pipeline integrates [MultiQC](https://github.com/ewels/MultiQC) to generate summary files in an interactive manner.

Now that you know the general outline of the analysis process, go through the step-by-step guide given [here](https://github.com/jkkbuddika/RNA-Seq-Data-Analyzer/blob/master/USERGUIDE.md) to analyze your RNA-seq data.

