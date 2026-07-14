# PLAN — Cycle 1: 거터 게임 (Gutter Game)

## 1. 목표 (RED 1단계)

**단 하나의 동작**: 20번의 롤이 전부 0핀(거터볼)이면, `score()`는 `0`을 반환한다.

이번 사이클의 목적은 스코어링 규칙이 아니라, `Game` 클래스와 `roll()` / `score()`의
가장 단순한 골격(스킵 프레임/스트라이크/스페어 없음)을 세우는 것이다.

## 2. 작성할 실패 테스트

- 파일: `test_bowling.py`
- 테스트: `test_all_gutter_balls_scores_zero`

```python
from bowling import Game

def test_all_gutter_balls_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)

    assert game.score() == 0
```

**예상 실패 이유**: `bowling.py` 모듈과 `Game` 클래스가 아직 존재하지 않으므로
`ModuleNotFoundError`(또는 `ImportError`)로 실패해야 한다.

## 3. 구현 방향 (GREEN에서 진행 — 지금은 작성하지 않음)

- 파일: `bowling.py`
- `Game.__init__`: 롤 기록용 리스트(`self.rolls = []`) 초기화
- `Game.roll(pins)`: `self.rolls.append(pins)`
- `Game.score()`: 이번 사이클을 통과시키는 최소 구현 — 예: `sum(self.rolls)`
  (스트라이크/스페어 보너스 로직은 다음 사이클들에서 하나씩 추가하며 자연스럽게 대체된다)

## 4. 이번 사이클 범위가 아닌 것

- 오픈 프레임(스트라이크/스페어 없는 일반 프레임) 합산 — 다음 사이클
- 스페어 보너스 (10 + 다음 1롤)
- 스트라이크 보너스 (10 + 다음 2롤)
- 퍼펙트 게임(300점)
- 10프레임 보너스 롤 처리

각각은 별도의 RED-GREEN-REVIEW 사이클로 하나씩 다룬다.

## 5. 완료 기준

- [ ] `test_bowling.py::test_all_gutter_balls_scores_zero`가 RED 상태에서
      `ModuleNotFoundError`/`ImportError`로 실패하는 것을 확인
- [ ] 위 실패를 사용자가 검토·승인
- [ ] 승인 후 PLAN.md + 실패 테스트 commit
