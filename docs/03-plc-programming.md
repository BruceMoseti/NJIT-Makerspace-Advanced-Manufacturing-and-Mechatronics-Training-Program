# PLC Programs — Allen-Bradley Micro820 / Connected Components Workbench

Every ladder-logic program I wrote during the program, with the rung structure, the I/O mapping, and what I observed when it ran on hardware.

**Platform**

| | |
|---|---|
| Controller | Allen-Bradley Micro820 |
| Software | Connected Components Workbench (CCW) Standard Edition |
| Connection | Ethernet, online in Connected mode for live monitoring |
| Language | Ladder Diagram (LD) |
| Trainer | PLC trainer unit with 4 toggle switch inputs, 4 indicator lamps (blue, green, amber, red), a potentiometer, and an analog panel meter |

---

## I/O and variable conventions

Embedded I/O on the Micro820 is addressed as:

| Tag pattern | Meaning |
|---|---|
| `_IO_EM_DI_xx` | Embedded **digital input** — the trainer toggle switches |
| `_IO_EM_DO_xx` | Embedded **digital output** — the trainer indicator lamps |
| `_IO_EM_AI_xx` | Embedded **analog input** — the trainer potentiometer |

Before writing any logic I declare working variables in the **Local Variables** table: name, alias, data type, initial value, and the retentive flag for anything that must survive a power cycle. Rungs then reference the alias, so the program is readable rather than a wall of raw addresses.

![CCW Local Variables table](../images/plc-local-variables-table.jpg)

**Data types used:** `BOOL` for discrete state, `INT`/`DINT` for counts and integer math, `REAL` for analog and floating-point math, `TIME` for timer presets.

---

## Program 1 — Direct output and series logic (AND)

The first working program: prove the toolchain end-to-end, then prove that contact arrangement determines logic.

**Rung 1 — direct control.** One toggle switch drives one lamp. Closing the input energizes the coil.

```
        _IO_EM_DI_01                                    _IO_EM_DO_00
  ---------] [-------------------------------------------(  )--------
```

**Rung 2 — series contacts = AND.** Three inputs in series: the lamp only lights when *all three* toggles are closed.

```
     _IO_EM_DI_01   _IO_EM_DI_02   _IO_EM_DI_03          _IO_EM_DO_01
  --------] [-----------] [-----------] [------------------(  )-------
```

**Observed:** flipping any single toggle on rung 2 does nothing; the lamp lights only on the last of the three. Downloaded to the controller with `1 succeeded, 0 failed, 0 up-to-date, 0 skipped, 0 error(s)` in the output pane.

![Micro820 trainer with the basic ladder program](../images/plc-trainer-and-logic.jpg)

### The OR variant

Parallel branches in the same rung give OR — any one closed input energizes the coil:

```
     _IO_EM_DI_01                                        _IO_EM_DO_02
  --------] [-------+--------------------------------------(  )-------
                    |
     _IO_EM_DI_02   |
  --------] [-------+
                    |
     _IO_EM_DI_03   |
  --------] [-------+
```

Combining the two — series groups in parallel branches — is how any boolean expression gets built in ladder. Adding a normally-closed contact inverts a condition, which is how a stop input is wired (fail-safe: NC contact, so a broken wire stops the machine).

---

## Program 2 — Latching and continuous operation (motor start/stop)

The seal-in pattern, which is the single most useful rung in industrial control. A momentary start input begins continuous operation; a normally-closed stop input drops it out.

```
        Start_PB        Stop_PB                            Motor_Run
  ---------] [------------]/[----------+---------------------(  )-------
                                       |
        Motor_Run                      |
  ---------] [--------------------------+
```

The `Motor_Run` contact in the parallel branch holds the rung true after the momentary start input opens. Breaking the normally-closed `Stop_PB` contact interrupts the whole rung, and the seal-in cannot re-establish itself until start is pressed again.

**Observed:** the lamp latches on from a momentary toggle and stays on, and drops out on stop and stays off. Verified that the stop input takes priority regardless of the start input's state.

---

## Program 3 — Math function blocks (`ADD`)

Function blocks in ladder use `EN`/`ENO` enable gating: the block executes when `EN` is true and passes `ENO` on to whatever follows, so a math operation can be conditional on rung logic.

```
                     +-----------+
                     |    ADD    |
     EN ------------ EN        ENO ------------
        A (REAL) --- i1         o1 --- X (REAL)
        B (REAL) --- i2
                     +-----------+
```

| Variable | Type | Value |
|---|---|---|
| `A` | REAL | 100.0 |
| `B` | REAL | 200.0 |
| `X` | REAL | **300.0** (computed) |

**Observed live in the CCW monitor:** with `A = 100.0` and `B = 200.0`, the output variable `X` reads `300.0`, confirming both that the block executes and that the `REAL` data type carries the decimal correctly.

![ADD function block with A=100.0, B=200.0, X=300.0](../images/plc-adder-function-block.jpg)

The same enable-gated block pattern applies to `SUB`, `MUL`, `DIV` and to comparison blocks (`GT`, `LT`, `EQ`, `GE`, `LE`) used against a setpoint. A common trap: a math block left permanently enabled recalculates every scan, so anything order-dependent has to be gated by rung logic rather than left unconditional.

---

## Program 4 — Count-up counter (`CTU`) with output and reset

Counts input events, and turns on an output when the count reaches a preset. This is the pattern behind batch counting, cycle counting, and part-present tallies on a conveyor.

```
     _IO_EM_DI_00        +-------------+
  --------] [----------- CU    CTU_1  Q ------------------(  )--------
                         |     CTU     |              _IO_EM_DO_01
        Reset_PB   ----- RESET      CV ----- Count_ACC
                         |             |
        Preset     ----- PV            |
                         +-------------+
```

| Terminal | Role |
|---|---|
| `CU` | Count-up input — increments on each **rising edge**, not on the level |
| `RESET` | Clears the accumulated value back to zero |
| `PV` | Preset value — the target count |
| `Q` | Done bit — true once accumulated value reaches the preset |
| `CV` | Current/accumulated count, monitored live |

**Observed:** each toggle of the input increments the accumulated value by exactly one; `Q` goes true at the preset and drives the output lamp; asserting `RESET` returns the accumulator to `0` and drops `Q`. The output pane confirmed `Download: 1 succeeded, 0 failed` and the corresponding lamps lit on the trainer, with the live values showing `True`/`False` and the accumulator value inline on the rung.

**Edge vs. level** is the thing to get right: `CU` counts transitions. A held-closed input counts once, not continuously, which is why a debounced or one-shot input matters for a real sensor.

![CTU counter and LIMIT block running, download succeeded](../images/plc-counter-timer-download.jpg)

---

## Program 5 — Range clamping (`LIMIT`) on an analog input

`LIMIT` clamps a value between a minimum and a maximum, which is how a raw analog reading gets constrained to a usable band before being acted on.

```
                     +-----------+
                     |   LIMIT   |
     EN ------------ EN        ENO ------------------------(  )--------
        MN --------- i1         o1 --- Clamped         _IO_EM_DO_02
        IN --------- i2
        MX --------- i3
                     +-----------+
```

Fed from the trainer's potentiometer on an embedded analog input, with the analog panel meter as an independent reference. Turning the pot sweeps the raw value; the clamped output tracks it inside the band and holds flat at `MN` or `MX` outside it. Combined with a comparison block, this is a working analog setpoint: read the analog input, clamp it to a sane range, compare it to a threshold, and drive an output — a low-level / high-level alarm.

---

## Program 6 — Timers (on-delay and off-delay)

| Block | Behavior | Used for |
|---|---|---|
| `TON` (on-delay) | Output goes true after the input has been continuously true for the preset time | Debouncing a noisy sensor, staged startup, ignoring transient conditions |
| `TOF` (off-delay) | Output stays true for the preset time after the input goes false | Dwell, run-on / cool-down after a stop, holding an indicator visible |

```
        Start_Cond          +-----------+
  ---------] [------------- IN   TON_1  Q -------------------(  )------
                            |    TON    |                 Output
        T#3s ------------ PT        ET ----- Elapsed
                            +-----------+
```

**Observed:** the output energizes exactly one preset period after the input goes true, and the elapsed-time value counts up live in the monitor. Releasing the input before the preset expires resets the elapsed time and the output never energizes — the input must be *continuously* true.

Chaining a `TON` off the done bit of the previous one gives a simple step sequencer, which is how the event-sequencing exercise in Week 13 was built: each stage arms the next after its dwell time.

---

## Working method

The routine I follow for every program, which is as much of the skill as the logic itself:

1. **Write the I/O map first** — every physical device to its tag, before opening the editor.
2. **Declare variables** in the Local Variables table with the right data type and initial value; set the retentive flag on anything that must survive a power cycle.
3. **Build the ladder** in small increments — one rung, verified, before the next.
4. **Compile and read the error list.** Fix the first error, then recompile; later errors are often cascades from the first.
5. **Download** and confirm `1 succeeded, 0 failed` in the output pane. A failed download is usually a controller-mode or connection-path problem, not a program problem.
6. **Go online and monitor live values.** Watching the `True`/`False` and numeric values annotated on the rungs is what actually proves the logic, rather than assuming from the code.
7. **Exercise every path**, including the ones that should do nothing, and confirm the failure modes behave safely.

## Troubleshooting notes worth keeping

- **Output won't energize but the logic looks true** — check the controller is in Run mode and that the output isn't forced or overwritten by a later rung driving the same coil. Last rung wins within a scan.
- **Counter increments by more than one per press** — contact bounce. Debounce with a short `TON` or condition on a one-shot.
- **Analog value jitters** — expected on a raw input; clamp with `LIMIT` and/or average, and add hysteresis so the comparison output doesn't chatter at the threshold.
- **Download fails** — verify the connection path and that the target matches the project's controller, then retry with the controller in Program mode.
- **Logic works on one trainer but not another** — the I/O map is per-machine. Re-verify which physical toggle is wired to which `_IO_EM_DI_xx`.
