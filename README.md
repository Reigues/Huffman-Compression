
# Compresser & Decompresser

Program used to compress text file according to the Huffman algorithm.
There is the program which cancel the action too
It can be used by everyone who wants to compress a file. 


## Usage/Examples

Usage `compresser.py` :

```bash
python compresser.py <[-sb] file_to_compress.txt>
```
Usage `decompresser.py` :
```bash
python decompresser.py <[-sb] file_to_uncompress.txt>
```
Example:

```bash
python compresser.py -s texte.txt -b autre_texte.txt
```


## Running Tests

To run tests, run the following commands

```bash
pytest test_compresser.py
pytest test_decompresser.py
pytest test_functions.py
```


## Authors

-Olivier Lamothe  
-Théo Bury  
-Rémy Sangoï


## Sponsor

Bungadrill
<a href="https://www.instagram.com/bungadrill" target="_blank"><img src="data/logo_BGD_fff.png" alt="Bungadrill" width="100"></a>


## License

MIT License

Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

