from check import solve_source,valid_source


def atom(terms,relation):
    return {"terms":terms,"relation":relation}


def test_hand_cases():
    positive = {"variables":1,"constraints":[atom([[1,[1]],[-2,[0]]],"=")]}
    assert valid_source(positive,{"values":[[2,1]]})
    assert not valid_source(positive,{"values":[[1,1]]})
    negative = {"variables":1,"constraints":[atom([[1,[2]],[1,[0]]],"=")]}
    assert solve_source(negative) == {"status":"NO-SOLUTION"}
    irrational = {"variables":1,"constraints":[atom([[1,[2]],[-2,[0]]],"=")]}
    try:
        solve_source(irrational)
    except RuntimeError as error:
        assert "Algebraic witness encoding pending" in str(error)
    else:
        raise AssertionError("Irrational source witness was silently treated as rational")


if __name__ == "__main__":
    test_hand_cases()
