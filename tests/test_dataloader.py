from nlpjunk.dataloader import jekyll_format
from nlpjunk.parser import Parser

s = """---
title: awesome title
updated: 2020-01-01
---
ここにコンテンツ"""

parser = Parser()


def test_jekyll_format():
    entry = jekyll_format(s, parser)
    assert entry.title == "awesome title"
    assert entry.text == "ここにコンテンツ"


def test_wakati():
    entry = jekyll_format(s, parser)
    entry.wakati_text = "ここ に コンテンツ"
