# Coupled Harmonic Oscillator Simulation

A Python simulation of a two-mass coupled harmonic oscillator system that visualizes normal-mode decomposition and individual mass displacements over time.

## Physics Overview

The system models two masses connected by springs in the following arrangement:

```
Wall ──[k_outer]── Mass 1 ──[k_link]── Mass 2 ──[k_outer]── Wall
```

Each mass is anchored to a fixed wall via an outer spring (`k_outer`) and connected to the other mass via a coupling spring (`k_link`). The motion is fully described by two **normal modes**:

| Mode | Frequency Formula | Description |
|------|-------------------|-------------|
| Slow mode | `ω_slow = √(k_outer / m)` | Masses move in phase |
| Fast mode | `ω_fast = √((k_outer + 2·k_link) / m)` | Masses move out of phase |

The individual displacements are recovered from the normal-mode coordinates:

```
x1 = 0.5 * (q_fast + q_slow)
x2 = 0.5 * (q_slow - q_fast)
```

## Requirements

- Python 3.7+
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

## Usage

Run the simulation directly:

```bash
python oscillator.py
```

This will print the normal-mode frequencies to the console and open an interactive plot window.

## Parameters

All parameters are set at the top of `coupled_harmonic_oscillator()` and can be freely adjusted:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `mass` | `1.0` | Mass of each object (kg) |
| `k_outer` | `10.0` | Spring constant for wall-to-mass springs (N/m) |
| `k_link` | `2.0` | Spring constant for the coupling spring (N/m) |
| `A_fast` | `1.0` | Initial amplitude of the fast normal mode |
| `A_slow` | `1.0` | Initial amplitude of the slow normal mode |
| `phi_fast` | `0.0` | Initial phase of the fast normal mode (rad) |
| `phi_slow` | `0.0` | Initial phase of the slow normal mode (rad) |

## Output

The simulation produces a two-panel figure:

**Top panel — Mass Displacements:** Time-series displacement of Mass 1 and Mass 2, showing the beating pattern that emerges when both normal modes are active simultaneously.

**Bottom panel — Normal Modes:** The underlying fast and slow mode oscillations whose superposition produces the motion shown above.

Console output example:
```
Fast mode: 3.742 rad/s
Slow mode: 3.162 rad/s
```

## Example: Observing Beating

To see a clear beating pattern, set `k_link` to a small value relative to `k_outer` (e.g., `k_link = 0.5`). The two normal-mode frequencies will be close together, causing the amplitude of each mass to oscillate slowly — the hallmark of coupled-oscillator energy exchange.

## File Structure

```
.
└── oscillator.py   # Main simulation script
```
