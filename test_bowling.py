from bowling import Game


def test_all_gutter_balls_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)

    assert game.score() == 0
