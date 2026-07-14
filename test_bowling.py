from bowling import Game


def test_all_gutter_balls_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)

    assert game.score() == 0


def test_spare_adds_next_roll_as_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)  # 1프레임: 스페어
    game.roll(3)  # 2프레임 첫 롤 — 스페어 보너스로도 사용됨
    game.roll(0)  # 2프레임 두 번째 롤
    for _ in range(16):
        game.roll(0)  # 3~10프레임: 전부 거터

    assert game.score() == 16
