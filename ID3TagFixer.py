#!/usr/bin/env python
#-*- coding: utf-8 -*-
from mutagen.easyid3 import EasyID3
import sys
import glob
def correctIncoding(scrambled, inv_map):
  corrected = ''
  for i in scrambled:
    ar_char = i
    if ord(i) > 127 and inv_map.has_key(hex(ord(i))):
      ar_char = inv_map[hex(ord(i))]
    corrected = corrected + ar_char
  # print(scrambled, corrected, type(corrected))
  return corrected

# Open Media Files
def exploreDir(wd, inv_map):
  files = glob.glob(wd + '/*.mp3')
  #exit()
  for filepath in files:
    fixTags(filepath, inv_map)
 
def fixTags(filepath, inv_map):
  audio = EasyID3(filepath)
  for tag in audio.keys():
    audio[tag] = correctIncoding(audio[tag][0], inv_map)
  # print(audio.keys())
  print('Updating File:' , filepath)
  audio.save(filepath)

def main():
  # Load inverse_map for transcoding text
  sys.path.append('/usr/lib/python2.7/encodings')
  from cp1256  import decoding_table
  keys = [ hex(k) for k in range(0,len(decoding_table))]
  inv_map = dict(zip(keys, decoding_table))
  for arg in sys.argv:
    exploreDir(arg ,inv_map)

if __name__ == "__main__":
  main()
