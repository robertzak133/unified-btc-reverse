import os
import struct
import sys
from collections import defaultdict

SPHOST_FAT_INDEX = 2
SPHOST_FAT_HEADER = 0x120

class Struct(object):
  '''
  A class to unpack a binary into a structure like container
  '''
  
  ##__getitem__ = ldata.get

  def __init__(self, fields, data, endianness='<'):
    '''
    E.g.:
    header = Struct([
        ('magic', '8s'),
        ('filesize', 'I'),
        ('items', [
            (0, 'I'),
            (1, 'I')
        ])
    ], data, endianness='>')
    Parameters
    ----------
    fields : list(tuple)
        The fields list has to contain entries like
        ('name', 'struct_format') or ('name', value). Value can be another
        list of tuples to build a tree.
    in_data : bytearray
        The data to parse
    endianness : chr
        '<' for little-endian, '>' for big-endian
    '''
    self.ldata = {}
    self._unpack(fields, data, endianness)

  def _unpack(self, fields, in_data, endianness):
    def up(fields, in_data, root, offset):
      for name, f in fields:
        if name == None:
          offset += struct.calcsize(f)
          continue
        if type(f) == list:
          root[name] = {}
          offset = up(f, in_data, self.ldata[name], offset)
        elif type(f) == str:
          root[name] = struct.unpack_from(endianness+f,in_data,offset)[0]
          offset += struct.calcsize(f)
        else:
          root[name] = f
      return offset
    up(fields, in_data, self.ldata, 0)
    return

  def pack_to_buffer(self, endianness='<'):
    if (endianness == '<'):
      endianness = 'little'
    else:
      endianness = 'big'

    def up(root, result):
      for name in root.keys():
        ##print(f'name: {name}; value = {root[name]}; type: {type(root[name])}')
        if (type(root[name]) == dict): 
          result = result + up(root[name], result)
        elif (type(root[name]) == int): 
          value = root[name]
          value = value.to_bytes(4, endianness)
          print(f'{name} : 0x{value} size={len(value)}')
          result = result + value
        elif (type(root[name]) == bytes):
          value = root[name]
          print(f'{name} : {value} size={len(value)}')
          result = result + value
        else:
          print('???')
      return result
    result = up(self.ldata, bytes())
    return (result)

  # recursively print elements in hierarchical dictionary
  def pretty_print(self):
    def up(indent, root, offset):
      for name in root.keys():
        ##print(f'name: {name}; value = {root[name]}; type: {type(root[name])}')
        if (type(root[name]) == dict): 
          offset = up(indent+"  ", root[name], offset)
        elif (type(root[name]) == int): 
          value = root[name]
          print(f'{indent}{name} : 0x{value:02x}')
        elif (type(root[name]) == bytes):
          value = root[name]
          print(f'{indent}{name} : {value}')
        else:
          print('???')
      return offset;
    up("", self.ldata, 0)
    return
