class Sqlyu():

    create_table = '''
        drop table stu;
        create table stu(
        id int not null,
        can varchar(10),
        yu varchar(10),
        result char(4)
        );
        '''
    
    insert_table = '''
        insert into stu(id,can,yu)
        values(1,'Demon','Demon'),
              (2,'laohu','laohu');
        '''