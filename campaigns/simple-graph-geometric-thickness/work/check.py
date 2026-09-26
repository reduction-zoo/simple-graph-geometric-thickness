"""Partial exact source oracle for real-polynomial conjunctions."""

import argparse
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import z3


RELATIONS = {"=","!=","<","<=",">",">="}


def legal_source(source):
    if not isinstance(source,dict) or set(source) != {"variables","constraints"}:
        return False
    n,constraints = source["variables"],source["constraints"]
    return (type(n) is int and n >= 0 and isinstance(constraints,list)
            and all(isinstance(atom,dict) and set(atom) == {"terms","relation"}
                    and atom["relation"] in RELATIONS and isinstance(atom["terms"],list)
                    and all(isinstance(term,list) and len(term) == 2
                            and type(term[0]) is int and isinstance(term[1],list)
                            and len(term[1]) == n
                            and all(type(power) is int and power >= 0 for power in term[1])
                            for term in atom["terms"]) for atom in constraints))


def polynomial(atom,variables):
    total = 0
    for coefficient,powers in atom["terms"]:
        term = coefficient
        for variable,power in zip(variables,powers):
            if power:
                term *= variable**power
        total += term
    return total


def relation(value,operator):
    if operator == "=":
        return value == 0
    if operator == "!=":
        return value != 0
    if operator == "<":
        return value < 0
    if operator == "<=":
        return value <= 0
    if operator == ">":
        return value > 0
    return value >= 0


def solve_source(source):
    if not legal_source(source):
        raise ValueError("Illegal polynomial conjunction")
    variables = [z3.Real(f"x_{i}") for i in range(source["variables"])]
    solver = z3.Solver()
    for atom in source["constraints"]:
        solver.add(relation(polynomial(atom,variables),atom["relation"]))
    result = solver.check()
    if result == z3.unsat:
        return {"status":"NO-SOLUTION"}
    if result != z3.sat:
        raise RuntimeError(f"Inconclusive real solver: {result}")
    model = solver.model()
    values = [model.eval(variable,model_completion=True) for variable in variables]
    if not all(z3.is_rational_value(value) for value in values):
        raise RuntimeError("Algebraic witness encoding pending for this source instance")
    output = {"values":[[value.numerator_as_long(),value.denominator_as_long()] for value in values]}
    assert direct_source(source,output)
    return output


def direct_source(source,output):
    if not isinstance(output,dict) or set(output) != {"values"}:
        return False
    values = output["values"]
    if (not isinstance(values,list) or len(values) != source["variables"]
            or any(not isinstance(value,list) or len(value) != 2
                   or any(type(part) is not int for part in value) or value[1] <= 0
                   for value in values)):
        return False
    rationals = [Fraction(*value) for value in values]
    return all(relation(polynomial(atom,rationals),atom["relation"])
               for atom in source["constraints"])


def valid_source(source,output):
    if not legal_source(source) or not isinstance(output,dict):
        return False
    if output == {"status":"NO-SOLUTION"}:
        return solve_source(source) == output
    return direct_source(source,output)


def self_test():
    from generate_cases import EDGE_CASES,random_source
    from test_oracle import test_hand_cases
    path = Path(__file__).with_name("cases.json")
    root = Path(__file__).resolve().parents[3]
    subprocess.run([sys.executable,str(root/"research/validate_preparation.py"),str(path)],check=True,cwd=root)
    cases = json.loads(path.read_text())
    for source,expected in EDGE_CASES:
        assert ("values" in solve_source(source)) == expected
    for case in cases:
        source = case["source"]
        if case["kind"] == "random":
            assert random_source(case["seed"]) == source
        answer = solve_source(source)
        assert ("values" in answer) == ("values" in case["expected"])
        assert valid_source(source,answer) and valid_source(source,case["expected"])
    test_hand_cases()
    print(f"Partial Prepare: {len(cases)} real-polynomial source cases checked; target oracle pending")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test",action="store_true")
    group.add_argument("--candidate",type=Path)
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        raise SystemExit("Prepare blocked: algebraic source witnesses and exact geometric-thickness target oracle pending")
