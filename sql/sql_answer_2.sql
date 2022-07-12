SELECT games.game as game, Count(DISTINCT games.play_id) as games_count
FROM
((SELECT play_id, Concat(event_entity.home_team, ' - ', event_entity.away_team) as game FROM event_entity)
UNION ALL
(SELECT play_id, Concat(event_entity.away_team, ' - ', event_entity.home_team) as game FROM event_entity)) as games
GROUP BY games.game;