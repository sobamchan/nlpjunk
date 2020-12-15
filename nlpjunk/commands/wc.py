from datetime import datetime
import fire
from nlpjunk.dataloader import load_files
from wordcloud import WordCloud


def generate(
        data_dir: str, opath: str, date_from: str = None,
        date_to: str = None):
    entries = load_files(data_dir, fmt='jekyll')

    if date_from:
        date_from = datetime.strptime(date_from, "%Y-%m-%d")
        entries =\
            list(filter(lambda ent: ent.updated_at.date() >= date_from.date(), entries))
    if date_to:
        date_to = datetime.strptime(date_to, "%Y-%m-%d")
        entries =\
            list(filter(lambda ent: ent.updated_at.date() <= date_to.date(), entries))

    words = ' '.join([ent.wakati_text for ent in entries])
    wordcloud =\
        WordCloud(
                width=800,
                height=400,
                font_path='./assets/NotoSansCJKjp-Bold.otf').generate(words)
    print(f'saving image to {opath}')
    wordcloud.to_image().save(opath)


if __name__ == '__main__':
    fire.Fire()
