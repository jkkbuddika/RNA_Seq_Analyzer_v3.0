import subprocess as sp
import os
import glob
import ColorTextWriter

class GzExtractor:

    def __init__(self, input_dir):
        self.input_dir = input_dir

    def gz_extractor(self):

        file_list = sorted(glob.glob(self.input_dir + '*.fastq.gz'))

        ctw = ColorTextWriter.ColorTextWriter()

        for i in file_list:

            print('\n' + ctw.CRED + 'Unzipping: ' + ctw.CBLUE + os.path.basename(i) + ctw.CRED + ' ...' + ctw.CEND + '\n')

            sp.call(['gunzip', i])