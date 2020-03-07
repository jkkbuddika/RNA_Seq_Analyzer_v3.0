import GeneralVariables
import CommonVariables
import GzExtractor
import FastQCRunner
import Tagduster
import TDSummaryProcessor
import WebDownloader
import RefGenMaker
import StarAligner
import SamTools
import BigWigFileMaker
import FeatureCounter
import MultiQCRunner
import ColorTextWriter

#### Executing the Program

ctw = ColorTextWriter.ColorTextWriter()
print('\n' + ctw.CRED + ctw.CBOLD + 'Initiating data analysis ...' + ctw.CEND + '\n')
print(ctw.CRED + 'This script can take minutes to hours to analyze your data based on the number of libraries to be analyzed ...' + '\n')

gv = GeneralVariables.GeneralVariables()
cv = CommonVariables.CommonVariables()

#ex = GzExtractor.GzExtractor(cv.raw_sequences_dir)
#ex.gz_extractor()

qc = FastQCRunner.FastQCRunner(cv.home_dir, cv.fastqc_raw, cv.raw_sequences_dir)
qc.fastqc()

td = Tagduster.Tagduster(cv.home_dir, cv.tagdust_singu, cv.raw_sequences_dir, cv.rRNA_path, cv.extensions, gv.seq_method)
td.tagdust()

tdsp = TDSummaryProcessor.TDSummaryProcessor(cv.home_dir, cv.tagdust_out)
tdsp.td_summary()

wd = WebDownloader.WebDownloader(cv.home_dir, cv.genome_dir_name, cv.genome_path, cv.genome_file)
wd.download()

wd = WebDownloader.WebDownloader(cv.home_dir, cv.feature_dir_name, cv.feature_path, cv.feature_file)
wd.download()

rg = RefGenMaker.RefGenMaker(cv.home_dir, cv.Threads, cv.genome_fa, cv.genes_gtf)
rg.refgen()

sa = StarAligner.StarAligner(cv.home_dir, cv.tagdust_out, cv.Threads, cv.ref_genome, cv.extensions, cv.genes_gtf, gv.seq_method)
sa.aligner()

ss = SamTools.SamTools(cv.home_dir, cv.star_aligned, cv.Threads, cv.extensions)
ss.sam_sorting()

bw = BigWigFileMaker.BigWigFileMaker(cv.home_dir, cv.sam_sorted, cv.extensions)
bw.bigwig()

fc = FeatureCounter.FeatureCounter(cv.home_dir, cv.sam_sorted, gv.diff_features, gv.stranded, cv.feature_dir, cv.feature_file, cv.extensions, gv.seq_method)
fc.feature()

mqc = MultiQCRunner.MultiQCRunner(cv.home_dir)
mqc.multiqc()

ctw = ColorTextWriter.ColorTextWriter()
print('\n' + ctw.CGREEN + ctw.CBOLD + ctw.CBLINK + 'Data analysis is successfully completed!!! ' + ctw.CEND + '\n')
