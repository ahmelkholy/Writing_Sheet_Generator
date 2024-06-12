Writing Sheet Generator

This script generates a PDF of a writing sheet using the ReportLab library.
The sheet includes solid baselines for writing and dashed guidelines for ascenders.

Dependencies:
- ReportLab (https://www.reportlab.com/)
  Install using: pip install reportlab

Functions:
- create_writing_sheet(filename): Generates a PDF writing sheet with specified parameters.

Usage:
1. Ensure you have Python installed on your system.
2. Install the ReportLab library using the command: pip install reportlab
3. Run the script to generate the PDF writing sheet using: python create_writing_sheet.py

Example:
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
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, gray, HexColor
from reportlab.pdfgen import canvas


def create_writing_sheet(filename):
    """
    Generates a PDF writing sheet with solid baselines and dashed guidelines for ascenders.

    Args:
        filename (str): The name of the output PDF file.

    Customizable Parameters:
        - line_height (int): Spacing between baselines in points (default: 30).
        - half_line_spacing (int): Spacing between baseline and ascender guideline in points (default: 18).
        - margin (float): Margins of the page in points (default: 3.5 * 28.35).
        - solid_line_color (Color): Color of the baseline (default: gray).
        - dashed_line_color (Color): Color of the ascender guideline (default: gray).
        - bottom_line_color (Color): Color of the bottom line (default: HexColor("#CCCCCC")).

    Returns:
        None
    """
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


if __name__ == "__main__":
    create_writing_sheet("writing_sheet.pdf")
