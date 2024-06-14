from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import gray, HexColor
from reportlab.pdfgen import canvas


def create_writing_sheet(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    solid_line_color = gray
    dashed_line_color = gray
    line_height = (
        30  # spacing between baselines in points (0.75 inches * 72 points/inch)
    )
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
