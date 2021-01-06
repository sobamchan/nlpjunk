from datetime import datetime
import fire
from nlpjunk.dataloader import load_files
from nlpjunk.tfidf import get_feature_words


def generate(
        data_dir: str, date_from: str = None, date_to: str = None
        ):
    entries = load_files(data_dir, fmt="jekyll")

    if date_from:
        date_from = datetime.strptime(date_from, "%Y-%m-%d")
        entries =\
            list(filter(lambda ent: ent.updated_at.date() >= date_from.date(), entries))
    if date_to:
        date_to = datetime.strptime(date_to, "%Y-%m-%d")
        entries =\
            list(filter(lambda ent: ent.updated_at.date() <= date_to.date(), entries))

    words_li = [ent.wakati_text for ent in entries]

    feature_words = get_feature_words(words_li, n=3)
    breakpoint()


if __name__ == '__main__':
    fire.Fire()
