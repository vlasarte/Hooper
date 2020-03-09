-- Table: "Hooper"."Player"

-- DROP TABLE "Hooper"."Player";

CREATE TABLE "Hooper"."Player"
(
    player_name character varying(100) COLLATE pg_catalog."default",
    team_id bigint NOT NULL,
    player_id bigint NOT NULL,
    season integer NOT NULL,
    age smallint NOT NULL DEFAULT 21,
    "position" character varying(1) COLLATE pg_catalog."default" DEFAULT 'F'::character varying,
    CONSTRAINT "Player_pkey" PRIMARY KEY (player_id, team_id, season)
)

TABLESPACE pg_default;

ALTER TABLE "Hooper"."Player"
    OWNER to postgres;


-- Table: "Hooper"."Game"

-- DROP TABLE "Hooper"."Game";

CREATE TABLE "Hooper"."Game"
(
    game_date_est timestamp without time zone NOT NULL,
    game_id bigint NOT NULL,
    game_status_text character varying(20) COLLATE pg_catalog."default",
    home_team_id bigint NOT NULL,
    visitor_team_id bigint,
    season integer,
    team_id_home bigint,
    pts_home numeric(4,1),
    fg_pct_home numeric(4,3),
    ft_pct_home numeric(4,3),
    fg3_pct_home numeric(4,3),
    ast_home numeric(4,1),
    reb_home numeric(4,1),
    team_id_away bigint,
    pts_away numeric(4,1),
    fg_pct_away numeric(4,3),
    ft_pct_away numeric(4,3),
    fg3_pct_away numeric(4,3),
    ast_away numeric(4,1),
    reb_away numeric(4,1),
    home_team_wins boolean,
    CONSTRAINT "Game_pkey" PRIMARY KEY (game_id)
)

TABLESPACE pg_default;

ALTER TABLE "Hooper"."Game"
    OWNER to postgres;