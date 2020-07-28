import UserDefinedOptions
import CommonOptions
import FastQCRunner
import CutAdapt
import WebDownloader
import RefGenMaker
import GenomeAligner
import SamTools
import BigWigFileMaker
import FeatureCounter
import MultiQCRunner
import ColorTextWriter

#### Executing the Program

ctw = ColorTextWriter.ColorTextWriter()
print('\n' + ctw.CRED + ctw.CBOLD + 'Initiating data analysis ...' + ctw.CEND + '\n')

gv = UserDefinedOptions.UserDefinedOptions()
cv = CommonOptions.CommonOptions()

qc = FastQCRunner.FastQCRunner(cv.home_dir, cv.fastqc_raw, cv.raw_sequences_dir)
qc.fastqc()

ca = CutAdapt.CutAdapt(cv.home_dir, cv.raw_sequences_dir, cv.extensions, cv.seq_method)
ca.cutadapt()

wd = WebDownloader.WebDownloader(cv.home_dir, cv.genome_dir_name, cv.genome_path, cv.genome_file)
wd.download()

wd = WebDownloader.WebDownloader(cv.home_dir, cv.feature_dir_name, cv.feature_path, cv.feature_file)
wd.download()

rg = RefGenMaker.RefGenMaker(cv.home_dir, cv.Threads, cv.genome_fa, cv.genes_gtf)
rg.refgen()

sa = GenomeAligner.GenomeAligner(cv.home_dir, cv.cutadapt_dir, cv.Threads, cv.ref_genome, cv.extensions, cv.genes_gtf, cv.seq_method)
sa.aligner()

ss = SamTools.SamTools(cv.home_dir, cv.star_aligned, cv.Threads, cv.extensions, cv.seq_method, gv.dedup)
ss.sam_sorting()

bw = BigWigFileMaker.BigWigFileMaker(cv.home_dir, cv.sam_sorted, cv.extensions)
bw.bigwig()

fc = FeatureCounter.FeatureCounter(cv.home_dir, cv.sam_sorted, cv.diff_features, cv.feature_dir, cv.feature_file, cv.extensions, cv.seq_method)
fc.feature()

mqc = MultiQCRunner.MultiQCRunner(cv.home_dir)
mqc.multiqc()

ctw = ColorTextWriter.ColorTextWriter()
print('\n' + ctw.CGREEN + ctw.CBOLD + 'Data analysis is successfully completed !!!' + ctw.CBLACK + ctw.CURL + ctw.CBLINK + ctw.CEND + '\n')
