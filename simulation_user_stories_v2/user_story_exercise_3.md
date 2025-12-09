# User Story – Exercise 3: Two-Stage Process Simulation

## Story
As a **production planner**, I want to simulate a two-stage manufacturing process with Normal and Erlang processing times so that I can determine the **probability that total processing time exceeds 55 minutes**.

## Acceptance Criteria
- t1 ~ Normal(mean=30, variance=10).
- t2 ~ Erlang(k=3, mean=20).
- Total time per piece = t1 + t2.
- Threshold: 55 minutes.
- The simulation must run **1000 trials** (1000 pieces).
- For each trial, the system must store:
  - t1, t2, total time, and a flag indicating if it exceeds 55 minutes.
- The system must generate a **CSV file** in the folder `output/problema3/` that:
  - Contains one row per piece.
  - Includes all variables used (t1, t2, total time) and the over-threshold flag.
- The system must generate an **Excel file** in `output/problema3/` that:
  - Contains the same data table as the CSV.
  - Includes at least one embedded chart, for example:
    - histogram of total times,
    - line chart of running probability of exceeding 55 minutes.
- The final output must include the empirical probability of exceeding 55 minutes and any relevant descriptive statistics.

## Definition of Done
- Total time distribution is correctly computed from the underlying distributions.
- Probability estimation is derived directly from the simulated data.
- The folder `output/problema3/` exists and contains:
  - CSV with all simulation variables.
  - Excel workbook with data and embedded charts.
