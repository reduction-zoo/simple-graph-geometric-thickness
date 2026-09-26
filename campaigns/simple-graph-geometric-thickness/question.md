# Existential theory of the reals → Geometric thickness of simple graphs

Category: Complexity open

## Source

The source asks whether a finite existential formula of polynomial equalities and inequalities over the reals is satisfiable, using binary integer coefficients. Recovery must respect the campaign’s finite algebraic witness representation; an unsatisfiable instance returns NO-SOLUTION.

## Target

Given a simple graph and layer budget k, find a straight-line drawing and an edge partition into at most k crossing-free layers, or report NO-SOLUTION. Coordinates require a finite real-algebraic encoding.

## Required result

Construct deterministic polynomial-time maps F and G: F sends every legal source instance to a legal target instance, and G(x,y) is a valid source output for every valid output y of F(x). Preserve the stated threshold, domain and promises. The requested complexity conclusion is ∃R-hardness for the stated target problem.

## Acceptance

Give explicit construction and recovery algorithms, a general proof for every legal input and every valid target output, and polynomial runtime and encoding-size bounds. Specify finite output encodings and handle NO-SOLUTION outputs when applicable. Tests compare recovered source outputs with independent source solutions.

## Why it matters

Real-algebraic hardness would explain geometric recognition difficulty beyond ordinary combinatorial NP-hardness.

## Difficulty

A simple graph must enforce geometric incidences without the parallel edges or extra geometric data used by other formulations.

## Literature context

Real-algebraic hardness in formulations using multigraphs or extra geometric information does not settle geometric thickness of simple graphs alone.

Literature checked 2026-09-15. This summarizes the archived literature search on the date above. Unpublished, unindexed and overlooked work remains outside coverage; no new novelty assessment was performed.

## References

- [Geometric Thickness of Multigraphs is ∃R-Complete](https://link.springer.com/article/10.1007/s00453-025-01351-7): - R9: Förster et al., Geometric Thickness of Multigraphs is ∃R-Complete, Algorithmica 88:3 (2026), Section 5, Questions 2–3; arXiv record. The journal PDF was downloaded and inspected. Parallel edges are essential to the result as stated.
- [arXiv record](https://arxiv.org/abs/2312.05010): - R9: Förster et al., Geometric Thickness of Multigraphs is ∃R-Complete, Algorithmica 88:3 (2026), Section 5, Questions 2–3; arXiv record. The journal PDF was downloaded and inspected. Parallel edges are essential to the result as stated.
- [Pathways to Tractability for Geometric Thickness](https://arxiv.org/abs/2411.15864): - 2026-09-15: Rechecked R9's journal Section 5, Question 2, p. 31, against "geometric thickness" "simple" "2026" complete and "geometric thickness" "simple graphs" completeness 2025 2026. Pathways to Tractability for Geometric Thickness, abstract and arXiv record, concerns structural parameters and partial-solution extension. Those results do not settle unrestricted simple-graph ∃R-hardness. No matching resolution located; full proofs of this follow-up were not audited. Gate 5 remains on hold; Gate 6 is not assessed for admission. Fourth priority in the current five: an explicit recent question, but narrower audience than the learning and matrix targets. No new experiment or campaign round.

Fixed from board record `website/questions/simple-graph-geometric-thickness.json` in board checkout at 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17; the record was copied from the current working tree.
