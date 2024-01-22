def hard_init(game):
    difficult = {
        "null": {
            "name": "null",
            "sprite": game.cash["sprites"]["cells"]["null"],
            "count": 0,
            "visible": False,
            "tag": ""
        },

        "start": {
            "name": "start",
            "sprite": None,
            "count": 0,
            "visible": True,
            "tag": ""
        },

        "enemy_1": {
            "name": "enemy_1",
            "sprite": game.cash["sprites"]["cells"]["enemy_1"],
            "count": 30,
            "visible": False,
            "tag": "se"
        },

        "enemy_2": {
            "name": "enemy_2",
            "sprite": game.cash["sprites"]["cells"]["enemy_2"],
            "count": 9,
            "visible": False,
            "tag": "se"
        },

        "enemy_3": {
            "name": "enemy_3",
            "sprite": game.cash["sprites"]["cells"]["enemy_3"],
            "count": 9,
            "visible": False,
            "tag": "se"
        },

        "health_add_1": {
            "name": "health_add_1",
            "sprite": game.cash["sprites"]["cells"]["health_add_1"],
            "count": 6,
            "visible": False,
            "tag": "sgh",

            "add_health": 1
        },

        "health_add_3": {
            "name": "health_add_3",
            "sprite": game.cash["sprites"]["cells"]["health_add_3"],
            "count": 3,
            "visible": False,
            "tag": "sgh",

            "add_health": 3
        },

        "tnt": {
            "name": "tnt",
            "sprite": game.cash["sprites"]["cells"]["tnt"],
            "count": 8,
            "visible": False,
            "tag": "sg"
        },

        "gun_1": {
            "name": "gun_1",
            "sprite": game.cash["sprites"]["cells"]["gun_1"],
            "count": 1,
            "visible": False,
            "tag": "sg"
        },

        "gun_2": {
            "name": "gun_2",
            "sprite": game.cash["sprites"]["cells"]["gun_2"],
            "count": 1,
            "visible": False,
            "tag": "sg"
        },

        "gun_3": {
            "name": "gun_3",
            "sprite": game.cash["sprites"]["cells"]["gun_3"],
            "count": 1,
            "visible": False,
            "tag": "sg"
        },

        "gun_4": {
            "name": "gun_4",
            "sprite": game.cash["sprites"]["cells"]["gun_4"],
            "count": 1,
            "visible": False,
            "tag": "sg"
        },

        "gun_5": {
            "name": "gun_5",
            "sprite": game.cash["sprites"]["cells"]["gun_5"],
            "count": 1,
            "visible": False,
            "tag": "sg"
        },

        "fuel": {
            "name": "fuel",
            "sprite": game.cash["sprites"]["cells"]["fuel"],
            "count": 2,
            "visible": False,
            "tag": "sg"
        },

        "detail": {
            "name": "detail",
            "sprite": game.cash["sprites"]["cells"]["detail"],
            "count": 1,
            "visible": False,
            "tag": "sg"
        },

        "ship": {
            "name": "ship",
            "sprite": game.cash["sprites"]["cells"]["ship"],
            "count": 1,
            "visible": False,
            "tag": "s"
        }
    }

    return difficult
