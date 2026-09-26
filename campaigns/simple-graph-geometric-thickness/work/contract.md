# Partial contract

The current source corpus uses a conjunction of polynomial comparisons, encoded as `{"variables":n,"constraints":[{"terms":[[integer_coefficient,[nonnegative_exponents,...]],...],"relation":op},...]}`. Relations are `=`, `!=`, `<`, `<=`, `>` and `>=` against zero. Covered positive outputs are rational vectors `{"values":[[numerator,positive_denominator],...]}`. `NO-SOLUTION` is accepted only after conclusive Z3 `unsat`. This is a finite test subdomain of the fixed existential-real source problem. The full source witness contract must also encode real algebraic values; a positive irrational case raises an explicit blocker.

The target is a simple graph with an integer layer budget and asks for a straight-line vertex drawing plus a partition of the edges into crossing-free layers. Coordinates need a finite real-algebraic encoding. A conclusive target NO oracle and full output validator remain to be fixed. `check.py --candidate` exits with the blocker.
