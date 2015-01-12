#coding:utf-8
import MeCab

def extractKeyword(text):
    """textを形態素解析して、名詞のみのリストを返す"""
    tagger = MeCab.Tagger('-Ochasen')
    node = tagger.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            keywords.append(node.surface)
        node = node.next
    return keywords

if __name__ == "__main__":
    keywords = extractKeyword(u"PythonからMeCabの形態素解析機能を使ってみました。")
    for w in keywords:
        print w,
    print
    keywords = extractKeyword(u"菅直人首相は野党の出方や世論を見極めつつ判断する考えだ。")
    for w in keywords:
        print w,
