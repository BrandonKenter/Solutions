SELECT 
    h.team_name AS home_team, 
    a.team_name AS away_team
FROM Teams h JOIN Teams a
ON h.team_name != a.team_name