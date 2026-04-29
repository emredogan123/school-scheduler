# 📘 Problem Approach

## 1. Problem Definition

The problem is defined as generating a valid school timetable by assigning courses to available time slots while satisfying multiple real-world constraints.

Each course must be scheduled for a fixed number of weekly hours, and assignments must ensure that:

* Teachers are only scheduled when they are available
* Class groups do not have overlapping lessons
* Classrooms are not double-booked

This problem can be categorized as a **constraint satisfaction problem (CSP)**.

---

## 2. Assumptions

To simplify the problem and ensure a feasible implementation, the following assumptions were made:

* Each course is assigned to exactly one teacher
* Each class group attends only one lesson at a time
* All time slots are of equal duration
* Classroom capacity is sufficient and not considered
* Teacher availability is predefined and static
* Courses do not require specialized equipment or room types

---

## 3. Constraints Considered

The system enforces the following constraints:

### Hard Constraints (must be satisfied)

* A teacher cannot teach more than one class at the same time
* A class group cannot attend multiple courses simultaneously
* A classroom cannot host more than one course at the same time
* A course must be scheduled for its required weekly hours

### Constraints Not Considered

* Teacher preferences (e.g., morning vs afternoon)
* Classroom capacity or specialization (e.g., labs)
* Consecutive lesson optimization (e.g., avoiding gaps)
* Priority levels between courses

---

## 4. Alternative Approaches Considered

Several alternative approaches were evaluated:

* **Brute-force search:** Guarantees correctness but is computationally expensive
* **Backtracking algorithms:** More optimal but increases implementation complexity
* **Genetic algorithms:** Suitable for optimization but requires tuning and is harder to debug
* **Linear programming / optimization models:** Powerful but overkill for the current scope

---

## 5. Chosen Approach and Justification

A **greedy constraint-based scheduling approach** was selected.

### Reasoning:

* Simple and fast to implement
* Easy to debug and extend
* Provides acceptable results for small to medium datasets
* Prioritizes courses with fewer available time slots (reducing conflicts early)

Although it does not guarantee a globally optimal solution, it offers a practical balance between performance, simplicity, and correctness.

---

## 6. Limitations

* May produce suboptimal schedules in complex scenarios
* Does not minimize gaps between lessons
* Conflict resolution is basic and not iterative


