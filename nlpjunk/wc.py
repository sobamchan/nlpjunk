from wordcloud import WordCloud


def gen_wc(text: str):
    wc = WordCloud(
            font_path="./assets/NotoSansCJKjp-Bold.otf"
            ).generate_from_text(text)
    return wc
