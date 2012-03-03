#coding: utf-8
import MeCab

if __name__ == '__main__':
    string = "私はあいつに来い、と命じることにした。"
    t = MeCab.Tagger()
    node = t.parseToNode(string)
    while node:
        #基本形を取り出す
        feature = node.feature.split(",")[6]
        print feature
        node = node.next
    print "end"
    