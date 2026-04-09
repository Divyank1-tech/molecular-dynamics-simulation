# 3D Molecular Dynamics Simulation

An interactive 3D particle simulation implementing the Lennard-Jones potential with Velocity Verlet integration and periodic boundary conditions — all rendered in real time using Matplotlib.

## Physics Overview

### Lennard-Jones Potential

Particle interactions are governed by the Lennard-Jones (LJ) pair potential:

```
V(r) = 4ε [ (σ/r)¹² − (σ/r)⁶ ]
```

| Term | Role |
|------|------|
| `(σ/r)¹²` | Short-range repulsion (Pauli exclusion) |
| `(σ/r)⁶` | Long-range attraction (van der Waals) |

The force on particle `i` from all neighbours is derived from `F = −∇V`:

```
F(r) = 24ε/r² [ 2(σ/r)¹² − (σ/r)⁶ ] · r̂
```

A **cutoff radius** (`r_cut = 3σ`) truncates interactions beyond a set distance for performance.

### Integration: Velocity Verlet

Each timestep advances the system using the Velocity Verlet algorithm, which conserves energy better than simple Euler integration:

```
v(t + dt/2) = v(t) + F(t)/m · dt/2
x(t + dt)   = x(t) + v(t + dt/2) · dt
F(t + dt)   = compute_forces(x(t + dt))
v(t + dt)   = v(t + dt/2) + F(t + dt)/m · dt/2
```

### Periodic Boundary Conditions (PBC)

Particles that exit one face of the simulation box re-enter from the opposite face (`positions %= L`). The minimum image convention is applied during force calculations to ensure each particle only interacts with the nearest image of every other particle.

### Temperature

Instantaneous temperature is estimated from the kinetic energy per particle:

```
T ≈ KE / N    where KE = ½ Σ m·v²
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

```bash
python md_simulation.py
```

A 3D animated window will open immediately. The simulation runs for 500 frames and rotates the camera automatically for a better view of the particle dynamics.

## Interactive Controls

| Control | Description |
|---------|-------------|
| **Particles slider** | Drag to set N between 10 and 100. The system reinitialises instantly with the new particle count. |
| **Mouse drag** | Rotate the 3D view manually at any time. |

## Parameters

Adjust these constants at the top of the script:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `L` | `10.0` | Box side length (simulation units) |
| `dt` | `0.01` | Timestep size |
| `epsilon` | `1.0` | LJ energy well depth (ε) |
| `sigma` | `1.0` | LJ length scale / particle diameter (σ) |
| `mass` | `1.0` | Particle mass |
| `cutoff` | `3.0` | Force cutoff radius (in units of σ) |
| `N` | `40` | Initial particle count |

> **Performance tip:** Keep `N` below ~60 for smooth animation. The force calculation is O(N²) per frame; larger `N` will noticeably slow the update rate.

## Output

The animation window displays:

- **3D scatter plot** of all particles inside the periodic box
- **Slow camera rotation** (0.5°/frame) for a dynamic view
- **Title bar** updates every 5 frames showing current `N` and instantaneous temperature

## File Structure

```
.
└── md_simulation.py   # Main simulation script
```

## Known Limitations

- Force computation is pure Python/NumPy loops — not optimised for large N. For production MD, consider libraries such as LAMMPS, OpenMM, or a neighbour-list implementation.
- Only kinetic energy is tracked; potential energy and total energy conservation are not plotted.
- The LJ potential is not shifted at the cutoff, which introduces a small discontinuity in energy at `r = r_cut`.
