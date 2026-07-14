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


def test_strike_adds_next_two_rolls_as_bonus():
    game = Game()
    game.roll(10)  # 1프레임: 스트라이크 (롤 1개만 소비)
    game.roll(3)
    game.roll(4)   # 2프레임: 3 + 4 = 7 (오픈)
    for _ in range(16):
        game.roll(0)  # 3~10프레임: 전부 거터

    assert game.score() == 24


def test_tenth_frame_strike_gets_two_bonus_rolls():
    game = Game()
    for _ in range(9):
        game.roll(0)
        game.roll(0)   # 1~9프레임: 전부 거터
    game.roll(10)      # 10프레임: 스트라이크
    game.roll(3)       # 보너스 롤 1
    game.roll(4)       # 보너스 롤 2

    assert game.score() == 17


def test_tenth_frame_spare_gets_one_bonus_roll():
    game = Game()
    for _ in range(9):
        game.roll(0)
        game.roll(0)   # 1~9프레임: 전부 거터
    game.roll(5)
    game.roll(5)       # 10프레임: 스페어
    game.roll(3)       # 보너스 롤

    assert game.score() == 13
