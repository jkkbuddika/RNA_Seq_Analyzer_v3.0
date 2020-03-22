class GeneralVariables:

    ## Analysis mode: 'single' or 'paired'.
    seq_method = 'paired'

    ## Name of the Biomart rRNA list in add_mat directory.
    rRNA_list = 'Dro_rRNA.txt'

    ## Link to the Biomart genome file of interest.
    genome = 'ftp://ftp.ensembl.org/pub/release-99/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.28.dna_sm.toplevel.fa.gz'

    ## Link to the Biomart annotation file of interest.
    feature = 'ftp://ftp.ensembl.org/pub/release-99/gtf/drosophila_melanogaster/Drosophila_melanogaster.BDGP6.28.99.gtf.gz'

    ## Strandedness of the experiment: '0', '1' or '2'
    stranded = '0'

    ## Include a list of features to be quantified.
    diff_features = ['gene', 'three_prime_utr', 'CDS', 'five_prime_utr']
