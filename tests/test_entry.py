from datetime import datetime
from nlpjunk.entry import Entry, remove_stopwords
from nlpjunk.parser import Parser


parser = Parser()


def test_preprocess():
    entry = Entry(
            title="これがタイトル",
            text="https://www.google.com にアクセスしろ．",
            updated_at=datetime.now(),
            meta={},
            p=parser
            )
    entry.clean_text = "にアクセスしろ．"
    entry.wakati_text = "アクセス"


def test_remove_stopwords():
    stopwords = ["は", "です", "し", "ます", "．"]
    words = "私 は 元気 です ． 失礼 し ます ．".split()
    assert remove_stopwords(words, stopwords) == ["私", "元気", "失礼"]
