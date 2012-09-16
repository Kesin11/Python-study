#coding: utf-8
import pymongo

if __name__ == '__main__':
    conn = pymongo.Connection()
    #testというデータベースのtest_collectというコレクションに接続
    db = conn.test.test_collect

    #dict型をそのままinsertできる
    dic = {'id':1, 'name':'user'}
    db.insert(dic)
    
    print "SELECT ONE"
    print db.find_one()

    print "SELECT *"
    for data in db.find():
        print data
    
    print "SELECT * FROM test_collection WHERE id=1"
    for data in db.find({'id':1}):
        print "id: %s" % data['id'], data
    print "SELECT name FROM test_collection WHERE id=1"
    for data in db.find({'id':1},{'name':True}):
        print data

    print "COUNT"
    print db.count()
    print db.find({'name':'user'}).count()

    print "LIMIT"
    for data in db.find().limit(2):
        print data
    
    print "UPDATE"
    db.update({'id':1},{'$set':{'name':'updated'}})
    print [data for data in db.find({'name':'updated'})]
    
    print "SAVE python的に変更したものをdbに反映"
    for data in db.find({'id':1}).limit(3):
        data['id'] = 10
        db.save(data)
    print [data for data in db.find({'id':10})]

    conn.close()
