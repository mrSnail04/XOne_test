SELECT bid.b_id as client_number,
Count(CASE WHEN event_value.outcome='win' THEN 1 ELSE NULL END) as win,
Count(CASE WHEN event_value.outcome='lose' THEN 1 ELSE NULL END) as lose
FROM event_entity
INNER JOIN event_value
    ON event_entity.play_id = event_value.play_id
INNER JOIN bid
    ON event_entity.play_id = bid.play_id
GROUP BY bid.b_id;

