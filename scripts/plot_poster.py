import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/ket_qua_mo_phong.csv')

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(df['Time(ms)'], df['Voltage(mV)'], color='#2980b9', linewidth=3)

ax.axhline(-70, color='#27ae60', linestyle='--', linewidth=2.5, alpha=0.8)
ax.axhline(-55, color='#e74c3c', linestyle='--', linewidth=2.5, alpha=0.8)

x_max = df['Time(ms)'].max()
ax.text(x_max * 0.98, -69, 'Resting Potential', color='#27ae60', fontsize=14, va='bottom', ha='right', fontweight='bold', bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))
ax.text(x_max * 0.98, -54, 'Threshold', color='#e74c3c', fontsize=14, va='bottom', ha='right', fontweight='bold', bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

spikes = df[df['Voltage(mV)'] > 0]
if not spikes.empty:
    peak_idx = spikes['Voltage(mV)'].idxmax()
    peak_t = df.loc[peak_idx, 'Time(ms)']
    peak_v = df.loc[peak_idx, 'Voltage(mV)']
    
    ax.annotate('Spike', 
                xy=(peak_t, peak_v), 
                xytext=(peak_t + (x_max*0.05), peak_v),
                arrowprops=dict(facecolor='#c0392b', edgecolor='#c0392b', shrink=0.05, width=2, headwidth=10),
                fontsize=16, fontweight='bold', color='#c0392b',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

ax.set_title('LIF Neuron Simulation', fontsize=24, fontweight='bold', pad=25, color='#2c3e50')
ax.set_xlabel('Time (ms)', fontsize=18, fontweight='bold', labelpad=15)
ax.set_ylabel('Voltage (mV)', fontsize=18, fontweight='bold', labelpad=15)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.tight_layout()
plt.savefig('assets/poster_lif_simulation_detailed.png', dpi=600)