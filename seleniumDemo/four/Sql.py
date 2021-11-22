class SqlYju():

    create_table ='''
        drop table testdata;
        create table testdata(
        id int not null,
        bookname varchar(40),
        author varchar(30),
        result char(4)    # pass fail
        );
        '''
    insert_table = '''
        insert into testdata(id,bookname,author)
        values(1,'HTTP','qqq'),
            (2,'eee','rrr');
        '''
