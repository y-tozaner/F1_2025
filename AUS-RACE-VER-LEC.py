from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
#
fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme= 'fastf1')
session = fastf1.get_session(2025, 1, 5) #Choosing the event
session.load()
#
ver_lap = session.laps.pick_driver('VER').pick_fastest() #Choosing the lap
ver_car_data = ver_lap.get_car_data().add_distance()
lec_lap = session.laps.pick_driver('LEC').pick_fastest()
lec_car_data = lec_lap.get_car_data().add_distance()
#
#Extracting data
ver_vCar = ver_car_data['Speed']
ver_nCar = ver_car_data['RPM']
ver_nGear = ver_car_data['nGear']
#
lec_vCar = lec_car_data['Speed']
lec_nCar = lec_car_data['RPM']
lec_nGear = lec_car_data['nGear']
#
#Plotting
fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0) #Defining the number, the spacing and the config of subplots
axs = gs.subplots(sharex=True, sharey=False) #Defining the shared x-axis of the plots

fig.suptitle('2025 Australian GP Race Verstappen- Leclerc Fastest Lap')
axs[0].plot (ver_car_data['Distance'], ver_vCar, color='#0055ffff')
axs[0].plot (lec_car_data['Distance'], lec_vCar, color='#E21B4D')
axs[0].set_ylabel('Speed (km/h)')
axs[1].plot(ver_car_data['Distance'], ver_nCar, color='#0055ffff')
axs[1].plot(lec_car_data['Distance'], lec_nCar, color='#E21B4D')
axs[1].set_ylabel('RPM')
axs[2].plot (ver_car_data['Distance'], ver_nGear, color='#0055ffff')
axs[2].plot (lec_car_data['Distance'], lec_nGear, color='#E21B4D')
axs[2].set_ylabel('Gear')
for ax in fig.get_axes():
    ax.label_outer() #Only labelling the bottom x-axis
    ax.set_xlabel('Time')
    ax.legend()
fig.align_ylabels() #Alligning the y-axis labels
#
plt.show()
