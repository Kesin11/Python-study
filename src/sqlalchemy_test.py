#coding: utf-8
'''
SQLAlchemy tutorial
'''
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class User(Base):
    __tablename__='users'
    
    #If you use NOT 'sqlite' or 'postgresql' , you need String length like 'String(50)'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
        
    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

if __name__ == '__main__':
    engine = create_engine('sqlite://///Users/Kenta/tmpdata/sqalchemy_test.sqlite3', echo=True)
    Base.metadata.create_all(engine)
    
    #セッション作成
    Session = sessionmaker(bind=engine)
    #Sessinに後から追加する場合はconfigureを使用する
    #Session.configure(bind=engine)
    session = Session()
    
    #データの追加
    ed_user = User('ed', 'Ed Jones', 'edpassword')
    session.add(ed_user)
    #コミットされてなければクエリ実行前にフラッシュが行われる（コミットされてないからロールバックで戻せる変更？）
    our_user = session.query(User).filter_by(name='ed').first()
    print 'our_user: ', our_user
    
    #一括してセッションに追加
    session.add_all([
                     User('wendy', 'Wen Will', 'footbar'),
                     User('mary', 'Mary Con', 'foo'),
                     User('fred', 'Fred Wesry', 'bar')
                     ])
    #変更を検知
    ed_user.password = 'f8s7ccs'
    print 'session.dirty: ', session.dirty
    #追加したオブジェクトの処理待ちを検知
    print 'session.new: ', session.new
    #トランザクションをコミット
    session.commit()
    
    #ロールバック処理は省略
    
    #クエリ発行
    #Userインスタンスを読み出す
    for instance in session.query(User).order_by(User.id):
        print instance.name, instance.fullname
    #タプルで受け取ることも可能
    for name, fullname in session.query(User.name, User.fullname):
        print name, fullname
    #LIMIT, OFFSETの操作をPythonのスライスで実行できる
    for user in session.query(User).order_by(User.id)[1:3]:
        print user
    #filter_byは簡易。filterを使うとPythonの標準的な演算子を使える
    for name, in session.query(User.name).filter(User.fullname == 'Ed Jones'):
        print name
    #filterを2回呼びだしてAND検索
    for usr in session.query(User).filter(User.name=='ed').filter(User.id == 1):
        print usr
    #LIKE, INなども可能である。省略
    #SQLAlchemyのSQL式の他にSQLの文字列にも対応。from_statement()で完全に生のSQL文も使える
    for usr in session.query(User).filter("id<5").order_by("id").all():
        print usr
    #count()も可能
    print session.query(User).filter(User.name.like('%ed')).count()

    session.close()
    