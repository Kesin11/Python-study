#coding: utf-8
import sqlite3, sys, multiprocessing, os, time
def select_lecture(db_lecturename):
    db, lecture_name = db_lecturename
    _conn = sqlite3.connect(db)
    _conn.row_factory = sqlite3.Row
    for row in _conn.execute("select * from freqfile where lecture = ?", (lecture_name, )):
        print "pid; %s, ipu: %s" % (os.getpid(), row['ipu'])
        time.sleep(0.1)
        strings = row['word'].strip().split('\n')
        for string in strings:
            freq, word = string.split(' ')
            #print freq, word
    _conn.close()

if __name__ == '__main__':
    con = sqlite3.connect("data.db")
    #テーブル作成
    #con.execute(u"create table テスト(整数 integer, 小数 real, 文字 text);")
    #レコード挿入
    con.execute(u"insert into テスト values (1, 1.23, 'てすとてすと')")
    #プレースホルダとバインドを使用
    sql = u"insert into テスト values(?,?,?)"
    con.execute(sql, (2, 3.45, u'テスト'))
    
    #レコード取得
    c = con.execute(u"select * from テスト")
    for row in c:
        print row[0], row[1], row[2]
    
    #名前でのアクセス
    con.row_factory = sqlite3.Row
    for row in con.execute(u"select * from テスト"):
        print row['整数'], row['小数'], row['文字']
    con.commit()
    con.close()
    
    #freqfile, collectionsを使った実践的なテスト
    db = sys.argv[1]
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    print "show freqfile"
    for row in conn.execute("select * from freqfile"):
        lecture = ['lecture']
        ipu = row['ipu']
        print row['lecture'], row['ipu']
        word_freq={}
        strings = row['word'].strip().split('\n')
        for string in strings:
            freq, word = string.split(' ')
            word_freq[word] = int(freq)
            print "%s %s" % (word, freq)
    
    print "show distinct lecture name"
    for row in conn.execute("select distinct lecture from freqfile"):
        lecture_name = row['lecture']
        print "Lecture: %s" % lecture_name
        sql = "select * from freqfile where lecture = ?;"
        for lecture in conn.execute(sql, (lecture_name,)):
            print lecture['ipu']
            print lecture['word']
        
    print "show collections table"
    for row in conn.execute("select * from collections"):
        print row['prob'], row['word']
        
    print "show freqfile using multiprocess"
    pool = multiprocessing.Pool()
    lecture_names = [(db, lecture['lecture']) for lecture in conn.execute("select distinct lecture from freqfile")]
    results = pool.imap(select_lecture, lecture_names)
    for result in results:
        pass
    conn.close()
    
        
    
    