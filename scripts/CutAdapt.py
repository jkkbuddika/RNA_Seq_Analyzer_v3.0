import os
import glob
import subprocess as sp
import ColorTextWriter

class CutAdapt:

    def __init__(self, home_dir, input_dir,  extensions, seq_method):
        self.home_dir = home_dir
        self.input_dir = input_dir
        self.extensions = extensions
        self.seq_method = seq_method

    def cutadapt(self):

        outdir = os.path.join(self.home_dir, 'cutadapt')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        ctw = ColorTextWriter.ColorTextWriter()

        print(ctw.CBEIGE + ctw.CBOLD + 'Running CutAdapt ...' + ctw.CEND + '\n')

        r1_reads = sorted(glob.glob(self.input_dir + '*R1.fastq'))
        r2_reads = sorted(glob.glob(self.input_dir + '*R2.fastq'))

        if self.seq_method == 'single':
            for i in r1_reads:
                print('\n' + ctw.CBEIGE + ctw.CBOLD + 'CutAdapting: ' + ctw.CBLUE + os.path.basename(i) +
                      ctw.CBEIGE + ctw.CBOLD + ' ...' + ctw.CEND + '\n')

                output_file = outdir + '/' + os.path.basename(i).split('.fastq')[0] + '_trimmed' + self.extensions[0]

                command = [
                    'cutadapt -m 30',
                    '-o', output_file, i,
                    '>', output_file.split('_trimmed')[0] + '_trim.matrics' + self.extensions[3]
                ]

                command = ' '.join(command)
                sp.check_call(command, shell=True)

        elif self.seq_method == 'paired':
            for (i, j) in zip(r1_reads, r2_reads):
                print('\n' + ctw.CBEIGE + ctw.CBOLD + 'CutAdapting: ' + ctw.CBLUE + os.path.basename(i) + ' and ' +
                      os.path.basename(j) + ctw.CBEIGE + ctw.CBOLD + ' ...' + ctw.CEND + '\n')

                output_file_R1 = outdir + '/' + os.path.basename(i).split('.fastq')[0] + '_trimmed' + self.extensions[0]
                output_file_R2 = outdir + '/' + os.path.basename(j).split('.fastq')[0] + '_trimmed' + self.extensions[0]

                command = [
                    'cutadapt -m 30 -u 5',
                    '-o', output_file_R1, '-p', output_file_R2, i, j,
                    '>', output_file_R1.split('_trimmed')[0] + '_trim.matrics' + self.extensions[3]
                ]

                command = ' '.join(command)
                sp.check_call(command, shell=True)

        print('\n' + ctw.CRED + ctw.CBOLD + 'CutAdapt Trimming Completed!!!' + ctw.CEND)
