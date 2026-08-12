# Photos

Project photographs referenced from the [main README](../README.md) and the documents in [`docs/`](../docs).

**The `.jpg` files currently in this folder are generated placeholders**, so the gallery lays out correctly before the real photographs land. Replace each one with the actual photo using the **exact same filename** and every reference across the repository picks it up with no edits. Filenames are lowercase with hyphens and a `.jpg` extension; if a photo is a `.jpeg`, `.png` or `.heic`, convert or rename it to `.jpg`.

The placeholders come from [`tools/make_photo_placeholders.py`](../tools/make_photo_placeholders.py) and can be regenerated with `python3 tools/make_photo_placeholders.py` (requires Pillow). Once all the real photos are in place the script and this note can be deleted.

## Filename map

### Capstone: motor test stand

| Filename | What the photo shows |
|---|---|
| `test-stand-front-assembly.jpg` | The completed stand from the front: AC motor on the deck, motor disconnect box, and both clear-cover enclosures with yellow liquid-tight cordsets |
| `test-stand-frame-motor-mount.jpg` | The T-slot extrusion frame with leveling feet and the motor bolted to the deck (open-frame view) |
| `test-stand-ac-enclosure-breaker.jpg` | AC enclosure interior: DIN-rail miniature circuit breaker, terminal blocks, and line/neutral/ground conductors |
| `test-stand-24vdc-power-supply.jpg` | Enclosure interior with the Mean Well MDR-60-24 DIN-rail 24 VDC power supply beside its branch breaker |
| `test-stand-dc-panel-lamps.jpg` | The DC operator panel: three toggle switches with red, amber and green indicator lamps |
| `test-stand-dc-panel-rear.jpg` | Rear of the stand: red (+24 V) and black (0 V) push-in DIN-rail terminal blocks feeding the control panel |

### PLC / Connected Components Workbench

| Filename | What the photo shows |
|---|---|
| `plc-trainer-and-logic.jpg` | The Micro820 trainer next to a CCW ladder program with a direct rung and a series-contact (AND) rung |
| `plc-adder-function-block.jpg` | CCW rung with the `ADD` function block: A = 100.0, B = 200.0, X = 300.0 |
| `plc-counter-timer-download.jpg` | CCW with the `CTU` counter and `LIMIT` block, the output pane reporting a successful download, and lamps lit on the trainer |
| `plc-local-variables-table.jpg` | The CCW Local Variables table: name, alias, data type, initial value, retentive |

### Bench labs

| Filename | What the photo shows |
|---|---|
| `breadboard-analog-circuit.jpg` | Bench breadboard with two 8-pin DIP ICs, resistors, a toggle switch, powered from the Va/Vb supplies |
| `arduino-breadboard-circuit.jpg` | Arduino Uno on a baseplate wired to a breadboard circuit with potentiometers, capacitors and a diode |
| `pneumatics-frl-blowgun.jpg` | Pneumatic circuit: FRL with pressure gauge, ball valve with quick-connect coupler, push-to-connect tubing with a tee, and a blow gun |
| `electronics-component-kit.jpg` | Organized component and jumper-wire kit used for the electronics labs |

## Tips

- Keep the long edge around 1600–2000 px so the repository stays small; GitHub scales images down in the README anyway.
- Crop out anything that identifies other people in the frame.
- Machine or asset labels visible in a photo (such as a workstation ID) are worth cropping out too.
