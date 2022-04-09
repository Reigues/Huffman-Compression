# coding: utf8

from functions import *

def test_byte_to_bits():
  assert byte_to_bits(255)=='11111111'
  assert byte_to_bits(0)=='00000000'
  assert byte_to_bits(184)=='10111000'
  assert byte_to_bits(22)=='00010110'

def test_bits_to_byte():
  assert bits_to_byte('11111111')==255
  assert bits_to_byte('00000000')==0
  assert bits_to_byte('10111000')==184
  assert bits_to_byte('00010110')==22

def test_get_args():
  assert get_args(['compresser.py'])==[]
  assert get_args(['compresser.py','-s','-b','-s', 'example_files/bonjour.txt'])==[('example_files/bonjour.txt',False)]
  assert get_args(['compresser.py','example_files/bonjour.txt','example_files/vide.txt'])==[('example_files/bonjour.txt',True),('example_files/vide.txt',True)]