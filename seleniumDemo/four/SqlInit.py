class SqlYju():
    create_table = '''
        # DROP TABLE IF EXISTS `testdata`;
        CREATE TABLE IF NOT EXISTS `testdata`(
        id int not null,
        bookname varchar(40),
        author varchar(30),
        result char(4)  
        ); 
        '''
    insert_table = '''
        insert into testdata(id,bookname,author)
        values(1,'HTTP','qqq'),
            (2,'eee','rrr');
        '''
