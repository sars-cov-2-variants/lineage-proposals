import matplotlib.pyplot as plt

# Data
# 2025-1-2025-5: 1/19 (Merged)
# 2025-6: 1/12
# 2025-7: 4/12
# 2025-8: 6/17
# 2025-9: 2/5
# 2025-10: 4/9
# 2025-11: 4/6

data = [
    ("2025-01~05", 1, 19),
    ("2025-06", 1, 12),
    ("2025-07", 4, 12),
    ("2025-08", 6, 17),
    ("2025-09", 2, 5),
    ("2025-10", 4, 9),
    ("2025-11", 4, 6),
]

# Extract data for plotting
x_labels = [d[0] for d in data]
ratios = [d[1]/d[2] * 100 for d in data]
point_labels = [f"{d[1]/d[2]*100:.1f}%" for d in data]

# Create the plot
plt.figure(figsize=(10, 6))

# Plotting with categorical x-axis
plt.plot(x_labels, ratios, marker='o', linestyle='-', color='b')

# Add labels for each point
for i, txt in enumerate(point_labels):
    plt.annotate(txt, (x_labels[i], ratios[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Add titles and labels
plt.title("Indonesia XFW")
plt.xlabel("Date")
plt.ylabel("Percentage (%)")
plt.grid(True)

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
output_file = "indonesia_xfw.png"
plt.savefig(output_file)
print(f"Figure saved to {output_file}")
