def points_per_game(points, games):
    if games == 0:
        return 'На 0 делить нельзя!'
    else:
        return points/games

assert points_per_game(72, 6) == 12
assert points_per_game(72, 0) == 'На 0 делить нельзя!'
assert points_per_game(121, 11) == 11

print(sorted(["сыр", "огурец", "баклажан"], key=lambda word: len(word)))
