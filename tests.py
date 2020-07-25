import pytest
import urllib.request


class test():
    def setup(self):
        pass

    def test_internet_connectivity(self):
        print('abc')
        try:
            urllib.request.urlopen("http://www.google.com")
            skip_all = True
        except:
            skip_all = False

    def test_check(self):
        print('passed')
