# https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    player_idx_dict = {player: i for i, player in enumerate(players)}
    idx_player_dict = {i: player for i, player in enumerate(players)}

    for call in callings:
        cur_idx = player_idx_dict[call]
        pre_idx = cur_idx - 1
        cur_player = call
        pre_player = idx_player_dict[pre_idx]

        player_idx_dict[cur_player] = pre_idx
        player_idx_dict[pre_player] = cur_idx

        idx_player_dict[pre_idx] = cur_player
        idx_player_dict[cur_idx] = pre_player

    return list(idx_player_dict.values())
