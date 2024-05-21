SELECT "user".id AS user_id, "user".name AS user_name, COUNT(reservation.reservation_id) AS reservation_count 
FROM "User" AS "user"
JOIN reservation ON "user".id = reservation.guest_id
GROUP BY "user".id, "user".name
ORDER BY reservation_count DESC
LIMIT 1;
