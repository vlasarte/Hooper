CREATE TABLE "Hooper"."Player"
(
    player_name character varying(100) COLLATE pg_catalog."default",
    team_id bigint NOT NULL,
    player_id bigint NOT NULL,
    season integer NOT NULL,
    CONSTRAINT "Player_pkey" PRIMARY KEY (player_id, team_id, season)
)


