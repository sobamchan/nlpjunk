from nlpjunk.tfidf import get_feature_words


def test_get_feature_words():
    n = 2
    texts = [
            "hello world , normal one",
            "love world , good one",
            "hate world , bad one",
            ]
    gts = [
            ["hello", "normal"],
            ["love", "good"],
            ["hate", "bad"],
            ]

    words_li = get_feature_words(texts, n)

    for words, gt in zip(words_li, gts):
        assert set(words) == set(gt)
