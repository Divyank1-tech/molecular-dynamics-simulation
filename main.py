import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

L = 10.0
dt = 0.01
epsilon = 1.0
sigma = 1.0
mass = 1.0
cutoff = 3.0

N = 40  

def initialize_system(N):
    positions = np.random.rand(N, 3) * L
    velocities = np.random.randn(N, 3)
    velocities -= np.mean(velocities, axis=0)
    return positions, velocities

positions, velocities = initialize_system(N)

def compute_forces(pos):
    N = len(pos)
    forces = np.zeros_like(pos)

    for i in range(N):
        r_vec = pos[i] - pos
        r_vec -= L * np.round(r_vec / L)

        r = np.linalg.norm(r_vec, axis=1)
        mask = (r < cutoff) & (r > 0)

        r_valid = r[mask]
        r_vec_valid = r_vec[mask]

        if len(r_valid) > 0:
            f_mag = 24 * epsilon * (2*(sigma/r_valid)**12 - (sigma/r_valid)**6) / r_valid**2
            forces[i] += np.sum((f_mag[:, None] * r_vec_valid), axis=0)

    return forces

def compute_energy(pos, vel):
    KE = 0.5 * mass * np.sum(vel**2)
    return KE

forces = compute_forces(positions)

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')

scat = ax.scatter(positions[:,0], positions[:,1], positions[:,2], s=20)

ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)

ax.set_title("3D Molecular Dynamics")

ax_slider = plt.axes([0.2, 0.02, 0.6, 0.03])
slider = Slider(ax_slider, 'Particles', 10, 100, valinit=N, valstep=1)

def update_particles(val):
    global positions, velocities, forces
    N_new = int(slider.val)
    positions, velocities = initialize_system(N_new)
    forces = compute_forces(positions)

slider.on_changed(update_particles)

def update(frame):
    global positions, velocities, forces

    velocities += 0.5 * forces / mass * dt
    positions += velocities * dt
    positions %= L

    new_forces = compute_forces(positions)
    velocities += 0.5 * new_forces / mass * dt
    forces = new_forces
  
    scat._offsets3d = (positions[:,0], positions[:,1], positions[:,2])
  
    ax.view_init(elev=30, azim=frame * 0.5)
  
    if frame % 5 == 0:
        KE = compute_energy(positions, velocities)
        temp = KE / len(positions)
        ax.set_title(f"3D MD | N={len(positions)} | Temp={temp:.2f}")

    return scat,

ani = FuncAnimation(fig, update, frames=500, interval=30)

plt.show()
