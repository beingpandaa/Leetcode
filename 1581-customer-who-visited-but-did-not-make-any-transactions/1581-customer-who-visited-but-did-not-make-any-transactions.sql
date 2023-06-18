# Write your MySQL query statement below
select Visits.customer_id ,count(Visits.customer_id) as count_no_trans 
from Visits
left join Transactions
on Visits.visit_id = Transactions.visit_id
where Transactions.transaction_id  IS NULL
group by Visits.customer_id 



# SELECT
# 	customer_id,
# 	COUNT(Visits.visit_id) AS count_no_trans
# FROM
# 	visits
# LEFT JOIN Transactions
# 	ON Visits.visit_id = Transactions.visit_id
# WHERE 
# 	Transactions.visit_id IS NULL
# GROUP BY customer_id
