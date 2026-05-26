SELECT 
    ROUND((SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(DISTINCT(customer_id)))*100,2) AS immediate_percentage
    FROM (
    SELECT *,
        RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as first_od
        FROM Delivery
    ) a
    WHERE first_od = '1'