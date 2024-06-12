
```markdown
# Writing Sheet Generator

This Python script generates a PDF of a writing sheet using the ReportLab library. The sheet includes solid baselines for writing and dashed guidelines for ascenders.

## Features

- Generates a PDF writing sheet with customizable line height and margins.
- Solid baseline lines for writing.
- Dashed guideline lines for ascenders.
- Light grey bottom line.

## Dependencies

- [ReportLab](https://www.reportlab.com/)

You can install ReportLab using pip:

```sh
pip install reportlab
```

## Usage

1. Ensure you have Python installed on your system.
2. Install the ReportLab library using the command above.
3. Run the script to generate the PDF writing sheet.

### Running the Script

```sh
python create_writing_sheet.py
```

The script will generate a PDF file named `writing_sheet.pdf` in the same directory.

## Customization

You can customize various aspects of the writing sheet by modifying the script:

- `line_height`: Spacing between baselines in points.
- `half_line_spacing`: Spacing between baseline and ascender guideline in points.
- `margin`: Margins of the page in points.
- `solid_line_color`: Color of the baseline.
- `dashed_line_color`: Color of the ascender guideline.
- `bottom_line_color`: Color of the bottom line.

## Example

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray, HexColor
from reportlab.pdfgen import canvas

def create_writing_sheet(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    solid_line_color = gray
    dashed_line_color = gray
    line_height = 30  # spacing between baselines in points (0.75 inches * 72 points/inch)
    half_line_spacing = 18  # 6.35 mm in points
    margin = 3.5 * 28.35  # 2 cm in points
    bottom_line_color = HexColor("#CCCCCC")  # Light grey color for bottom line

    # Adjust the initial value of y
    y = height - margin - half_line_spacing

    while y > margin:
        # Draw solid baseline for writing
        c.setStrokeColor(solid_line_color)
        c.setLineWidth(0.5)
        c.line(margin, y, width - margin, y)

        # Draw guideline for ascenders 0.5mm above the baseline
        c.setStrokeColor(dashed_line_color)
        c.setLineWidth(0.5)
        c.setDash(1, 2)  # Set dashed line pattern
        c.line(margin, y - half_line_spacing, width - margin, y - half_line_spacing)
        c.setDash()  # Reset to solid line

        # Move to the next baseline
        y -= line_height
    # Draw the bottom line less dark
    c.setStrokeColor(bottom_line_color)
    c.setLineWidth(0.5)
    c.line(margin, margin, width - margin, margin)

    c.showPage()
    c.save()

create_writing_sheet("writing_sheet.pdf")
```

Feel free to modify the script and settings to suit your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides a comprehensive overview of the script, including how to install dependencies, run the script, and customize its behavior.ere is a `README.md` file for your GitHub repository that explains the purpose of the script, its dependencies, and how to use it.

```markdown
# Writing Sheet Generator

This Python script generates a PDF of a writing sheet using the ReportLab library. The sheet includes solid baselines for writing and dashed guidelines for ascenders.

## Features

- Generates a PDF writing sheet with customizable line height and margins.
- Solid baseline lines for writing.
- Dashed guideline lines for ascenders.
- Light grey bottom line.

## Dependencies

- [ReportLab](https://www.reportlab.com/)

You can install ReportLab using pip:

```sh
pip install reportlab
```

## Usage

1. Ensure you have Python installed on your system.
2. Install the ReportLab library using the command above.
3. Run the script to generate the PDF writing sheet.

### Running the Script

```sh
python create_writing_sheet.py
```

The script will generate a PDF file named `writing_sheet.pdf` in the same directory.

## Customization

You can customize various aspects of the writing sheet by modifying the script:

- `line_height`: Spacing between baselines in points.
- `half_line_spacing`: Spacing between baseline and ascender guideline in points.
- `margin`: Margins of the page in points.
- `solid_line_color`: Color of the baseline.
- `dashed_line_color`: Color of the ascender guideline.
- `bottom_line_color`: Color of the bottom line.

## Example

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray, HexColor
from reportlab.pdfgen import canvas

def create_writing_sheet(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    solid_line_color = gray
    dashed_line_color = gray
    line_height = 30  # spacing between baselines in points (0.75 inches * 72 points/inch)
    half_line_spacing = 18  # 6.35 mm in points
    margin = 3.5 * 28.35  # 2 cm in points
    bottom_line_color = HexColor("#CCCCCC")  # Light grey color for bottom line

    # Adjust the initial value of y
    y = height - margin - half_line_spacing

    while y > margin:
        # Draw solid baseline for writing
        c.setStrokeColor(solid_line_color)
        c.setLineWidth(0.5)
        c.line(margin, y, width - margin, y)

        # Draw guideline for ascenders 0.5mm above the baseline
        c.setStrokeColor(dashed_line_color)
        c.setLineWidth(0.5)
        c.setDash(1, 2)  # Set dashed line pattern
        c.line(margin, y - half_line_spacing, width - margin, y - half_line_spacing)
        c.setDash()  # Reset to solid line

        # Move to the next baseline
        y -= line_height
    # Draw the bottom line less dark
    c.setStrokeColor(bottom_line_color)
    c.setLineWidth(0.5)
    c.line(margin, margin, width - margin, margin)

    c.showPage()
    c.save()

create_writing_sheet("writing_sheet.pdf")
```

Feel free to modify the script and settings to suit your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
