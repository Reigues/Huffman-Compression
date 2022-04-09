# coding: utf8

from compresser import *

def test_count_occurences():
  test = {}
  count_occurences([], test)
  assert test == {}
  test = {'a' : 2}
  count_occurences(['a', 'a', 'a', 'b'], test)
  assert test == {'a' : 5 , 'b' : 1}
  test = {}
  count_occurences([2, 'a', 'r', 0.1], test)
  assert test == { 2 : 1, 'a' : 1, 'r' : 1, 0.1 : 1}

def test_make_tree():
  assert make_tree({-1:0}) == (-1,0)
  assert make_tree({(0) : 0, (1) : 1}) == ((0,0), (1,1), 1)
  assert make_tree({'1' :1, '2':2, '3':3, '4':4, '5':5, '6':6}) == (('4', '5', 9), ('6', ('3', ('1', '2', 3), 6), 12), 21)

def test_make_encoded_components():
  a, b, c = make_encoded_components(('a', 0), '01101', ['0', '1', '1', '0', '1'], {'b': '2'}, ['b'])
  assert a == ['0', '1', '1', '0', '1', '1']
  assert b == ['b', 'a']
  assert c == {'b' : '2','a': '01101'}
  a, b, c = make_encoded_components((('a', 0), ('b', 1), 2), '', [], {}, [])
  assert a == ['0', '1', '1']
  assert b == ['a', 'b']
  assert c == {'a': '0', 'b' :'1'}
  tree  = ((('4', 4), ('5', 5), 9), (('6', 6), (('3', 3), (('1', 1), ('2', 2), 3), 6), 12), 21)
  a, b, c = make_encoded_components(tree, '', [], {}, [])
  print(a, b, c)
  assert a == ['0', '0', '1', '1', '0', '1', '0', '1', '0', '1', '1'] 
  assert b == ['4', '5', '6', '3', '1', '2']
  assert c == {'4': '00', '5': '01', '6': '10', '3': '110', '1': '1110', '2': '1111'}

def test_encode_char_list():
  assert encode_char_list([-1, 0]) == '000000000000000000000000'
  assert encode_char_list([ 255, 58, -1, 96, 2]) == '000000101111111100111010011000000000001000000010'
  assert encode_char_list([1, 2, 3, 4, -1, 6]) == '00000100000000010000001000000011000001000000011000000110'