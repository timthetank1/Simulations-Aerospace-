import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
g=9.81
deg_angle= int(input("Launch Angle: "))
angle=(deg_angle/360)*(2*np.pi)
constv0= int(input("launch velocity: "))
v0h=np.cos(angle)*constv0
v0y=np.sin(angle)*constv0
v0=np.linspace(10,30,5) 
vv0y=np.sin(angle)*v0
tlim=(2*v0y)/g
t=np.linspace(0,tlim,100)
distance=v0h*t
h=v0y*t-(0.5*g*(t**2))
maxh=(v0y**2)/(2*g)



fig, ax = plt.subplots()
line2, = ax.plot(distance[0], h[0])
ax.set(xlim=[0,100], ylim=[0,50])


def update(frame):
    x = distance[:frame]
    y = h[:frame]
    line2.set_xdata(distance[:frame])
    line2.set_ydata(h[:frame])
    return (line2,)


anim = animation.FuncAnimation(fig=fig, func=update, frames=len(t)+1, interval=20)
plt.get_current_fig_manager().window.activateWindow()
plt.show()