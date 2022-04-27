#!/usr/bin/env python3
import copy

import tcod

import entity_factories
from input_handlers import EventHandler
from engine import Engine
from procgen import generate_dungeon, generate_dungeon_umberhulk


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 5
    max_rooms = 20

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "E:\E\_Programming\Python Game\dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD # !! Update tileset (Also CHARMAP_TCOD is outdated?)
    )

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)

    game_map = generate_dungeon( # !! Use more and different generators
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()