# Skills Matrix

Each skill mapped to the specific work in this program that demonstrates it. Intended for screening against a job description: the middle column is the claim, the right column is the evidence.

## Industrial controls and PLC

| Skill | Level | Demonstrated by |
|---|---|---|
| PLC hardware and architecture | Working | Micro820 anatomy: CPU and scan cycle, program vs. data memory, embedded digital and analog I/O, expansion concept |
| Ladder-logic programming | Working | Wrote, downloaded and debugged programs using contacts, coils, AND/OR, latching, math blocks, comparison, counters and timers — [PLC Programs](03-plc-programming.md) |
| PLC software toolchain | Working | Connected Components Workbench: variable declaration, compile and error resolution, Ethernet download, online monitoring of live values |
| Digital I/O | Working | Mapped toggle switch inputs and pilot lamp outputs to `_IO_EM_DI_xx` / `_IO_EM_DO_xx` and verified state changes online |
| Analog I/O | Working | Potentiometer on an embedded analog input, clamped with `LIMIT` and compared against a setpoint, cross-checked against an analog panel meter |
| Counters and timers | Working | `CTU` with preset, accumulator and reset; `TON`/`TOF` for debounce, dwell and staged sequencing |
| Sequencing and continuous operation | Working | Seal-in/latching start-stop rung with fail-safe NC stop; chained timers for step sequencing |
| Live troubleshooting of logic | Working | Diagnosed contact-bounce miscounts, duplicated coils, download failures, and analog chatter at a threshold |

## Electrical

| Skill | Level | Demonstrated by |
|---|---|---|
| AC and DC wiring fundamentals | Working | Wire gauge selection, insulation types, plugs and cordsets, junction boxes, breakers, batteries, grounding — [Introductory Module](01-introductory-module.md) |
| Panel building | Working | Built AC and DC panels on the capstone: DIN rail, breakers, terminal blocks, 24 VDC supply, switches and pilot lamps — [Capstone](04-capstone-motor-test-stand.md) |
| Terminations and workmanship | Working | Stripping to gauge without nicking strands, ferrules on stranded conductors, pull-tested crimps, wire dress with service loops, strain relief in cord grips |
| Grounding and bonding | Working | Equipment grounding conductor from plug pin through enclosures to the frame, with continuity verified and paint-piercing hardware at lugs |
| Circuit protection | Working | Miniature circuit breakers sized to protect the conductor; fuse identification and correct-rating replacement |
| Electrical measurement | Working | DMM for AC/DC voltage, continuity and resistance; non-contact voltage tester; prove-dead-before-work routine |
| Commissioning | Working | Full cold-check sequence, staged energization, and functional verification of the capstone — documented procedure with results |
| Electrical troubleshooting | Working | Breaker, fuse, battery, switch and cordset diagnosis; segment isolation by continuity; find-the-cause-before-reset discipline |
| Motor circuits | Working | Single-phase AC motor wired through a branch breaker and local disconnect; start/run/stop behavior observed |
| Relays and contactors | Working | Low-voltage control signal switching a higher-power load; coil vs. contact and NO/NC identification |

## Mechanical

| Skill | Level | Demonstrated by |
|---|---|---|
| Hand tools | Working | Screwdrivers, shears, hammers, saws, wrenches, with correct tool-to-hardware matching |
| Power tools | Working | Drills, impact drivers, power saws — speed/feed by material, pilot holes, clamping, safe bit and blade changes |
| Precision measurement | Working | Dial and digital calipers, scales, tape, combination square, thread pitch gauges; zeroing and repeatability checks |
| Finishing | Working | Files and draw filing, progressive grit sanding, steel wool, abrasive pads, surface prep and painting; power grinding, sanding and buffing |
| Assembly from BOM and instructions | Working | Capstone frame and motor mount built from a written instruction set and verified BOM, then measured post-assembly |
| Alignment and squaring | Working | Diagonal comparison to square the T-slot frame, levelling on adjustable feet before mounting the motor |
| Fastening and torque | Working | Correct grade, pitch and length selection; cross-pattern torquing; extraction of damaged hardware |
| Mechanical troubleshooting | Working | Vibration, balance and alignment diagnosis; wrong-hardware, damage and corrosion identification |
| Maintenance and repair | Working | Damaged hardware removal, cleaning, lubrication, sanding and repainting, with re-verification after repair |

## Pneumatics

| Skill | Level | Demonstrated by |
|---|---|---|
| Air supply and conditioning | Working | FRL setup, regulator adjustment to working pressure against a gauge |
| Distribution and fittings | Working | Push-to-connect fittings, tees and elbows, squarely cut polyurethane tubing, ball-valve isolation with quick-connect coupler |
| Actuation and control | Working | Single- and double-acting cylinders, directional valves, flow control valves for stroke speed, pneumatic grippers |
| Safe practice | Working | Venting stored pressure before breaking connections, restraining tubing, blow gun handling |

## Sensors and actuators

| Skill | Level | Demonstrated by |
|---|---|---|
| Proximity sensing | Working | Inductive, magnetic/reed, optical (through-beam, diffuse, reflective) and ultrasonic sensors wired and range-set |
| Sensor-to-PLC integration | Working | Sourcing (PNP) vs. sinking (NPN) output identification, wiring to a PLC digital input, and confirming bit state online |
| Motion actuators | Working | AC induction motor, stepper and servo motors — position and speed commands, open-loop vs. closed-loop behavior |
| Test and troubleshoot | Working | Repeatable, chatter-free switch points; distinguishing a sensor fault from a wiring fault from a logic fault |

## Electronics and microcontrollers

| Skill | Level | Demonstrated by |
|---|---|---|
| Breadboard prototyping | Working | Multi-stage DIP IC circuit on a bench breadboard with dual supplies, switch input, meter and scope characterization |
| Microcontroller I/O | Familiar | Arduino Uno reading analog inputs and driving outputs on a 12 VDC supply |
| Component identification | Working | Resistors, capacitors, diodes, potentiometers, DIP ICs, and their markings |

## Process, safety, and documentation

| Skill | Level | Demonstrated by |
|---|---|---|
| Shop and electrical safety | Working | Tool-specific safety briefs, PPE, energy isolation, prove-dead-before-work, pressure venting |
| Reading technical documentation | Working | Working from assembly instructions, wiring drawings and datasheets rather than from example photos |
| BOM management | Working | Counting, sorting, labeling and verifying parts against the list before starting a build |
| Verification and test procedure | Working | Wrote and executed the cold-check, staged-energization and functional-verification sequence for the capstone |
| Technical writing | Working | This repository: procedures, I/O maps, rung documentation and troubleshooting tables |
| Structured fault finding | Working | Symptom → hypothesis → measurement → isolation → repair → re-verify, applied to seeded electrical and mechanical faults |

---

**Level key** — *Working:* performed independently on hardware with verified results. *Familiar:* performed with guidance and understand the principles.
