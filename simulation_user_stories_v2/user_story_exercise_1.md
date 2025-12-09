# User Story – Exercise 1: Fast-Food Restaurant Simulation

## Story
As a **restaurant operations analyst**, I want to simulate hourly hamburger sales based on probabilistic demand so that I can estimate the **expected utility per hour** and understand profitability.

## Acceptance Criteria
- Demand per hour must be generated using the discrete probability distribution:
  - 0–6 hamburgers with their given probabilities.
- For each simulated hour, the system must compute:
  - Hourly revenue (price × sold units).
  - Hourly cost (cost × sold units).
  - Hourly utility (revenue − cost).
- The simulation must run for **100 hours**.
- The system must generate a **CSV file** in the folder `output/problema1/` that:
  - Contains one row per simulated hour.
  - Includes all variables used and derived (demand, revenue, cost, utility, and any parameters).
- The system must generate an **Excel file** in `output/problema1/` that:
  - Contains the same data table as the CSV.
  - Includes at least one embedded chart (e.g., utility vs. hour or distribution of utility) inside the workbook.
- Optional: Include additional charts (e.g., histogram of utility) as extra sheets.

## Definition of Done
- Simulation produces consistent and reproducible results given the same random seed (if applicable).
- Calculations adhere exactly to the specified probability distribution and pricing structure.
- The folder `output/problema1/` exists and contains at least:
  - One CSV file with all simulation variables.
  - One Excel file with data and embedded charts.
