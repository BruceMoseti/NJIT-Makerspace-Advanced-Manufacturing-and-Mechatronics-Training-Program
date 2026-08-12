# Photos

Project photographs referenced from the [main README](../README.md) and the documents in [`docs/`](../docs). All of them were taken during the program and show my own work.

They were prepared with [`tools/prepare_photos.py`](../tools/prepare_photos.py), which rotates each frame upright, crops it onto its subject, resizes the long edge to 1500 px, strips camera metadata, and writes it here under the filename the documents reference.

## Index

### Capstone: motor test stand

| Filename | What the photo shows | Used in |
|---|---|---|
| `test-stand-front-assembly.jpg` | The completed stand from the front: AC motor on the deck, local disconnect box, and both clear-cover enclosures fed by yellow liquid-tight cordsets | README (lead image), capstone |
| `test-stand-frame-motor-mount.jpg` | The T-slot extrusion frame with leveling feet and the motor bolted to the deck, open-frame view | README, advanced module, capstone |
| `test-stand-ac-enclosure-breaker.jpg` | AC enclosure interior: DIN-rail Eaton miniature circuit breaker, terminal blocks, and line/neutral/ground conductors | README, advanced module, capstone |
| `test-stand-24vdc-power-supply.jpg` | Enclosure interior with the Mean Well MDR-60-24 DIN-rail 24 VDC power supply beside its branch breaker | README, advanced module, capstone |
| `test-stand-dc-panel-rear.jpg` | Rear of the stand: red (+24 V) and black (0 V) push-in terminal blocks feeding the operator sub-panel, **lamps unlit** | README, capstone |
| `test-stand-dc-panel-lamps.jpg` | The same operator panel **energized**, red, amber and green pilot lamps lit | README, capstone |

The last two are a deliberate pair: the same panel wired and cold-checked, then energized. Read together they show the commissioning sequence rather than just a finished object.

### PLC / Connected Components Workbench

| Filename | What the photo shows | Used in |
|---|---|---|
| `plc-local-variables-table.jpg` | The Micro820 trainer on the bench beside the CCW Local Variables table: name, alias, data type, initial value, retentive | README, introductory module, PLC programs |
| `plc-adder-function-block.jpg` | CCW rung with the `ADD` function block monitored online: A = 100.0, B = 200.0, X = 300.0 | README, PLC programs |
| `plc-counter-timer-download.jpg` | CCW with the `CTU` counter and `LIMIT` block, the output pane reporting a successful download, and lamps lit on the trainer | README, advanced module, PLC programs |

### Bench labs

| Filename | What the photo shows | Used in |
|---|---|---|
| `pressure-transducer-signal-conditioning.jpg` | A 0–500 PSIG pressure transducer cabled into a breadboard signal-conditioning circuit built around two DIP ICs | README, introductory module |
| `breadboard-analog-circuit.jpg` | Bench breadboard with two 8-pin DIP ICs, resistors and a toggle switch, powered from the Va/Vb supplies | README, advanced module |
| `arduino-breadboard-circuit.jpg` | Arduino Uno on a baseplate wired to a breadboard circuit with potentiometers, capacitors and a diode | README, advanced module |
| `electronics-component-kit.jpg` | Organized component and jumper-wire kit staged for the electronics labs | Advanced module |

## Adding or replacing a photo

Filenames are lowercase with hyphens and a `.jpg` extension. Overwriting a file with a new photograph under the same filename updates every reference across the repository with no edits.

To re-run the preparation script on the source PDF:

```bash
pip install pymupdf pillow
python3 tools/prepare_photos.py path/to/source.pdf
```

Guidelines worth keeping if you add more:

- Long edge around 1500–2000 px, so the repository stays small. GitHub scales images down for display anyway.
- Crop in on the subject. A tight frame on the work reads far better than a wide shot of a bench.
- Crop out anything that identifies other people, and any workstation or asset ID labels.
- Write a descriptive `alt` text for each new image so the documents stay accessible.
