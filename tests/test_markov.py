import os
import re
import shutil
import unittest

from ia_markov import MarkovModel
from ia_markov import POSMarkov


class TestMarkov(unittest.TestCase):

    def test_model(self):
        path = 'tmp'
        os.makedirs(path)
        os.chdir(path)
        m = MarkovModel()
        #m.train_model('FuturistManifesto')
        #assert isinstance(m.model.make_sentence(), str)
        p = POSMarkov()
        # p.train_model('FuturistManifesto')
        # assert isinstance(p.model.make_sentence(), str)
        #os.chdir(os.pardir)
        #shutil.rmtree('tmp', ignore_errors=True)

    def test_clean_sentences(self):
        # test single regex pattern
        regex = re.compile(r'[0-9]*^.*?\s[A-Z]*\s[A-Z]*')
        m = MarkovModel(exclude=regex)
        sentences = ['138 TEST STRING', 'second string is here']
        self.assertEquals(len(sentences), 2)
        cleaned = m._clean_sentences(sentences)
        self.assertEquals(len(cleaned), 1)

        # test list of regex patterns
        reg_list = [regex]
        regex2 = re.compile(r'[a-z]*\s[a-z]*\s[a-z]*\s[a-z]')
        reg_list.append(regex2)
        m = MarkovModel(exclude=reg_list)
        cleaned = m._clean_sentences(sentences)
        self.assertEquals(len(cleaned), 0)

if __name__ == '__main__':
    unittest.main()
