SELECT *
FROM Employee e1
JOIN Employee e2
    ON e1.id = e2.managerID
GROUP BY e1.id
HAVING COUNT(e1.id) >= 5