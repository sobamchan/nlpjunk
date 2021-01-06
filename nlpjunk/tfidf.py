from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer


def get_feature_words(texts: List[str], n: int = 2) -> List[List[str]]:
    """
    Calculate n feature words for each string from texts by using tf-idf.
    """
    vectorizer = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')
    vecs = vectorizer.fit_transform(texts).todense()
    argsorted_vecs = (-1 * vecs).argsort(axis=1)

    idx2voc = {idx: voc for voc, idx in vectorizer.vocabulary_.items()}

    return [
            [idx2voc[idx] for idx in vec[:n]]
            for vec in argsorted_vecs.tolist()
            ]
