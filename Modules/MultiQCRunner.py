import os
import subprocess as sp
import ListMaker
import ColorTextWriter

class MultiQCRunner:

    def __init__(self, home_dir):
        self.home_dir = home_dir

    def multiqc(self):

        outdir = os.path.join(self.home_dir, 'MultiQC_Summary')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        dl = ListMaker.ListMaker(self.home_dir)
        dir_list = dl.list_files()

        ctw = ColorTextWriter.ColorTextWriter()

        print(ctw.CBEIGE + ctw.CBOLD + 'Running MultiQC ...' + ctw.CEND + '\n')

        for i in dir_list:
            print('\n' + ctw.CBEIGE + ctw.CBOLD + 'Generating MultiQC Reports for ' + i + ' ...' + ctw.CEND + '\n')

            param = [
                'multiqc',
                self.home_dir + i + '/',
                '-o', outdir,
                '-n', i + '_MultiQC_Report.html'
            ]

            command = ' '.join(param)
            sp.check_call(command, shell=True)

        print('\n' + ctw.CBEIGE + ctw.CBOLD + 'Running MultiQC done!!!' + ctw.CEND)