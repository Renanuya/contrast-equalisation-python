import pandas as pd
from rich.console import Console
from rich.table import Table

file_path = "data/example_data.xlsx"
df = pd.read_excel(file_path, header=None)  #

data = df.values

histogram = [0] * 256
for row in data:
    for pixel in row:
        histogram[pixel] += 1

cdf = [0] * 256
cdf_value = 0
for i in range(256):
    cdf_value += histogram[i]
    cdf[i] = cdf_value

total_pixels = len(data) * len(data[0])
cdf_min = min(filter(lambda x: x > 0, cdf))

L = 256
equalized = [0] * 256
for i in range(256):
    equalized[i] = round(((cdf[i] - cdf_min) / (total_pixels - cdf_min)) * (L - 1))

equalized_image = []
for row in data:
    new_row = []
    for pixel in row:
        new_row.append(equalized[pixel])
    equalized_image.append(new_row)

console = Console()

table1 = Table(show_header=True, header_style="bold cyan")
table1.add_column("Value", style="dim", width=12)
table1.add_column("Count", style="green")

for i in range(256):
    if histogram[i] > 0:
        table1.add_row(str(i), str(histogram[i]))

console.print("\n[bold cyan]Value & Count Table:[/bold cyan]")
console.print(table1)

table2 = Table(show_header=True, header_style="bold magenta")
table2.add_column("Pixel Intensity", style="dim", width=16)
table2.add_column("CDF(v)", style="blue")
table2.add_column("Equalized v", style="red")

for i in range(256):
    if histogram[i] > 0:
        table2.add_row(str(i), str(cdf[i]), str(equalized[i]))

console.print("\n[bold magenta]Pixel Intensity, CDF(v), Equalized v Table:[/bold magenta]")
console.print(table2)
