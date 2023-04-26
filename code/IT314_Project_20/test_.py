from crosswordApp.views import testMe

import json
import requests
import pytest

def test1():
    assert testMe(3) == 1
    
def test2():
    assert testMe(4) == 2


