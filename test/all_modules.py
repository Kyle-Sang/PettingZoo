from pettingzoo.atari import (
    basketball_pong_v2,
    boxing_v1,
    combat_plane_v1,
    combat_tank_v1,
    double_dunk_v2,
    entombed_competitive_v2,
    entombed_cooperative_v2,
    flag_capture_v1,
    foozpong_v2,
    ice_hockey_v1,
    joust_v2,
    mario_bros_v2,
    maze_craze_v2,
    othello_v2,
    pong_v2,
    quadrapong_v3,
    space_invaders_v1,
    space_war_v1,
    surround_v1,
    tennis_v2,
    video_checkers_v3,
    volleyball_pong_v2,
    warlords_v2,
    wizard_of_wor_v2,
)
from pettingzoo.butterfly import (
    cooperative_pong_v3,
    knights_archers_zombies_v7,
    pistonball_v4,
    prison_v3,
    prospector_v4,
)
from pettingzoo.classic import (
    backgammon_v3,
    checkers_v3,
    chess_v4,
    connect_four_v3,
    dou_dizhu_v4,
    gin_rummy_v4,
    go_v5,
    hanabi_v4,
    leduc_holdem_v4,
    mahjong_v4,
    rps_v2,
    texas_holdem_no_limit_v5,
    texas_holdem_v4,
    tictactoe_v3,
    uno_v4,
)
from pettingzoo.magent import (
    adversarial_pursuit_v3,
    battle_v3,
    battlefield_v3,
    combined_arms_v5,
    gather_v3,
    tiger_deer_v3,
)
from pettingzoo.mpe import (
    simple_adversary_v2,
    simple_crypto_v2,
    simple_push_v2,
    simple_reference_v2,
    simple_speaker_listener_v3,
    simple_spread_v2,
    simple_tag_v2,
    simple_v2,
    simple_world_comm_v2,
)
from pettingzoo.sisl import multiwalker_v7, pursuit_v3, waterworld_v3

all_prefixes = ["atari", "classic", "butterfly", "magent", "mpe", "sisl"]

manual_environments = {
    "butterfly/knights_archers_zombies",
    "butterfly/pistonball",
    "butterfly/cooperative_pong",
    "butterfly/prison",
    "butterfly/prospector",
    "sisl/pursuit",
}

all_environments = {
    "atari/basketball_pong_v2": basketball_pong_v2,
    "atari/boxing_v1": boxing_v1,
    "atari/combat_tank_v1": combat_tank_v1,
    "atari/combat_plane_v1": combat_plane_v1,
    "atari/double_dunk_v2": double_dunk_v2,
    "atari/entombed_cooperative_v2": entombed_cooperative_v2,
    "atari/entombed_competitive_v2": entombed_competitive_v2,
    "atari/flag_capture_v1": flag_capture_v1,
    "atari/foozpong_v2": foozpong_v2,
    "atari/joust_v2": joust_v2,
    "atari/ice_hockey_v1": ice_hockey_v1,
    "atari/maze_craze_v2": maze_craze_v2,
    "atari/mario_bros_v2": mario_bros_v2,
    "atari/othello_v2": othello_v2,
    "atari/pong_v2": pong_v2,
    "atari/quadrapong_v3": quadrapong_v3,
    "atari/space_invaders_v1": space_invaders_v1,
    "atari/space_war_v1": space_war_v1,
    "atari/surround_v1": surround_v1,
    "atari/tennis_v2": tennis_v2,
    "atari/video_checkers_v3": video_checkers_v3,
    "atari/volleyball_pong_v2": volleyball_pong_v2,
    "atari/wizard_of_wor_v2": wizard_of_wor_v2,
    "atari/warlords_v2": warlords_v2,
    "classic/chess_v4": chess_v4,
    "classic/checkers_v3": checkers_v3,
    "classic/rps_v2": rps_v2,
    "classic/connect_four_v3": connect_four_v3,
    "classic/tictactoe_v3": tictactoe_v3,
    "classic/leduc_holdem_v4": leduc_holdem_v4,
    "classic/mahjong_v4": mahjong_v4,
    "classic/texas_holdem_v4": texas_holdem_v4,
    "classic/texas_holdem_no_limit_v5": texas_holdem_no_limit_v5,
    "classic/uno_v4": uno_v4,
    "classic/dou_dizhu_v4": dou_dizhu_v4,
    "classic/gin_rummy_v4": gin_rummy_v4,
    "classic/go_v5": go_v5,
    "classic/hanabi_v4": hanabi_v4,
    "classic/backgammon_v3": backgammon_v3,
    "butterfly/knights_archers_zombies_v7": knights_archers_zombies_v7,
    "butterfly/pistonball_v4": pistonball_v4,
    "butterfly/cooperative_pong_v3": cooperative_pong_v3,
    "butterfly/prison_v3": prison_v3,
    "butterfly/prospector_v4": prospector_v4,
    "magent/adversarial_pursuit_v3": adversarial_pursuit_v3,
    "magent/battle_v3": battle_v3,
    "magent/battlefield_v3": battlefield_v3,
    "magent/combined_arms_v5": combined_arms_v5,
    "magent/gather_v3": gather_v3,
    "magent/tiger_deer_v3": tiger_deer_v3,
    "mpe/simple_adversary_v2": simple_adversary_v2,
    "mpe/simple_crypto_v2": simple_crypto_v2,
    "mpe/simple_push_v2": simple_push_v2,
    "mpe/simple_reference_v2": simple_reference_v2,
    "mpe/simple_speaker_listener_v3": simple_speaker_listener_v3,
    "mpe/simple_spread_v2": simple_spread_v2,
    "mpe/simple_tag_v2": simple_tag_v2,
    "mpe/simple_world_comm_v2": simple_world_comm_v2,
    "mpe/simple_v2": simple_v2,
    "sisl/multiwalker_v7": multiwalker_v7,
    "sisl/waterworld_v3": waterworld_v3,
    "sisl/pursuit_v3": pursuit_v3,
}
