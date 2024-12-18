from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io

def add_text_at_coordinates(input_pdf, output_pdf, text,x,y,font_size,center_align,color):

    # Load the existing PDF
    reader = PdfReader(input_pdf)
    page = reader.pages[0]
    page_width = page.mediabox.width
    page_height = page.mediabox.height

    # Create a new PDF layer with text at (x, y)
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    can.setFont("Times-Roman", font_size)  # Font and size
    if color=="black":
      can.setFillColor(colors.black)
    elif color=="#2f055c":
      can.setFillColor(colors.HexColor("#2f055c"))
    elif color=="darkblue":
      can.setFillColor(colors.darkblue)
    elif color=="red":
      can.setFillColor(colors.red)
    elif color=="#5c0516":
      can.setFillColor(colors.HexColor("#5c0516"))
    text_width=can.stringWidth(text,"Times-Roman",font_size)
    if center_align:
      x=int((float(page_width)-text_width)/2)
    else:
      x=x
    can.drawString(x, y, text)
    can.save()

    # Merge the new text with the existing PDF
    packet.seek(0)
    new_pdf = PdfReader(packet)
    writer = PdfWriter()
    page.merge_page(new_pdf.pages[0])
    writer.add_page(page)

    # Save the modified PDF
    with open(output_pdf, "wb") as output:
        writer.write(output)
    



def Generate_pdf(name,roll_no,department,session,teacher,subject,year):

    outputfile=name+"_"+subject+"_"+"file"+".pdf"
    branch=department+" "+year
    Dep="Department of "+department

    add_text_at_coordinates("FileFrontPage.pdf", outputfile,"SESSION: "+session,x=0,y=610,font_size=22,center_align=True,color="black")
    add_text_at_coordinates(outputfile, outputfile, subject,x=0,y=580,font_size=20,center_align=True,color="darkblue")

    add_text_at_coordinates(outputfile, outputfile, "Submitted by:",x=50,y=480,font_size=20,center_align=False,color="black")
    add_text_at_coordinates(outputfile, outputfile, name,x=50,y=450,font_size=18,center_align=False,color="red")
    add_text_at_coordinates(outputfile, outputfile, "Roll No: ",x=50,y=420,font_size=20,center_align=False,color="#5c0516")
    add_text_at_coordinates(outputfile, outputfile, roll_no,x=130,y=420,font_size=18,center_align=False,color="red")
    add_text_at_coordinates(outputfile, outputfile, branch,x=50,y=390,font_size=18,center_align=False,color="red")

    add_text_at_coordinates(outputfile, outputfile, "Submitted To:",x=400,y=480,font_size=20,center_align=False,color="black")
    add_text_at_coordinates(outputfile, outputfile, teacher,x=400,y=450,font_size=18,center_align=False,color="red")
    add_text_at_coordinates(outputfile, outputfile, "Teacher's Signature",x=400,y=420,font_size=20,center_align=False,color="#5c0516")
    add_text_at_coordinates(outputfile, outputfile, "_ _ _ _ _ _ _ _ _ _",x=400,y=390,font_size=20,center_align=False,color="#5c0516")


    add_text_at_coordinates(outputfile, outputfile, "Bachelor of Technology in Computer Science",x=0,y=230,font_size=26,center_align=True,color="#2f055c")
    add_text_at_coordinates(outputfile, outputfile, "and Engineering",x=0,y=200,font_size=26,center_align=True,color="#2f055c")
    add_text_at_coordinates(outputfile, outputfile, Dep,x=0,y=170,font_size=26,center_align=True,color="#2f055c")
