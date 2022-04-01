from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import requests, getpass
from pytz import timezone 
from datetime import datetime
import os

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica-Bold',10)
can.drawString(350,730, "TCIL")# name of msi
can.drawString(350,718,"1") # mb no.
can.drawString(350,706,"1") # sheet no.
can.drawString(350,694,"GP") # pop type
can.drawString(350,683,"Nalgonda")# Zone/mandal/Gp Name
can.drawString(350,659,"SpanID")

can.drawString(70,560,'1')
can.drawString(80,560,'Ch_f1')
can.drawString(120,560,'Ch_t1')
can.drawString(160,560,'Cb_f1')
can.drawString(200,560,'Cbt1')
can.drawString(240,560,'Len1')
can.drawString(290,560,'Tst1')# Air Test Result
can.drawString(350,560,'Tst1')# Sponge Test
can.drawString(410,560,'Ok')# Shuttle Test
can.drawString(470,560,'1')# Press applies 5bar 30min
can.drawString(570,560,'1')#Press applies 10bar 30min
can.drawString(670,560,'1')# Press obs after 10/30 min
can.drawString(750,560,'1')# Drop in press
can.drawString(805,560,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,560,'18.123456 / 78.123456')#Loc of coupler

can.setFont('Helvetica-Bold',10)
can.drawString(945,560,'1')# MB Duct Missing from
can.drawString(970,560,'1')# MB Duct Missing To
can.drawString(1020,560,'1')# Duct missing Len
can.drawString(1060,560,'Ok')#Remarks

can.drawString(70,548,'1')
can.drawString(80,548,'Ch_f1')
can.drawString(120,548,'Ch_t1')
can.drawString(160,548,'Cb_f1')
can.drawString(200,548,'Cbt1')
can.drawString(240,548,'Len1')
can.drawString(290,548,'Tst1')# Air Test Result
can.drawString(350,548,'Tst1')# Sponge Test
can.drawString(410,548,'Ok')# Shuttle Test
can.drawString(470,548,'1')# Press applies 5bar 30min
can.drawString(570,548,'1')#Press applies 10bar 30min
can.drawString(670,548,'1')# Press obs after 10/30 min
can.drawString(750,548,'1')# Drop in press
can.drawString(805,548,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,548,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,548,'1')# MB Duct Missing from
can.drawString(970,548,'1')# MB Duct Missing To
can.drawString(1020,548,'1')# Duct missing Len
can.drawString(1060,548,'Ok')#Remarks

can.drawString(70,536,'1')
can.drawString(80,536,'Ch_f1')
can.drawString(120,536,'Ch_t1')
can.drawString(160,536,'Cb_f1')
can.drawString(200,536,'Cbt1')
can.drawString(240,536,'Len1')
can.drawString(290,536,'Tst1')# Air Test Result
can.drawString(350,536,'Tst1')# Sponge Test
can.drawString(410,536,'Ok')# Shuttle Test
can.drawString(470,536,'1')# Press applies 5bar 30min
can.drawString(570,536,'1')#Press applies 10bar 30min
can.drawString(670,536,'1')# Press obs after 10/30 min
can.drawString(750,536,'1')# Drop in press
can.drawString(805,536,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,536,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,536,'1')# MB Duct Missing from
can.drawString(970,536,'1')# MB Duct Missing To
can.drawString(1020,536,'1')# Duct missing Len
can.drawString(1060,536,'Ok')#Remarks

can.drawString(70,524,'1')
can.drawString(80,524,'Ch_f1')
can.drawString(120,524,'Ch_t1')
can.drawString(160,524,'Cb_f1')
can.drawString(200,524,'Cbt1')
can.drawString(240,524,'Len1')
can.drawString(290,524,'Tst1')# Air Test Result
can.drawString(350,524,'Tst1')# Sponge Test
can.drawString(410,524,'Ok')# Shuttle Test
can.drawString(470,524,'1')# Press applies 5bar 30min
can.drawString(570,524,'1')#Press applies 10bar 30min
can.drawString(670,524,'1')# Press obs after 10/30 min
can.drawString(750,524,'1')# Drop in press
can.drawString(805,524,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,524,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,524,'1')# MB Duct Missing from
can.drawString(970,524,'1')# MB Duct Missing To
can.drawString(1020,524,'1')# Duct missing Len
can.drawString(1060,524,'Ok')#Remarks

can.drawString(70,512,'1')
can.drawString(80,512,'Ch_f1')
can.drawString(120,512,'Ch_t1')
can.drawString(160,512,'Cb_f1')
can.drawString(200,512,'Cbt1')
can.drawString(240,512,'Len1')
can.drawString(290,512,'Tst1')# Air Test Result
can.drawString(350,512,'Tst1')# Sponge Test
can.drawString(410,512,'Ok')# Shuttle Test
can.drawString(470,512,'1')# Press applies 5bar 30min
can.drawString(570,512,'1')#Press applies 10bar 30min
can.drawString(670,512,'1')# Press obs after 10/30 min
can.drawString(750,512,'1')# Drop in press
can.drawString(805,512,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,512,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,512,'1')# MB Duct Missing from
can.drawString(970,512,'1')# MB Duct Missing To
can.drawString(1020,512,'1')# Duct missing Len
can.drawString(1060,512,'Ok')#Remarks

can.drawString(70,500,'1')
can.drawString(80,500,'Ch_f1')
can.drawString(120,500,'Ch_t1')
can.drawString(160,500,'Cb_f1')
can.drawString(200,500,'Cbt1')
can.drawString(240,500,'Len1')
can.drawString(290,500,'Tst1')# Air Test Result
can.drawString(350,500,'Tst1')# Sponge Test
can.drawString(410,500,'Ok')# Shuttle Test
can.drawString(470,500,'1')# Press applies 5bar 30min
can.drawString(570,500,'1')#Press applies 10bar 30min
can.drawString(670,500,'1')# Press obs after 10/30 min
can.drawString(750,500,'1')# Drop in press
can.drawString(805,500,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,500,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,500,'1')# MB Duct Missing from
can.drawString(970,500,'1')# MB Duct Missing To
can.drawString(1020,500,'1')# Duct missing Len
can.drawString(1060,500,'Ok')#Remarks

can.drawString(70,488,'1')
can.drawString(80,488,'Ch_f1')
can.drawString(120,488,'Ch_t1')
can.drawString(160,488,'Cb_f1')
can.drawString(200,488,'Cbt1')
can.drawString(240,488,'Len1')
can.drawString(290,488,'Tst1')# Air Test Result
can.drawString(350,488,'Tst1')# Sponge Test
can.drawString(410,488,'Ok')# Shuttle Test
can.drawString(470,488,'1')# Press applies 5bar 30min
can.drawString(570,488,'1')#Press applies 10bar 30min
can.drawString(670,488,'1')# Press obs after 10/30 min
can.drawString(750,488,'1')# Drop in press
can.drawString(805,488,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,488,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,488,'1')# MB Duct Missing from
can.drawString(970,488,'1')# MB Duct Missing To
can.drawString(1020,488,'1')# Duct missing Len
can.drawString(1060,488,'Ok')#Remarks

can.drawString(70,476,'1')
can.drawString(80,476,'Ch_f1')
can.drawString(120,476,'Ch_t1')
can.drawString(160,476,'Cb_f1')
can.drawString(200,476,'Cbt1')
can.drawString(240,476,'Len1')
can.drawString(290,476,'Tst1')# Air Test Result
can.drawString(350,476,'Tst1')# Sponge Test
can.drawString(410,476,'Ok')# Shuttle Test
can.drawString(470,476,'1')# Press applies 5bar 30min
can.drawString(570,476,'1')#Press applies 10bar 30min
can.drawString(670,476,'1')# Press obs after 10/30 min
can.drawString(750,476,'1')# Drop in press
can.drawString(805,476,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,476,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,476,'1')# MB Duct Missing from
can.drawString(970,476,'1')# MB Duct Missing To
can.drawString(1020,476,'1')# Duct missing Len
can.drawString(1060,476,'Ok')#Remarks

can.drawString(70,464,'1')
can.drawString(80,464,'Ch_f1')
can.drawString(120,464,'Ch_t1')
can.drawString(160,464,'Cb_f1')
can.drawString(200,464,'Cbt1')
can.drawString(240,464,'Len1')
can.drawString(290,464,'Tst1')# Air Test Result
can.drawString(350,464,'Tst1')# Sponge Test
can.drawString(410,464,'Ok')# Shuttle Test
can.drawString(470,464,'1')# Press applies 5bar 30min
can.drawString(570,464,'1')#Press applies 10bar 30min
can.drawString(670,464,'1')# Press obs after 10/30 min
can.drawString(750,464,'1')# Drop in press
can.drawString(805,464,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,464,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,464,'1')# MB Duct Missing from
can.drawString(970,464,'1')# MB Duct Missing To
can.drawString(1020,464,'1')# Duct missing Len
can.drawString(1060,464,'Ok')#Remarks

can.drawString(70,452,'1')
can.drawString(80,452,'Ch_f1')
can.drawString(120,452,'Ch_t1')
can.drawString(160,452,'Cb_f1')
can.drawString(200,452,'Cbt1')
can.drawString(240,452,'Len1')
can.drawString(290,452,'Tst1')# Air Test Result
can.drawString(350,452,'Tst1')# Sponge Test
can.drawString(410,452,'Ok')# Shuttle Test
can.drawString(470,452,'1')# Press applies 5bar 30min
can.drawString(570,452,'1')#Press applies 10bar 30min
can.drawString(670,452,'1')# Press obs after 10/30 min
can.drawString(750,452,'1')# Drop in press
can.drawString(805,452,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,452,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,452,'1')# MB Duct Missing from
can.drawString(970,452,'1')# MB Duct Missing To
can.drawString(1020,452,'1')# Duct missing Len
can.drawString(1060,452,'Ok')#Remarks

can.drawString(70,440,'1')
can.drawString(80,440,'Ch_f1')
can.drawString(120,440,'Ch_t1')
can.drawString(160,440,'Cb_f1')
can.drawString(200,440,'Cbt1')
can.drawString(240,440,'Len1')
can.drawString(290,440,'Tst1')# Air Test Result
can.drawString(350,440,'Tst1')# Sponge Test
can.drawString(410,440,'Ok')# Shuttle Test
can.drawString(470,440,'1')# Press applies 5bar 30min
can.drawString(570,440,'1')#Press applies 10bar 30min
can.drawString(670,440,'1')# Press obs after 10/30 min
can.drawString(750,440,'1')# Drop in press
can.drawString(805,440,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,440,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,440,'1')# MB Duct Missing from
can.drawString(970,440,'1')# MB Duct Missing To
can.drawString(1020,440,'1')# Duct missing Len
can.drawString(1060,440,'Ok')#Remarks

can.drawString(70,428,'1')
can.drawString(80,428,'Ch_f1')
can.drawString(120,428,'Ch_t1')
can.drawString(160,428,'Cb_f1')
can.drawString(200,428,'Cbt1')
can.drawString(240,428,'Len1')
can.drawString(290,428,'Tst1')# Air Test Result
can.drawString(350,428,'Tst1')# Sponge Test
can.drawString(410,428,'Ok')# Shuttle Test
can.drawString(470,428,'1')# Press applies 5bar 30min
can.drawString(570,428,'1')#Press applies 10bar 30min
can.drawString(670,428,'1')# Press obs after 10/30 min
can.drawString(750,428,'1')# Drop in press
can.drawString(805,428,'Not Ok')# Test REs
can.setFont('Helvetica-Bold',7)
can.drawString(855,428,'95978087780')#Loc of coupler
can.setFont('Helvetica-Bold',10)
can.drawString(945,428,'1')# MB Duct Missing from
can.drawString(970,428,'1')# MB Duct Missing To
can.drawString(1020,428,'1')# Duct missing Len
can.drawString(1060,428,'Ok')#Remarks



# can.drawString()
can.save()
packet.seek(0)
new_pdf = PdfFileReader(packet,strict=False)
existing_pdf = PdfFileReader(open(r"C:\Users\parth.pandey\Desktop\Field Force Forms\AT_Report/R09-Duct Integrity Test REPORT.pdf", "rb"),strict=False)
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open(r'C:\Users\parth.pandey\Desktop\Field Force Forms\Test/final_path.pdf', "wb")
output.write(outputStream)
outputStream.close()