# User Story – Exercise 5: Gas Station Queue (M/M/1) Simulation

## Story
As an **operations manager**, I want to simulate customer arrivals and service at a single-pump gas station so that I can compute key queuing metrics: **average customers in system**, **server utilization**, and **average waiting time**.

## Acceptance Criteria
- Arrivals follow an exponential interarrival time with rate λ = 10 customers/hour.
- Service times follow an exponential distribution with mean 4 minutes (µ = 15 customers/hour).
- The simulation must consider several hundred customers (≥ 200 recommended).
- For each customer, the system must record:
  - arrival time,
  - service start time,
  - service end time,
  - time in queue,
  - total time in system.
- The system must generate a **CSV file** in the folder `output/problema5/` that:
  - Contains one row per customer.
  - Includes all relevant variables (arrival, start, end, queue time, system time, and any flags).
- The system must generate an **Excel file** in `output/problema5/` that:
  - Contains the same data table as the CSV.
  - Includes at least one embedded chart, for example:
    - time series of number of customers in the system,
    - histogram of waiting times.
- The system must compute and report:
  - average number of customers in the system,
  - server utilization (percentage of time busy),
  - average waiting time in the queue.

## Definition of Done
- Queue logic correctly enforces FIFO and correct handling of overlapping arrivals.
- Metrics are computed purely from the stored customer records.
- The folder `output/problema5/` exists and contains:
  - CSV with all simulation variables.
  - Excel workbook with data and embedded charts.
