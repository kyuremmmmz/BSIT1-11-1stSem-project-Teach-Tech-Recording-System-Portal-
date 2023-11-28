use for_teacher_form;
create table add_button(
student_id bigint primary key auto_increment,
l_name varchar(250) not null,
m_initial varchar(250) not null,
g_name varchar(250) not null, 
age int not null,
p1_grade int not null, 
p2_grade int not null,
p3_grade int not null,
final_grade int not null
);