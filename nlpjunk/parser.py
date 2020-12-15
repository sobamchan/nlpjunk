from typing import List
import MeCab
import neologdn


class Parser:
    """
    分ち書きをするクラス、
    Attributes
    ----------
    tagger : Mecab.Tagger
    word_normalize : boolean
        true : 単語の原形のリストを返します
        false : 単語の表層形のリストを返します
    pos_fileters : list
        学習の対象となる品詞セット名のリスト
        e.g. : ["名詞", "動詞"]
    """

    def __init__(
            self, pos=[], word_normalize=False, remove_proper_nouns=False):
        self.tagger = MeCab.Tagger("-Owakati")
        self.word_normalize = word_normalize
        self.pos_filters = pos
        self.remove_proper_nouns = remove_proper_nouns

    def extract(self, text: str) -> str:
        """
        posで指定された品詞を文章から抽出する。
        Parameters
        ----------
        text : string
            解析対象となる文字列
        Returns
        -------
        text : string
            解析結果となる文字列、スペース区切りで一つの文字列として返す
        """
        text = neologdn.normalize(text)
        node = self.tagger.parseToNode(text)
        base = []
        surface = []
        while node:
            features = node.feature.split(",")
            if not features[0] == "BOS/EOS":
                if self.remove_proper_nouns and features[1] == "固有名詞":
                    pass
                else:
                    if self.pos_filters:
                        if features[0] in self.pos_filters:
                            # 原型が*となってしまっている場合、元の単語をbaseに追加する。
                            base.append(
                                features[-3]
                                if features[-3] != "*" else node.surface
                            )
                            surface.append(node.surface)
                    else:
                        base.append(
                            features[-3]
                            if features[-3] != "*" else node.surface
                            )
                        surface.append(node.surface)
            node = node.next
        if self.word_normalize:
            return " ".join(base)
        else:
            return " ".join(surface)

    def tokenize(self, text: str) -> List[str]:
        """extract alias"""
        return self.extract(text).split(" ")
