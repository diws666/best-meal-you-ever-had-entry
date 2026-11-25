import os

# Verified count: 132 characters (1 to 200 allowed by the bounty gate).
LINE = (
    "The best meal I ever had was my grandmother's fried rice at midnight, "
    "eaten straight from the wok while she pretended not to notice."
)

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
