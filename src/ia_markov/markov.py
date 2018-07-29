import glob
import os
import re

import markovify
import nltk
from internetarchive import download
from markovify.splitters import split_into_sentences


class MarkovModel(object):

    """
    A Markov Model trained on
    on an Internet Archive text file.
    """

    def __init__(self, exclude=None, state_size=2):
        self.archive_name = None
        self.exclude = exclude
        self.model = None
        self.state_size = state_size

    def train_model(self, archive_name):
        """
        Trains the model
        on a given archive_name
        """
        self.archive_name = archive_name
        self._download_corpus()
        self._unpack_corpus()

    def sentence_split(self, text):
        """
        Splits full-text string into a list of sentences.
        """
        sentences = split_into_sentences(text)
        if self.exclude:
            return self._clean_sentences(sentences)
        else:
            return sentences

    def _clean_sentences(self, sentences):
        """
        Removes excluded regex patterns
        """
        if isinstance(self.exclude, re._pattern_type):
            regex = self.exclude
            return [s for s in sentences if not regex.search(s)]
        if isinstance(self.exclude, list):
            filtered = sentences
            for regex in self.exclude:
                filtered = [s for s in filtered if not regex.search(s)]
            return filtered

    def _download_corpus(self):
        """
        Downloads a corpus of text
        from internet archive to
        current working directory
        """
        download(self.archive_name, verbose=True, glob_pattern="*.txt")

    def _unpack_corpus(self):
        """
        unpacks a text file
        downloaded from internet archive
        """
        filenames = glob.glob(os.path.join(self.archive_name, '*.txt'))
        text = None
        for filename in filenames:
            with open(filename) as f:
                text = f.read()
            # build the model
            self._create_markov(text)

    def _create_markov(self, text):
        """
        Assign markovify.Text
        as model
        """
        self.model = markovify.Text(text, state_size=self.state_size)


class POSMarkov(MarkovModel):

    def _create_markov(self, text):
        """
        Assign part of speech tagged markov
        to model.
        """
        self.model = POSifiedText(text, state_size=self.state_size)


class POSifiedText(markovify.Text):
    """
    Override Markovify Text
    to use part-of-speech tagging
    on training text.
    """

    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        print(words)
        try:
            words = ["::".join(tag) for tag in nltk.pos_tag(words)]
        except Exception:
            pass
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
