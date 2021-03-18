import pytest

from Dogs import *


def test_age_sort():
    assert callable(age_sort)
    current_roster = {'Sparky':['Chihuahua', 9 , 'small'],
                     }
    assert (age_sort(current_roster) == ['older_dog'])
    assert isinstance(age_sort(current_roster), list)


def test_capacity_counter():
    assert callable(capacity_counter)
    current_roster = {'Hazel': ['English Toy Spaniel', 5 , 'small'], 
                      'Maco':['Australian Terrier', 7 , 'small'],
                      'Loki':['Chihuahua', 6 , 'small'], 
                      'Fiona':['Chihuahua', 12 , 'small'],
                      'Peaches':['Pitbull', 3 , 'large'], 
                      'Booger':['French Bulldog', 2 , 'medium'],
                      'Teddy':['Maltese', 16, 'small'],
                      'Gio':['Maltese', 1 ,'small'],
                      'Barbie':['Golden Retriever', 10 , 'large'],
                      'Baby':['Bulldog', 3 , 'large'],
                      'Tita':['Miniature Pinscher', 8 ,'medium'],
                      'Tony':['Greyound', 4 ,'large'],
                      'Sparky':['Chihuahua', 9 , 'small'],
                      'Stella':['Dachshund', 11 ,'small'],
                      'Korren':['German Sheperd', 6 ,'large'],
                      'Rascal':['Husky', 4 ,'large'],
                      'Sally':['Labrador Retriever', 10 ,'large'],
                      'Archie':['Collie', 5 ,'large'],
                      'Spike':['Irish Setter',7,'large'],
                      'Zeus':['Mastiff',13,'large']
                     }
    #There are exatly 20 dogs
    assert (capacity_counter(current_roster) == 'We are at capacity.') 
    assert isinstance(capacity_counter(current_roster), str)