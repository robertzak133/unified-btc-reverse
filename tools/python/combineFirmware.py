import os
## Subset of code from Linouth: https://github.com/Linouth/iCatch-V50-Playground
##  with apologies until I figure out how (or whether) to merge

class combineFirmware:
    def combine_firmware(self, outfile='SPHOST.BRN', files=None, directory='./'):
        '''Combine carved out chunks into a single firmware file
        Parameters
        ----------
        outfile : str
           File to save the firmware file to
        files : list(str)
           List of chunks to copy into firmware file. NOTE: The order is very
           important. 
        directory : str
           Directory where the chunks are located
        '''
        if not files:
            print(f'Error::combineFirmware: no file list')
            return

        # Do nothing if directory or outfile are not valid
        if not os.path.isdir(directory):
            print(f'Error::combineFirmware: directory {directory} is not valid')
            return

        # Open firmware file to read to 
        with open(outfile, 'wb') as f:

            # Loop over files to combine
            for filename in files:
                filename = os.path.join(directory, filename)
                ##print(f'Info::combineFirmware::Concatting {filename} into {outfile}')

                try:
                    # Copy file contents to firmware file
                    with open(filename, 'rb') as infile:
                        data = infile.read()
                        f.write(data)
                except FileNotFoundError:
                    print(f'Error::combineFirmware:File {filename} not found.')
                    break
