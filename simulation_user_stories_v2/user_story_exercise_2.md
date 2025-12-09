# User Story – Exercise 2: Metal Bar Welding Simulation

## Story
As a **quality engineer**, I want to simulate the welding of metal bars whose lengths follow Normal and Erlang distributions so that I can estimate the **percentage of bars exceeding the length specification**.

## Acceptance Criteria
- X1 ~ Normal(mean=30, variance=0.81).
- X2 ~ Erlang(k=2, mean=15).
- Total length = X1 + X2.
- Specification: length ≤ 50 cm.
- The simulation must run **300 trials** (300 welded bars).
- For each trial, the system must store:
  - X1, X2, total length, and whether it is in or out of specification.
- The system must generate a **CSV file** in the folder `output/problema2/` that:
  - Contains one row per simulated bar.
  - Includes all variables used (X1, X2, total length) and the classification (OK / out-of-spec).
- The system must generate an **Excel file** in `output/problema2/` that:
  - Contains the same data table as the CSV.
  - Includes at least one embedded chart, for example:
    - histogram of total length,
    - bar chart of in-spec vs. out-of-spec counts.
- The final output must include the empirical probability of non-conforming bars.

## Definition of Done
- Random generation of both distributions (Normal and Erlang) is validated and documented.
- Percentage of failures is correctly computed from the stored data.
- The folder `output/problema2/` exists and contains:
  - CSV with all simulation variables.
  - Excel workbook with data and embedded charts.
