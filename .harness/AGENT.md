# OpenHarness entry

Read `.harness/config.json`; run `openharness --repo . entry` and `doctor` for live
authority, legal work and current closure. Exit 2 means OPEN GAP, never success.
Canonical Backlog task files at the GitHub target ref are the sole work authority.
Use `workspace --task TASK_ID --change NAME` for a task-bound isolated Change;
PRs require exactly one `Work-Item: TASK_ID` line and the bound backlog branch.
Explicit configured assignee mapping authorizes the native executor/PR author.
Unassigned/ambiguous work, incomplete dependencies and stale corpus bindings reject.
Task metadata is not exclusive ownership or fencing; only the declared trusted
single-writer envelope is supported. Competing/unknown writers remain OPEN GAP.
Task corpus/control changes require exact native owner approval on the PR.
Trusted immutable baseline verification and independent publication preserve native
strict candidate/ref/check enforcement. Local verification never authorizes merge.
Use `integrate --pr N`, then `release`, or `handoff --reason TEXT` for continuity.
Reconcile invalidates drift without acquiring authority or automatically activating.
Break-glass invalidates guarantees and grants no remote bypass. Unsupported task
syntax and unavailable native proof remain OPEN GAP. Run current Doctor/activation;
saved reports and conversations are not activation authority.
