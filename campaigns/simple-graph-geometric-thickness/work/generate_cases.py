"""Fix reproducible small polynomial source cases before construction."""

import json
import random
from pathlib import Path


def atom(terms,relation):
    return {"terms":terms,"relation":relation}


def instance(n,*constraints):
    return {"variables":n,"constraints":list(constraints)}


EDGE_CASES = [
    (instance(0),True),
    (instance(0,atom([[1,[]]],"=")),False),
    (instance(0,atom([[1,[]]],">")),True),
    (instance(1,atom([[1,[1]]],"=")),True),
    (instance(1,atom([[1,[1]],[-1,[0]]],"=")),True),
    (instance(1,atom([[1,[1]],[1,[0]]],"=")),True),
    (instance(1,atom([[1,[2]],[-1,[0]]],"=")),True),
    (instance(1,atom([[1,[2]],[1,[0]]],"=")),False),
    (instance(1,atom([[1,[2]]],"<")),False),
    (instance(1,atom([[1,[2]]],">=")),True),
    (instance(1,atom([[1,[1]],[-1,[0]]],">="),atom([[1,[1]]],"<")),False),
    (instance(1,atom([[1,[1]]],">"),atom([[1,[1]]],"<")),False),
    (instance(1,atom([[1,[1]]],"!=")),True),
    (instance(2,atom([[1,[1,0]],[1,[0,1]],[-1,[0,0]]],"=")),True),
    (instance(2,atom([[1,[1,0]]],"="),atom([[1,[0,1]]],"=")),True),
    (instance(2,atom([[1,[1,0]]],">"),atom([[1,[1,0]]],"<=")),False),
    (instance(2,atom([[1,[1,1]],[-1,[0,0]]],"=")),True),
    (instance(2,atom([[1,[2,0]],[1,[0,2]],[1,[0,0]]],"=")),False),
    (instance(3,atom([[1,[1,0,0]]],"=")),True),
    (instance(3,atom([[1,[1,0,0]]],">"),atom([[1,[1,0,0]]],"<")),False),
]


def random_source(seed):
    rng = random.Random(seed)
    n = rng.randint(1,3)
    values = [rng.randint(-5,5) for _ in range(n)]
    constraints = []
    for i,value in enumerate(values):
        powers = [int(j == i) for j in range(n)]
        constraints.append(atom([[1,powers],[-value,[0]*n]],"="))
    if seed % 2:
        powers = [int(j == 0) for j in range(n)]
        constraints.append(atom([[1,powers],[-(values[0]+1),[0]*n]],">="))
    else:
        powers = [int(j == 0)*2 for j in range(n)]
        constraints.append(atom([[1,powers],[-values[0]**2,[0]*n]],"="))
    return instance(n,*constraints)


def build_cases():
    from check import solve_source
    cases,seen = [],set()

    def add(source,kind,seed=None,expected=None):
        key = json.dumps(source,sort_keys=True,separators=(",",":"))
        if key in seen:
            return False
        answer = solve_source(source)
        if expected is not None and ("values" in answer) != expected:
            raise AssertionError(f"Hand label disagrees with oracle: {source}")
        seen.add(key)
        case = {"source":source,"kind":kind,"expected":answer}
        if seed is not None:
            case["seed"] = seed
        cases.append(case)
        return True

    for source,expected in EDGE_CASES:
        add(source,"edge",expected=expected)
    seed = 0
    while sum(case["kind"] == "random" for case in cases) < 100:
        add(random_source(seed),"random",seed=seed)
        seed += 1
    return cases


if __name__ == "__main__":
    path = Path(__file__).with_name("cases.json")
    cases = build_cases()
    path.write_text(json.dumps(cases,indent=2)+"\n")
    print(f"Wrote {len(cases)} cases to {path}")
