# PLAN — Cycle 3: 스트라이크 보너스 (Strike Bonus)

## 0. 이전 사이클

- Cycle 1(거터 게임): `score()` = `sum(self.rolls)` — 완료·커밋됨
- Cycle 2(스페어 보너스): `score()`가 프레임을 2롤씩 순회하며 스페어(2롤 합 10)에
  `10 + 다음 1롤`을 더하도록 개선 — 완료·커밋됨

현재 `score()`는 **모든 프레임이 정확히 2롤을 소비한다**고 가정한다. 스트라이크는
1롤만으로 프레임이 끝나므로, 이 가정이 깨지는 첫 사례다.

## 1. 목표 (RED 1단계)

**단 하나의 동작**: 스트라이크(첫 롤에서 10핀)를 기록한 프레임은
`10 + 다음 2롤의 핀 수 합`을 프레임 점수로 받고, 그 프레임은 롤 1개만 소비한다.

## 2. 작성할 실패 테스트

- 파일: `test_bowling.py`
- 테스트: `test_strike_adds_next_two_rolls_as_bonus`

```python
def test_strike_adds_next_two_rolls_as_bonus():
    game = Game()
    game.roll(10)  # 1프레임: 스트라이크 (롤 1개만 소비)
    game.roll(3)
    game.roll(4)   # 2프레임: 3 + 4 = 7 (오픈)
    for _ in range(16):
        game.roll(0)  # 3~10프레임: 전부 거터

    # 1프레임: 10 + 3 + 4(보너스) = 17
    # 2프레임: 3 + 4 = 7
    # 3~10프레임: 0
    assert game.score() == 24
```

**예상 실패 이유**: 현재 `score()`는 프레임마다 정확히 2롤을 소비한다고 가정하고
순회하므로, 스트라이크로 인해 실제 롤 개수(19개)와 순회 인덱스가 어긋난다.
그 결과 `IndexError: list index out of range`(또는 그 전에 잘못된 총점)로 실패한다 —
스트라이크를 인식하지 못해서 생기는 실패이지, 오타나 우연한 값 불일치가 아니다.

## 3. 구현 방향 (GREEN에서 진행 — 지금은 작성하지 않음)

`score()`의 프레임 순회 로직에 스트라이크 분기를 추가한다:

- 각 프레임 시작에서 `rolls[roll_index]`가 10이면(스트라이크):
  - `10 + rolls[roll_index + 1] + rolls[roll_index + 2]`를 더한다
  - `roll_index`는 **1**만 전진 (스트라이크는 롤 1개만 소비)
- 스트라이크가 아니면 기존 스페어/오픈 프레임 로직을 그대로 적용하고
  `roll_index`는 2 전진

## 4. 이번 사이클 범위가 아닌 것

- 퍼펙트 게임(연속 스트라이크, 300점) — 다음 사이클
- 10프레임에서의 스페어/스트라이크 보너스 롤 처리 — 이후 사이클

## 5. 완료 기준

- [ ] `test_bowling.py::test_strike_adds_next_two_rolls_as_bonus`가 RED 상태에서
      `IndexError`(또는 잘못된 총점)로 실패하는 것을 확인
- [ ] 위 실패를 사용자가 검토·승인
- [ ] 승인 후 PLAN.md + 실패 테스트 commit
