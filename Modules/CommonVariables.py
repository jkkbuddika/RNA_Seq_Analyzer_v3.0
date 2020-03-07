import os
import GeneralVariables

class CommonVariables:
    gv = GeneralVariables.GeneralVariables()

    ## General
    home_dir = os.path.dirname(os.getcwd())
    raw_sequences_dir = home_dir + 'raw_sequences/'
    tar_gz_file_path = raw_sequences_dir + gv.tar_gz_file
    add_mat = home_dir + 'add_mat/'
    Threads = '8'
    extensions = ['.fastq', '.sam', '.csv', '.txt', '.bam', '.bw', '.bed']
    summary_dir = home_dir + 'summary_files/'

    ## TagDust Variables
    tagdust_singu = add_mat + 'gostripes.simg'
    tagdust_out = home_dir + 'tagdust_out/'
    rRNA_path = add_mat + gv.rRNA_list

    ## Cutadapt Variables
    cutadapt_dir = home_dir + 'cutadapt/'

    ## Variables for FastQC
    fastqc_raw = 'fastqc_raw'
    fastqc_trimmed = 'fastqc_trimmed'

    ## STAR Reference Genome
    genome_file = 'Drosophila_melanogaster.BDGP6.28.dna_sm.toplevel.fa.gz'
    genome_path = 'ftp://ftp.ensembl.org/pub/release-99/fasta/drosophila_melanogaster/dna/'
    genome_url = genome_path + genome_file
    genome_dir_name = 'genome'
    genome_dir = home_dir + 'genome/'
    genome_fa = genome_dir + genome_file.split('.gz')[0]
    feature_file = 'Drosophila_melanogaster.BDGP6.28.99.gtf.gz'
    feature_path = 'ftp://ftp.ensembl.org/pub/release-99/gtf/drosophila_melanogaster/'
    feature_url = feature_path + feature_file
    feature_dir_name = 'genome_feature'
    feature_dir = home_dir + 'genome_feature/'
    genes_gtf = feature_dir + feature_file.split('.gz')[0]
    ref_genome = home_dir + 'star_genome/'

    ## STAR Alignment
    star_aligned = home_dir + 'star_aligned/'

    ## Sam Tools Sorting
    sam_sorted = home_dir + 'sam_sorted/'

    ## DeepTools BigWig Files
    bigwig_files = home_dir + 'bigwig_files/'

    ## FeatureCounts
    fc_output = home_dir + 'feature_counts'