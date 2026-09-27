# Research instructions

Read the [fixed question](campaigns/simple-graph-geometric-thickness/question.md), [prior state](campaigns/simple-graph-geometric-thickness/state.md) and [preparation notes](campaigns/simple-graph-geometric-thickness/work/preparation.md). The fixed [test corpus](campaigns/simple-graph-geometric-thickness/work/cases.json) and [verifier](campaigns/simple-graph-geometric-thickness/work/check.py) are the starting evidence; the preparation notes state their coverage and any pending checks.

Run `uv sync --locked`, then `uv run --locked python campaigns/simple-graph-geometric-thickness/work/check.py --self-test` before relying on that evidence. Follow the current user's AutoResearch pipeline. Preserve prior evidence, commit new work incrementally and make only evidence-backed claims.
