# def generate_pdf(self):
#     entries = [
#         "Medicine Name", "Price", "QTY", "SGST", "CGST", "HSN No.", "Item Name"
#     ]
#     data = [
#         [self.medicine.get(), self.price.get(), self.qty.get(), self.sgst.get(), self.cgst.get(),
#          self.hsn_no.get(), self.itemtype.get()]
#     ]
#     directory = "C:\\Users\\naura\\PycharmProjects\\AdvancePython\\StockInventary\\PDF"
#     table_data = [entries] + data
#
#     # Create the PDF document
#     pdf_filename = os.path.join(directory, "Stock_Inventory_Report.pdf")
#     pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
#     elements = []
#
#     # Add the title
#     title = "Stock Inventory Report"
#     elements.append(canvas.Canvas(pdf_filename).drawCentredString(300, 750, title))
#
#     # Add the table to the PDF
#     table = Table(table_data)
#     table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
#
#     elements.append(table)
#
#     # Build the PDF document
#     pdf.build(elements)
#     pdf.save()
#     messagebox.showinfo(f"PDF generated successfully: {pdf_filename}")
#     self.welcome_bill()