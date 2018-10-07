import glob
import os
import re
import unittest
from unittest.mock import patch
from ia_markov import MarkovModel


class MockModel(MarkovModel):
    """Subclass to mock out the download from Internet Archive."""

    def _download_corpus(self):
        pass

    def _unpack_corpus(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        test_data_dir = os.path.join(current_dir, 'test_data')
        filenames = glob.glob(os.path.join(test_data_dir, '*.txt'))
        text = None
        m = MarkovModel()
        for filename in filenames:
            with open(filename) as f:
                text = f.read()
            # build the model
            model = m._create_markov(text)
        return model


class TestMarkov(unittest.TestCase):
    def test_model(self):
        with patch('ia_markov.MarkovModel', MockModel):
            m = MarkovModel()
            m.train_model('FuturistManifesto')
            sent = None
            while not sent:
                sent = m.model.make_sentence()
            self.assertTrue(sent)
            assert isinstance(sent, str)

    @patch(
        'ia_markov.markov.split_into_sentences'
    )
    def test_sentence_split_without_exclude(self, split_into_sentences):
        m = MarkovModel()
        split_into_sentences.return_value = ['a', 'b', 'c']

        self.assertListEqual(m.sentence_split('MockTest'), ['a', 'b', 'c'])
        split_into_sentences.assert_called_with('MockTest')

    def test_sentence_split_with_exclude(self):
        with patch.object(
            MarkovModel, '_clean_sentences', new=(
                lambda self, sentences: ['MockReturn']
            )
        ):
            regex = re.compile(r'[0-9]*^.*?\s[A-Z]*\s[A-Z]*')
            m = MarkovModel(exclude=regex)

            self.assertListEqual(m.sentence_split('MockTest'), ['MockReturn'])

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
