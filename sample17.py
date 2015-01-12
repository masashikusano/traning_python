#coding:utf-8
import MeCab
tagger = MeCab.Tagger("-Ochasen")
node = tagger.parseToNode("PythonからMeCabの形態素解析機能を使ってみました。")
while node:
    print "%s %s" % (node.surface, node.feature)
    node = node.next
