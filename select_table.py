#1.Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
select * from 
where user_id = 11;

#2.Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select t1.* from tasks as t1
where status_id in (select * from status where name = 'New');

#3.Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
update tasks
 set status_id = 5
where status_id = 4;

#4.Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
select * from users
where id not in (select user_id from tasks );

#5.Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
insert into tasks
values (21,'Task','About task',4,19);

#6.Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
select * from tasks
where status_id in (4,5);

#7.Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
delete tasks
where id = 1;

#8.Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
select * from users
where email like '%.com'

#9.Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
update users
set fullname = 'Paul Smith'
where id = 11;

#10.Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
select status_id,count() from tasks
group by status_id;

#11.Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в 
    #поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
select t1.*,t2.fullname,t2.email
 from tasks as t1
   join users as t2 on t2.id = t1.user_id
                  and t2.email like '%@example.com';

#12.Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
select  from tasks
where description is null;

#13.Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайт
#  inner JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
select t1.*,t2.fullname from tasks as t1
 inner join user as t2 on t2.id = t1.user_id
 inner join status as t3 on t3.id = t1.status_id
                          and t3.name = 'In progress';

#14.Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
select t2.fullname,count() from tasks as t1
left join user as t2 on t2.id = t1.user_id
group by t2.fullname;
