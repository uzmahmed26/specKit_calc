---
description: "Task list for the Basic Calculator feature implementation"
---

# Tasks: Basic Calculator

**Input**: Design documents from `/specs/001-basic-calculator/`
**Prerequisites**: plan.md, spec.md, data-model.md, quickstart.md

**Tests**: Following a TDD approach as requested.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Run `uv init` to initialize the Python project and create `pyproject.toml`.
- [x] T002 Create source directory `src/calculator/`.
- [x] T003 Create test directory `tests/unit/`.
- [x] T004 Create empty file `src/calculator/__init__.py`.
- [x] T005 Create empty file `src/calculator/main.py`.
- [x] T006 Create empty file `src/calculator/exceptions.py`.
- [x] T007 Create empty file `tests/unit/test_calculator.py`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T008 [P] Define custom exception classes `CalculatorError`, `InvalidExpressionError`, `DivisionByZeroError` in `src/calculator/exceptions.py`.
- [x] T009 [P] Add basic imports and test class structure to `tests/unit/test_calculator.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: A user can perform addition, subtraction, multiplication, and division.

**Independent Test**: The `calculate` function can be called with simple expressions like "2 + 2" and "10 / 2" and return the correct result.

### Tests for User Story 1 (TDD) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [US1] Write failing unit tests for addition, subtraction, multiplication, and division in `tests/unit/test_calculator.py`.

### Implementation for User Story 1

- [x] T011 [US1] Implement the `calculate` function in `src/calculator/main.py` to handle basic arithmetic, making the tests from T010 pass.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Advanced Operations (Priority: P2)

**Goal**: A user can perform exponentiation and square root operations.

**Independent Test**: The `calculate` function can be called with expressions like "2 ** 3" and "sqrt(9)" and return the correct result.

### Tests for User Story 2 (TDD) ⚠️

- [x] T012 [US2] Write failing unit tests for exponentiation and square root in `tests/unit/test_calculator.py`.

### Implementation for User Story 2

- [x] T013 [US2] Extend the `calculate` function in `src/calculator/main.py` to handle exponentiation and square root, making the tests from T012 pass.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Order of Operations (Priority: P3)

**Goal**: A user can use parentheses to group expressions and control the order of operations.

**Independent Test**: The `calculate` function can be called with expressions like "5 * (3 + 2)" and return the correct result.

### Tests for User Story 3 (TDD) ⚠️

- [x] T014 [US3] Write failing unit tests for expressions with parentheses in `tests/unit/test_calculator.py`.

### Implementation for User Story 3

- [x] T015 [US3] Ensure the `ast` parser in `src/calculator/main.py` correctly handles order of operations, making the tests from T014 pass.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: User Story 4 - Mathematical Constants (Priority: P4)

**Goal**: A user can use the constants `pi` and `e` in calculations.

**Independent Test**: The `calculate` function can be called with expressions like "pi * 2" and return the correct result.

### Tests for User Story 4 (TDD) ⚠️

- [x] T016 [US4] Write failing unit tests for expressions with `pi` and `e` in `tests/unit/test_calculator.py`.

### Implementation for User Story 4

- [x] T017 [US4] Extend the `calculate` function in `src/calculator/main.py` to recognize and use the constants `pi` and `e`, making the tests from T016 pass.

---

## Phase 7: Edge Cases & Error Handling

**Purpose**: Ensure the library is robust and handles invalid input gracefully.

### Tests for Edge Cases (TDD) ⚠️

- [x] T018 Write failing unit tests in `tests/unit/test_calculator.py` for:
    - Division by zero
    - Invalid expressions (e.g., "5 * + 3")
    - Non-numeric input
    - Empty/whitespace input
    - Expressions without required spaces (e.g., "5+3")

### Implementation for Edge Cases

- [x] T019 Implement validation and error handling in `src/calculator/main.py` to raise the correct custom exceptions, making the tests from T018 pass.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [x] T020 [P] Add comprehensive docstrings to all functions and classes in `src/calculator/`.
- [x] T021 [P] Run a linter (e.g., `ruff`) and formatter (e.g., `black`) over the entire `src/` and `tests/` directories.
- [x] T022 Run `quickstart.md` validation to ensure examples are correct.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup.
- **User Stories (Phases 3-6)**: Depend on Foundational.
- **Edge Cases (Phase 7)**: Depends on all User Stories.
- **Polish (Phase 8)**: Depends on all other phases.

### User Story Dependencies

- All user stories are independent and can be implemented in any order after the Foundational phase, but following the priority order is recommended.

### Within Each User Story

- Tests MUST be written and FAIL before implementation.

### Parallel Opportunities

- **T008** and **T009** can be done in parallel.
- Once the Foundational phase is complete, different developers could work on different user stories in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently.

### Incremental Delivery

1. Complete Setup + Foundational.
2. Add User Story 1 → Test → MVP is ready.
3. Add User Story 2 → Test.
4. Add User Story 3 → Test.
5. Add User Story 4 → Test.
6. Add Edge Case handling → Test.
7. Polish.