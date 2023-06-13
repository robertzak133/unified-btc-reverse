import os
from Struct import Struct

## Subset of code from Linouth: https://github.com/Linouth/iCatch-V50-Playground
##  with apologies until I figure out how (or whether) to merge

class carveBTCBRN:

    SPHOST_FAT_INDEX = 2
    SPHOST_FAT_HEADER = 0x120
    
    def carve(self, infile, outfile, size, offset=0, out_directory="./"):
        '''Carve block of bytes from infile and save into outfile
        Parameters
        ----------
        infile : BytesIO
            File to carve from
        outfile : BytesIO
            File to save to
        size : int
            Number of bytes to carve
        offset : int
            The offset to start at
        '''
        outfile = os.path.join(out_directory, outfile)
        ##print(f'Info::carve: {infile} > {outfile} @0x{offset:02x} 0x{size:02x}')
        with open(infile, 'rb') as infile, open(outfile, 'wb') as outfile:
            infile.seek(offset)
            data = infile.read(size)
            outfile.write(data)

    def carve_firmware(self,FILENAME='SPHOST.BRN', out_directory='./'):
        '''Carve all chunks from a SPHOST.BRN firmware file
        This also saves the A and B fat partitions in separate files
        Parameters
        ----------
        FILENAME : str
            The filename of the SPHOST.BRN(-like) firmware file
        '''

        # Read and parse SPHOST.BRN header
        with open(FILENAME, 'rb') as f:
            header = Struct([
                ('magic', '16s'),
                ('filesize', 'I'),
                ('offset', [
                    (0, 0x200),
                    (1, 'I'),
                    (2, 'I'),
                    (3, 'I'),
                    (4, 'I'),
                    (5, 'I'),
                    (6, 'I')
                    ]),
                ('crc', 'I')
                ], f.read(0x200))

        # Carve header to later reconstruct the SPHOST.BRN file
        self.carve(FILENAME, 'SPHOST.header', 0x200, 0, out_directory=out_directory)

        for index,offset in header.ldata['offset'].items():

            # Skip empty offset and the fat offset as this needs to be carved
            # differently
            if offset > 0 and index != self.SPHOST_FAT_INDEX:

                # Read offset from header and determine block size
                try:
                    i = index
                    while True:
                        i += 1
                        to_read = header.ldata['offset'][i];
                        if to_read != 0: break
                    to_read -= offset
                except:
                    to_read = header.ldata['filesize'] - offset

                # Write blocks to separate files
                self.carve(FILENAME, f'offset{index}', to_read, offset, out_directory=out_directory)


        # Carve AB Fat part header to later reconstruct a modified A or B partition
        self.carve(FILENAME, f'offset{self.SPHOST_FAT_INDEX}.header', self.SPHOST_FAT_HEADER,
              header.ldata['offset'][self.SPHOST_FAT_INDEX], out_directory=out_directory)

        with open(FILENAME, 'rb') as f:
            # Read and carve FAT16 (A) partition
            offset = header.ldata['offset'][self.SPHOST_FAT_INDEX] + self.SPHOST_FAT_HEADER
            print(f'Info::carve: (A) partition offset = 0x{offset:02x}')
            f.seek(offset)
            fat16hdr = Struct([
                (None, '3B'),
                ('oem', '8s'),
                ('bytes_per_sector', 'H'),
                (None, '6B'),
                ('sectors', 'H')
                ], f.read(0x40))
            fat16size = fat16hdr.ldata['bytes_per_sector'] * fat16hdr.ldata['sectors']
            print(f'Info::carve A size: 0x{fat16size:8x}')
            self.carve(FILENAME, f'offset{self.SPHOST_FAT_INDEX}.A', fat16size, offset, out_directory=out_directory)

            # Read and carve FAT12 (B) partition
            offset = header.ldata['offset'][self.SPHOST_FAT_INDEX] + fat16size + self.SPHOST_FAT_HEADER
            print(f'Info::carve: (B) partition offset = 0x{offset:02x}')
            if offset < 8000000 :
                f.seek(offset)
                fat12hdr = Struct([
                    (None, '3B'),
                    ('oem', '8s'),
                    ('bytes_per_sector', 'H'),
                    (None, '6B'),
                    ('sectors', 'H')
                    ], f.read(0x40))
                fat12size = fat12hdr.ldata['bytes_per_sector'] * fat12hdr.ldata['sectors']
                print(f'Info::carve B size: 0x{fat12size:8x}')
                self.carve(FILENAME, f'offset{self.SPHOST_FAT_INDEX}.B', fat12size, offset, out_directory=out_directory)
