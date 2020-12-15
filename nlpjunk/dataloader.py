import os
from typing import List, Dict
import frontmatter
from dateutil.parser import parse
from nlpjunk.entry import Entry
from nlpjunk.parser import Parser


def jekyll_format(s: str, p: Parser) -> Entry:
    post = frontmatter.loads(s)
    entry = Entry(
            title=post["title"],
            text=post.content,
            updated_at=parse(str(post["updated"])),
            meta=post.metadata,
            p=p)
    return entry


def load_files(dpath: str, fmt: str = "jekyll") -> List[Entry]:
    parser = Parser(pos=["名詞", "動詞", "形容詞"], word_normalize=True)

    entries = []
    if fmt == "jekyll":
        paths = [
                os.path.join(dpath, fname)
                for fname in os.listdir(dpath)
                if not (fname.startswith(".") or fname.startswith("README"))
                ]
        for p in paths:
            with open(p, "r") as f:
                entries.append(jekyll_format(f.read(), parser))
    else:
        print(f"{fmt} not exists.")
        raise ValueError

    return entries


def agg_text_monthly(entries: List[Entry]) -> Dict[int, str]:
    entries.sort()
    first_month: int = entries[0].updated_at.month
    last_month: int = entries[-1].updated_at.month

    month2text = {i: "" for i in range(first_month, last_month+1)}
    for ent in entries:
        month = ent.updated_at.month
        month2text[month] += ent.wakati_text + " "

    return month2text
