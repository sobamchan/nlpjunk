import re
from typing import Dict, List
from datetime import datetime
from dataclasses import dataclass, field
from nlpjunk.parser import Parser


def remove_stopwords(words: List[str], stopwords: List[str]) -> List[str]:
    new_words = []
    for w in words:
        if w not in stopwords:
            new_words.append(w)
    return new_words


def preprocess(words: List[str]) -> List[str]:
    with open("./nlpjunk/assets/stopwords.txt", "r") as f:
        stopwords = [line.strip() for line in f.readlines()]

    new_words = remove_stopwords(words, stopwords)

    return new_words


@dataclass
class Entry:

    title: str
    text: str
    updated_at: datetime
    meta: Dict
    p: Parser

    clean_text: str = field(init=False)
    wakati_text: str = field(init=False)

    def __post_init__(self):
        text = re.sub(
                r'^\(?https?:\/\/.*[\r\n]*[ )]',
                '',
                self.text,
                flags=re.MULTILINE)
        self.clean_text = text
        words = preprocess(self.p.tokenize(self.clean_text))
        self.wakati_text = " ".join(words)

    def __lt__(self, other):
        return self.updated_at < other.updated_at
