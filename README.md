# ID3 Audio Tag Fixer (Arabic: cp1256)

Fix wrong MP3 Arabic tag encoding. No more audio files for artist: 'äÌíÈ áÈíÈ'
## Requirements
* Python 2.7
* Linux, I didn't test on Windows!

## Usage
1. Download and install [Mutagen Library](https://github.com/quodlibet/mutagen). Use the _Install_ instructions in [the online documentation](https://mutagen.readthedocs.io/en/latest/index.html#installing).
2. Download `ID3TagFixer.py` script file
3. Make sure you have backups for your MP3 files, in case the script had problems with your files. _Better safe than sorry!_
4. Pass your directories with MP3 files to be fixed, as command line arguments to the script space separated.

## Example
```bash
$ python /path/to/ID3TagFixer.py /directory/with/mp3/files/1 /directory/with/mp3/fils/2 ...
```

## Problem
Some MP3 Arabic files have the ID3 tags; Album, Artist, Track Name, ...etc, in the wrong format, even if you can read them on your PC, your phone, tablet or Car player display them in latin characters.

## Root Cause
The main issue is that these tags are incoded in non-standard character incoding, in my case it was [cp1256, a Windows Arabic encoding](http://www.kreativekorp.com/charset/encoding.php?name=CP1256). If these tags were encoded in standard UTF-8; like on any Linux machine, it would have shown correctly on all other devices - even Windows!!.

## Solution
Included a simple script that open all MP3 files in any number of directories and fix them in two steps:

1. Change the ID3 tags to version 2.4 and map all tags if possible (_Done by [Mutagen Library](https://bitbucket.org/lazka/mutagen)_).
2. Change the character encoding to all tags using `cp1256` decoding table including in standard Python 2.7 `encodings` library.

## Future Enhancements
1. __Python 3__: There is no technical reason for using Python 2.7 othere than I started with another ID3 help library that supported only Python 2.7. Talk about bad influnce.
2. __Encoding as an Argument__: It will be very cool if we can pass the encoding library from command line, but the current encoding library implementation is not consistant and there are special cases to be handled.
3. __Encoding Detection__: Usually we know what the artist name, or album title. There can be another you utility script that takes that tag name and how should it be encoded, and it can use all available standard encoding libraries and try to match the given name, thus we can detect the right encoded automatically :)


