# Write your MySQL query statement below
select Weather.id from Weather 
join Weather w
on DATEDIFF(weather.recordDate,w.recordDate)=1
AND weather.Temperature > w.Temperature;