from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import requests, getpass
from pytz import timezone 
from datetime import datetime
import os

# ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y_%m_%d_%H_%M_%S') # this time will be filename
# ind_time=str(ind_time)

import sqlite3
from sqlite3 import Error

class Create_connection:
    def __init__(self,db_file):
        self.db_file=db_file
    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
    
        return conn

class HDD_form:
    def __init__(self,conn,form,span_id,prikey):
        self.conn=conn
        self.form=form
        self.span_id=span_id
        self.prikey=prikey
    def query_tasks(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        form=self.form
        prikey=self.prikey
        span_id=self.span_id
    
        cur = self.conn.cursor()
        # zone_name='Warangal'
        command="SELECT * FROM hdd WHERE span_id = \'"+span_id+"\' AND prikey >="+ str(prikey)
        cur.execute(command)
        
        
        rows = cur.fetchall()
        if len(rows)==0:
            print('Nothing to Show')
        else:
            date_time=self.make_pdf(rows)
            return date_time
    def make_pdf(self,data):
        self.data=data
        data=self.data
        # Initialising Canvas
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        # print(len(data))
        hdd_form_coordinates=[[298, 505],[298, 490],[298,476],[298,462],[298,448],[298,434],[298,422],[298,408],
        [55,350],[120,350],[210,350],[250,350],[300,350],[360,350],[450,350],[540,350],[630,350],[700,350],
        [55,337],[120,337],[210,337],[250,337],[300,337],[360,337],[450,337],[540,337],[630,337],[700,337],
        [55,323],[120,323],[210,323],[250,323],[300,323],[360,323],[450,323],[540,323],[630,323],[700,323],
        [55,310],[120,310],[210,310],[250,310],[300,310],[360,310],[450,310],[540,310],[630,310],[700,310],
        [55,296],[120,296],[210,296],[250,296],[300,296],[360,296],[450,296],[540,296],[630,296],[700,296],
        [120,236],[250,236],[540,236],[700,236],[120,222],[250,222],[540,222],[700,222],[120,208],[250,208],
        [540,208],[700,208],[120,194],[250,194],[540,194],[700,194],[120,180],[250,180],[540,180],[700,180]]
        
        # Looping over json data with maximum 5 rows for HDD MB
        
        i=0
        # print(data[i])
        while(i<len(data) and i<5):
            if i==0:
                can.drawString(hdd_form_coordinates[0][0],hdd_form_coordinates[0][1], "TCIL") # Name of MSI
                can.drawString(hdd_form_coordinates[1][0],hdd_form_coordinates[1][1], "1") # MB Book no
                can.drawString(hdd_form_coordinates[2][0],hdd_form_coordinates[2][1],"1")# Sheet No
                can.drawString(hdd_form_coordinates[3][0],hdd_form_coordinates[3][1],"GP")# POP type
                can.drawString(hdd_form_coordinates[4][0],hdd_form_coordinates[4][1],data[i][18]+"/"+data[i][20]+"/"+data[i][22])# Zone/mandal/GP Name
                can.drawString(hdd_form_coordinates[5][0],hdd_form_coordinates[5][1],"")# Ring ID
                can.drawString(hdd_form_coordinates[6][0],hdd_form_coordinates[6][1],data[0][23]) # Span ID
                can.drawString(hdd_form_coordinates[7][0],hdd_form_coordinates[7][1],"")# ABD Refernce
        
                can.drawString(hdd_form_coordinates[8][0],hdd_form_coordinates[8][1],"1")# Sr no
                can.drawString(hdd_form_coordinates[9][0],hdd_form_coordinates[9][1],data[i][24])# Side of road
                can.drawString(hdd_form_coordinates[10][0],hdd_form_coordinates[10][1],data[i][25])# Pit ch from
                can.drawString(hdd_form_coordinates[11][0],hdd_form_coordinates[11][1],data[i][26])# ch to
                can.drawString(hdd_form_coordinates[12][0],hdd_form_coordinates[12][1],data[i][27])# len
                can.drawString(hdd_form_coordinates[13][0],hdd_form_coordinates[13][1],data[i][29])# gr as build made
                can.drawString(hdd_form_coordinates[14][0],hdd_form_coordinates[14][1],data[i][30])# depth
                can.drawString(hdd_form_coordinates[15][0],hdd_form_coordinates[15][1],data[i][31])#dia
                can.drawString(hdd_form_coordinates[16][0],hdd_form_coordinates[16][1],data[i][32])# duct
                can.drawString(hdd_form_coordinates[17][0],hdd_form_coordinates[17][1],str(data[i][33]))# remark
        
                can.drawString(hdd_form_coordinates[58][0],hdd_form_coordinates[58][1],str(data[i][35]))# start lat
                can.drawString(hdd_form_coordinates[59][0],hdd_form_coordinates[59][1],str(data[i][36]))# start long
                can.drawString(hdd_form_coordinates[60][0],hdd_form_coordinates[60][1],str(data[i][37]))# end lat
                can.drawString(hdd_form_coordinates[61][0],hdd_form_coordinates[61][1],str(data[i][38]))# end long
        
            if i==1:
                can.drawString(hdd_form_coordinates[18][0],hdd_form_coordinates[18][1],"2")
                can.drawString(hdd_form_coordinates[19][0],hdd_form_coordinates[19][1],data[i][24])
                can.drawString(hdd_form_coordinates[20][0],hdd_form_coordinates[20][1],data[i][25])# Pit ch from
                can.drawString(hdd_form_coordinates[21][0],hdd_form_coordinates[21][1],data[i][26])# ch to
                can.drawString(hdd_form_coordinates[22][0],hdd_form_coordinates[22][1],data[i][27])# len
                can.drawString(hdd_form_coordinates[23][0],hdd_form_coordinates[23][1],data[i][29])# gr as build made
                can.drawString(hdd_form_coordinates[24][0],hdd_form_coordinates[24][1],data[i][30])# depth
                can.drawString(hdd_form_coordinates[25][0],hdd_form_coordinates[25][1],data[i][31])#dia
                can.drawString(hdd_form_coordinates[26][0],hdd_form_coordinates[26][1],data[i][32])# duct
                can.drawString(hdd_form_coordinates[27][0],hdd_form_coordinates[27][1],str(data[i][33]))# remark
        
                can.drawString(hdd_form_coordinates[62][0],hdd_form_coordinates[62][1],str(data[i][35]))# start lat
                can.drawString(hdd_form_coordinates[63][0],hdd_form_coordinates[63][1],str(data[i][36]))# start long
                can.drawString(hdd_form_coordinates[64][0],hdd_form_coordinates[64][1],str(data[i][37]))# end lat
                can.drawString(hdd_form_coordinates[65][0],hdd_form_coordinates[65][1],str(data[i][38]))# end long
        
            if i==2:
                can.drawString(hdd_form_coordinates[28][0],hdd_form_coordinates[28][1],"3")
                can.drawString(hdd_form_coordinates[29][0],hdd_form_coordinates[29][1],data[i][24])
                can.drawString(hdd_form_coordinates[30][0],hdd_form_coordinates[30][1],data[i][25])# Pit ch from
                can.drawString(hdd_form_coordinates[31][0],hdd_form_coordinates[31][1],data[i][26])# ch to
                can.drawString(hdd_form_coordinates[32][0],hdd_form_coordinates[32][1],data[i][27])# len
                can.drawString(hdd_form_coordinates[33][0],hdd_form_coordinates[33][1],data[i][29])# gr as build made
                can.drawString(hdd_form_coordinates[34][0],hdd_form_coordinates[34][1],data[i][30])# depth
                can.drawString(hdd_form_coordinates[35][0],hdd_form_coordinates[35][1],data[i][31])#dia
                can.drawString(hdd_form_coordinates[36][0],hdd_form_coordinates[36][1],data[i][32])# duct
                can.drawString(hdd_form_coordinates[37][0],hdd_form_coordinates[37][1],str(data[i][33]))# remark
        
                can.drawString(hdd_form_coordinates[66][0],hdd_form_coordinates[66][1],str(data[i][35]))# start lat
                can.drawString(hdd_form_coordinates[67][0],hdd_form_coordinates[67][1],str(data[i][36]))# start long
                can.drawString(hdd_form_coordinates[68][0],hdd_form_coordinates[68][1],str(data[i][37]))# end lat
                can.drawString(hdd_form_coordinates[69][0],hdd_form_coordinates[69][1],str(data[i][38]))# end long
        
            if i==3:
                can.drawString(hdd_form_coordinates[38][0],hdd_form_coordinates[38][1],"4")
                can.drawString(hdd_form_coordinates[39][0],hdd_form_coordinates[39][1],data[i][24])
                can.drawString(hdd_form_coordinates[40][0],hdd_form_coordinates[40][1],data[i][25])# Pit ch from
                can.drawString(hdd_form_coordinates[41][0],hdd_form_coordinates[41][1],data[i][26])# ch to
                can.drawString(hdd_form_coordinates[42][0],hdd_form_coordinates[42][1],data[i][27])# len
                can.drawString(hdd_form_coordinates[43][0],hdd_form_coordinates[43][1],data[i][29])# gr as build made
                can.drawString(hdd_form_coordinates[44][0],hdd_form_coordinates[44][1],data[i][30])# depth
                can.drawString(hdd_form_coordinates[45][0],hdd_form_coordinates[45][1],data[i][31])#dia
                can.drawString(hdd_form_coordinates[46][0],hdd_form_coordinates[46][1],data[i][32])# duct
                can.drawString(hdd_form_coordinates[47][0],hdd_form_coordinates[47][1],str(data[i][33]))# remark
        
                can.drawString(hdd_form_coordinates[70][0],hdd_form_coordinates[70][1],str(data[i][35]))# start lat
                can.drawString(hdd_form_coordinates[71][0],hdd_form_coordinates[71][1],str(data[i][36]))# start long
                can.drawString(hdd_form_coordinates[72][0],hdd_form_coordinates[72][1],str(data[i][37]))# end lat
                can.drawString(hdd_form_coordinates[73][0],hdd_form_coordinates[73][1],str(data[i][38]))# end long
        
        
            if i==4:
                can.drawString(hdd_form_coordinates[48][0],hdd_form_coordinates[48][1],"5")
                can.drawString(hdd_form_coordinates[49][0],hdd_form_coordinates[49][1],data[i][24])
                can.drawString(hdd_form_coordinates[50][0],hdd_form_coordinates[50][1],data[i][25])# Pit ch from
                can.drawString(hdd_form_coordinates[51][0],hdd_form_coordinates[51][1],data[i][26])# ch to
                can.drawString(hdd_form_coordinates[52][0],hdd_form_coordinates[52][1],data[i][27])# len
                can.drawString(hdd_form_coordinates[53][0],hdd_form_coordinates[53][1],data[i][29])# gr as build made
                can.drawString(hdd_form_coordinates[54][0],hdd_form_coordinates[54][1],data[i][30])# depth
                can.drawString(hdd_form_coordinates[55][0],hdd_form_coordinates[55][1],data[i][31])#dia
                can.drawString(hdd_form_coordinates[56][0],hdd_form_coordinates[56][1],data[i][32])# duct
                can.drawString(hdd_form_coordinates[57][0],hdd_form_coordinates[57][1],str(data[i][33]))# remark
        
                can.drawString(hdd_form_coordinates[74][0],hdd_form_coordinates[74][1],str(data[i][35]))# start lat
                can.drawString(hdd_form_coordinates[75][0],hdd_form_coordinates[75][1],str(data[i][36]))# start long
                can.drawString(hdd_form_coordinates[76][0],hdd_form_coordinates[76][1],str(data[i][37]))# end lat
                can.drawString(hdd_form_coordinates[77][0],hdd_form_coordinates[77][1],str(data[i][38]))# end long
            i+=1
        
        
        
        
        
        # # Coordinates
        
        
        can.save()
        
        #move to the beginning of the StringIO buffer
        packet.seek(0)
        
        # create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        cwd=os.getcwd()
        directory='AT_Report/R08-HDD REPORT.pdf'
        path = os.path.join(cwd, directory)
        existing_pdf = PdfFileReader(open(path, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        d="destination"
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y_%m_%d_%H_%M_%S') # this time will be filename
        ind_time=str(ind_time)
        final_directory="Output\PDF/"+ind_time+self.span_id+".pdf"
        final_path=os.path.join(cwd, final_directory)
        outputStream = open(final_path, "wb")
        output.write(outputStream)
        outputStream.close()
        return ind_time

class DIT_form:
    def __init__(self,conn,form,span_id,prikey):
        self.conn=conn
        self.form=form
        self.span_id=span_id
        self.prikey=prikey
    def query_tasks(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        form=self.form
        prikey=self.prikey
        span_id=self.span_id
    
        cur = self.conn.cursor()
        # zone_name='Warangal'
        command="SELECT * FROM dit WHERE span_id = \'"+span_id+"\' AND prikey >="+ str(prikey)
        cur.execute(command)
        
        
        rows = cur.fetchall()
        if len(rows)==0:
            print('Nothing to Show')
        else:
            date_time=self.make_pdf(rows)
            return date_time
    def make_pdf(self,data):
        self.data=data
        data=self.data
        # Initialising Canvas
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        # print(len(data))
        dit_form_coordinates=[
            [350,730],
            [350,718],
            [350,706],
            [350,694],
            [350,683],
            [350,659],
            [70,560],
            [80,560],
            [120,560],
            [160,560],
            [200,560],
            [240,560],
            [290,560],
            [350,560],
            [410,560],
            [470,560],
            [570,560],
            [670,560],
            [750,560],
            [805,560],
            [855,560],
            [945,560],
            [970,560],
            [1020,560],
            [1060,560],
            [70,548 ],
            [80,548 ],
            [120,548],
            [160,548],
            [200,548],
            [240,548],
            [290,548],
            [350,548],
            [410,548],
            [470,548],
            [570,548],
            [670,548],
            [750,548],
            [805,548],
            [855,548],
            [945,548 ],
            [970,548 ],
            [1020,548],
            [1060,548],
            [70,536 ],
            [80,536 ],
            [120,536],
            [160,536],
            [200,536],
            [240,536],
            [290,536],
            [350,536],
            [410,536],
            [470,536],
            [570,536],
            [670,536],
            [750,536],
            [805,536],
            [855,536],
            [945,536 ],
            [970,536 ],
            [1020,536],
            [1060,536],
            [70,524 ],
            [80,524 ],
            [120,524],
            [160,524],
            [200,524],
            [240,524],
            [290,524],
            [350,524],
            [410,524],
            [470,524],
            [570,524],
            [670,524],
            [750,524],
            [805,524],
            [855,524],
            [945,524 ],
            [970,524 ],
            [1020,524],
            [1060,524],
            [70,512 ],
            [80,512 ],
            [120,512],
            [160,512],
            [200,512],
            [240,512],
            [290,512],
            [350,512],
            [410,512],
            [470,512],
            [570,512],
            [670,512],
            [750,512],
            [805,512],
            [855,512],
            [945,512 ],
            [970,512 ],
            [1020,512],
            [1060,512],
            [70,500 ],
            [80,500 ],
            [120,500],
            [160,500],
            [200,500],
            [240,500],
            [290,500],
            [350,500],
            [410,500],
            [470,500],
            [570,500],
            [670,500],
            [750,500],
            [805,500],
            [855,500],
            [945,500 ],
            [970,500 ],
            [1020,500],
            [1060,500],
            [70,488 ],
            [80,488 ],
            [120,488],
            [160,488],
            [200,488],
            [240,488],
            [290,488],
            [350,488],
            [410,488],
            [470,488],
            [570,488],
            [670,488],
            [750,488],
            [805,488],
            [855,488],
            [945,488 ],
            [970,488 ],
            [1020,488],
            [1060,488],
            [70,476 ],
            [80,476 ],
            [120,476],
            [160,476],
            [200,476],
            [240,476],
            [290,476],
            [350,476],
            [410,476],
            [470,476],
            [570,476],
            [670,476],
            [750,476],
            [805,476],
            [855,476],
            [945,476 ],
            [970,476 ],
            [1020,476],
            [1060,476],
            [70,464 ],
            [80,464 ],
            [120,464],
            [160,464],
            [200,464],
            [240,464],
            [290,464],
            [350,464],
            [410,464],
            [470,464],
            [570,464],
            [670,464],
            [750,464],
            [805,464],
            [855,464],
            [945,464 ],
            [970,464 ],
            [1020,464],
            [1060,464],
            [70,452 ],
            [80,452 ],
            [120,452],
            [160,452],
            [200,452],
            [240,452],
            [290,452],
            [350,452],
            [410,452],
            [470,452],
            [570,452],
            [670,452],
            [750,452],
            [805,452],
            [855,452],
            [945,452 ],
            [970,452 ],
            [1020,452],
            [1060,452],
            [70,440 ],
            [80,440 ],
            [120,440],
            [160,440],
            [200,440],
            [240,440],
            [290,440],
            [350,440],
            [410,440],
            [470,440],
            [570,440],
            [670,440],
            [750,440],
            [805,440],
            [855,440],
            [945,440 ],
            [970,440 ],
            [1020,440],
            [1060,440],
            [70,428 ],
            [80,428 ],
            [120,428],
            [160,428],
            [200,428],
            [240,428],
            [290,428],
            [350,428],
            [410,428],
            [470,428],
            [570,428],
            [670,428],
            [750,428],
            [805,428],
            [855,428],
            [945,428 ],
            [970,428 ],
            [1020,428],
            [1060,428],
            
            
        ]
        
        # Looping over json data with maximum 5 rows for HDD MB
        
        i=0
        # print(data[i])
        while(i<len(data) and i<12):
            if i==0:
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[0][0],dit_form_coordinates[0][1], "TCIL") # Name of MSI
                can.drawString(dit_form_coordinates[1][0],dit_form_coordinates[1][1], "1") # MB Book no
                can.drawString(dit_form_coordinates[2][0],dit_form_coordinates[2][1],"1")# Sheet No
                can.drawString(dit_form_coordinates[3][0],dit_form_coordinates[3][1],"GP")# POP type
                can.drawString(dit_form_coordinates[4][0],dit_form_coordinates[4][1],data[i][18]+"/"+data[i][20]+"/"+data[i][22])# Zone/mandal/GP Name
                # can.drawString(dit_form_coordinates[5][0],dit_form_coordinates[5][1],"")# Ring ID
                can.drawString(dit_form_coordinates[5][0],dit_form_coordinates[5][1],data[0][23]) # Span ID
                # can.drawString(dit_form_coordinates[7][0],dit_form_coordinates[7][1],"")# ABD Refernce
        
                can.drawString(dit_form_coordinates[6][0],dit_form_coordinates[6][1],'1')
                can.drawString(dit_form_coordinates[7][0],dit_form_coordinates[7][1],data[0][24])
                can.drawString(dit_form_coordinates[8][0],dit_form_coordinates[8][1],data[0][25])
                can.drawString(dit_form_coordinates[9][0],dit_form_coordinates[9][1],data[0][26])
                can.drawString(dit_form_coordinates[10][0],dit_form_coordinates[10][1],data[0][27])
                can.drawString(dit_form_coordinates[11][0],dit_form_coordinates[11][1],data[0][28])
                can.drawString(dit_form_coordinates[12][0],dit_form_coordinates[12][1],data[0][29])# Air Test Result
                can.drawString(dit_form_coordinates[13][0],dit_form_coordinates[13][1],data[0][30])# Sponge Test
                can.drawString(dit_form_coordinates[14][0],dit_form_coordinates[14][1],data[0][31])# Shuttle Test
                can.drawString(dit_form_coordinates[15][0],dit_form_coordinates[15][1],data[0][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[16][0],dit_form_coordinates[16][1],data[0][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[17][0],dit_form_coordinates[17][1],data[0][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[18][0],dit_form_coordinates[18][1],data[0][35])   # Drop in press
                can.drawString(dit_form_coordinates[19][0],dit_form_coordinates[19][1],data[0][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[0][42]+' / '+data[0][43]
                can.drawString(dit_form_coordinates[20][0],dit_form_coordinates[20][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[21][0],dit_form_coordinates[21][1],data[0][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[22][0],dit_form_coordinates[22][1],data[0][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[23][0],dit_form_coordinates[23][1],data[0][40])# Duct missing Len
                can.drawString(dit_form_coordinates[24][0],dit_form_coordinates[24][1],data[0][41])#Remarks
        
            if i==1:
                can.drawString(dit_form_coordinates[25][0],dit_form_coordinates[25][1],'2')
                can.drawString(dit_form_coordinates[26][0],dit_form_coordinates[26][1],  data[1][24])
                can.drawString(dit_form_coordinates[27][0],dit_form_coordinates[27][1],  data[1][25])
                can.drawString(dit_form_coordinates[28][0],dit_form_coordinates[28][1],  data[1][26])
                can.drawString(dit_form_coordinates[29][0],dit_form_coordinates[29][1],data[1][27])
                can.drawString(dit_form_coordinates[30][0],dit_form_coordinates[30][1],data[1][28])
                can.drawString(dit_form_coordinates[31][0],dit_form_coordinates[31][1],data[1][29])# Air Test Result
                can.drawString(dit_form_coordinates[32][0],dit_form_coordinates[32][1],data[1][30])# Sponge Test
                can.drawString(dit_form_coordinates[33][0],dit_form_coordinates[33][1],data[1][31])# Shuttle Test
                can.drawString(dit_form_coordinates[34][0],dit_form_coordinates[34][1],data[1][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[35][0],dit_form_coordinates[35][1],data[1][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[36][0],dit_form_coordinates[36][1],data[1][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[37][0],dit_form_coordinates[37][1],data[1][35])   # Drop in press
                can.drawString(dit_form_coordinates[38][0],dit_form_coordinates[38][1],data[1][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[1][42]+' / '+data[1][43]
                can.drawString(dit_form_coordinates[39][0],dit_form_coordinates[39][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[40][0],dit_form_coordinates[40][1],data[0][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[41][0],dit_form_coordinates[41][1],data[0][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[42][0],dit_form_coordinates[42][1],data[0][40])# Duct missing Len
                can.drawString(dit_form_coordinates[43][0],dit_form_coordinates[43][1],data[0][41])#Remarks
        
            if i==2:
                can.drawString(dit_form_coordinates[44][0],dit_form_coordinates[44][1],'3')
                can.drawString(dit_form_coordinates[45][0],dit_form_coordinates[45][1],data[2][24])
                can.drawString(dit_form_coordinates[46][0],dit_form_coordinates[46][1],data[2][25])
                can.drawString(dit_form_coordinates[47][0],dit_form_coordinates[47][1],data[2][26])
                can.drawString(dit_form_coordinates[48][0],dit_form_coordinates[48][1],data[2][27])
                can.drawString(dit_form_coordinates[49][0],dit_form_coordinates[49][1],data[2][28])
                can.drawString(dit_form_coordinates[50][0],dit_form_coordinates[50][1],data[2][29])# Air Test Result
                can.drawString(dit_form_coordinates[51][0],dit_form_coordinates[51][1],data[2][30])# Sponge Test
                can.drawString(dit_form_coordinates[52][0],dit_form_coordinates[52][1],data[2][31])# Shuttle Test
                can.drawString(dit_form_coordinates[53][0],dit_form_coordinates[53][1],data[2][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[54][0],dit_form_coordinates[54][1],data[2][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[55][0],dit_form_coordinates[55][1],data[2][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[56][0],dit_form_coordinates[56][1],data[2][35])   # Drop in press
                can.drawString(dit_form_coordinates[57][0],dit_form_coordinates[57][1],data[2][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[2][42]+' / '+data[2][43]
                can.drawString(dit_form_coordinates[58][0],dit_form_coordinates[58][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[59][0],dit_form_coordinates[59][1], data[2][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[60][0],dit_form_coordinates[60][1], data[2][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[61][0],dit_form_coordinates[61][1], data[2][40])# Duct missing Len
                can.drawString(dit_form_coordinates[62][0],dit_form_coordinates[62][1],data[2][41])#Remarks
        
            if i==3:
                can.drawString(dit_form_coordinates[63][0],dit_form_coordinates[63][1],'4')
                can.drawString(dit_form_coordinates[64][0],dit_form_coordinates[64][1],data[3][24])
                can.drawString(dit_form_coordinates[65][0],dit_form_coordinates[65][1],data[3][25])
                can.drawString(dit_form_coordinates[66][0],dit_form_coordinates[66][1],data[3][26])
                can.drawString(dit_form_coordinates[67][0],dit_form_coordinates[67][1],data[3][27])
                can.drawString(dit_form_coordinates[68][0],dit_form_coordinates[68][1],data[3][28])
                can.drawString(dit_form_coordinates[69][0],dit_form_coordinates[69][1],data[3][29])# Air Test Result
                can.drawString(dit_form_coordinates[70][0],dit_form_coordinates[70][1],data[3][30])# Sponge Test
                can.drawString(dit_form_coordinates[71][0],dit_form_coordinates[71][1],data[3][31])# Shuttle Test
                can.drawString(dit_form_coordinates[72][0],dit_form_coordinates[72][1],data[3][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[73][0],dit_form_coordinates[73][1],data[3][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[74][0],dit_form_coordinates[74][1],data[3][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[75][0],dit_form_coordinates[75][1],data[3][35])   # Drop in press
                can.drawString(dit_form_coordinates[76][0],dit_form_coordinates[76][1],data[3][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[3][42]+' / '+data[3][43]
                can.drawString(dit_form_coordinates[77][0],dit_form_coordinates[77][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[78][0],dit_form_coordinates[78][1],data[3][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[79][0],dit_form_coordinates[79][1],data[3][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[80][0],dit_form_coordinates[80][1],data[3][40])# Duct missing Len
                can.drawString(dit_form_coordinates[81][0],dit_form_coordinates[81][1],data[3][41])#Remarks
        
        
            if i==4:
                can.drawString(dit_form_coordinates[82][0],dit_form_coordinates[82][1],'5')
                can.drawString(dit_form_coordinates[83][0],dit_form_coordinates[83][1],  data[4][24])
                can.drawString(dit_form_coordinates[84][0],dit_form_coordinates[84][1],  data[4][25])
                can.drawString(dit_form_coordinates[85][0],dit_form_coordinates[85][1],  data[4][26])
                can.drawString(dit_form_coordinates[86][0],dit_form_coordinates[86][1],data[4][27])
                can.drawString(dit_form_coordinates[87][0],dit_form_coordinates[87][1],data[4][28])
                can.drawString(dit_form_coordinates[88][0],dit_form_coordinates[88][1],data[4][29])# Air Test Result
                can.drawString(dit_form_coordinates[89][0],dit_form_coordinates[89][1],data[4][30])# Sponge Test
                can.drawString(dit_form_coordinates[90][0],dit_form_coordinates[90][1],data[4][31])# Shuttle Test
                can.drawString(dit_form_coordinates[91][0],dit_form_coordinates[91][1],data[4][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[92][0],dit_form_coordinates[92][1],data[4][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[93][0],dit_form_coordinates[93][1],data[4][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[94][0],dit_form_coordinates[94][1],data[4][35])   # Drop in press
                can.drawString(dit_form_coordinates[95][0],dit_form_coordinates[95][1],data[4][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[4][42]+' / '+data[4][43]
                can.drawString(dit_form_coordinates[96][0],dit_form_coordinates[96][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[97][0],dit_form_coordinates[97][1],data[4][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[98][0],dit_form_coordinates[98][1],data[4][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[99][0],dit_form_coordinates[99][1],data[4][40])# Duct missing Len
                can.drawString(dit_form_coordinates[100][0],dit_form_coordinates[100][1],data[4][41])#Remarks
            if i==5:
                can.drawString(dit_form_coordinates[101][0],dit_form_coordinates[101][1],'6')
                can.drawString(dit_form_coordinates[102][0],dit_form_coordinates[102][1],  data[5][24])
                can.drawString(dit_form_coordinates[103][0],dit_form_coordinates[103][1],  data[5][25])
                can.drawString(dit_form_coordinates[104][0],dit_form_coordinates[104][1],  data[5][26])
                can.drawString(dit_form_coordinates[105][0],dit_form_coordinates[105][1],data[5][27])
                can.drawString(dit_form_coordinates[106][0],dit_form_coordinates[106][1],data[5][28])
                can.drawString(dit_form_coordinates[107][0],dit_form_coordinates[107][1],data[5][29])# Air Test Result
                can.drawString(dit_form_coordinates[108][0],dit_form_coordinates[108][1],data[5][30])# Sponge Test
                can.drawString(dit_form_coordinates[109][0],dit_form_coordinates[109][1],data[5][31])# Shuttle Test
                can.drawString(dit_form_coordinates[110][0],dit_form_coordinates[110][1],data[5][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[111][0],dit_form_coordinates[111][1],data[5][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[112][0],dit_form_coordinates[112][1],data[5][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[113][0],dit_form_coordinates[113][1],data[5][35])   # Drop in press
                can.drawString(dit_form_coordinates[114][0],dit_form_coordinates[114][1],data[5][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[5][42]+' / '+data[5][43]
                can.drawString(dit_form_coordinates[115][0],dit_form_coordinates[115][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[116][0],dit_form_coordinates[116][1],data[5][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[117][0],dit_form_coordinates[117][1],data[5][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[118][0],dit_form_coordinates[118][1],data[5][40])# Duct missing Len
                can.drawString(dit_form_coordinates[119][0],dit_form_coordinates[119][1],data[5][41])#Remarks
            if i==6:
                can.drawString(dit_form_coordinates[120][0],dit_form_coordinates[120][1],'7')
                can.drawString(dit_form_coordinates[121][0],dit_form_coordinates[121][1],data[6][24])
                can.drawString(dit_form_coordinates[122][0],dit_form_coordinates[122][1],data[6][25])
                can.drawString(dit_form_coordinates[123][0],dit_form_coordinates[123][1],data[6][26])
                can.drawString(dit_form_coordinates[124][0],dit_form_coordinates[124][1],data[6][27])
                can.drawString(dit_form_coordinates[125][0],dit_form_coordinates[125][1],data[6][28])
                can.drawString(dit_form_coordinates[126][0],dit_form_coordinates[126][1],data[6][29])# Air Test Result
                can.drawString(dit_form_coordinates[127][0],dit_form_coordinates[127][1],data[6][30])# Sponge Test
                can.drawString(dit_form_coordinates[128][0],dit_form_coordinates[128][1],data[6][31])# Shuttle Test
                can.drawString(dit_form_coordinates[129][0],dit_form_coordinates[129][1],data[6][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[130][0],dit_form_coordinates[130][1],data[6][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[131][0],dit_form_coordinates[131][1],data[6][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[132][0],dit_form_coordinates[132][1],data[6][35])   # Drop in press
                can.drawString(dit_form_coordinates[133][0],dit_form_coordinates[133][1],data[6][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[6][42]+' / '+data[6][43]
                can.drawString(dit_form_coordinates[134][0],dit_form_coordinates[134][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[135][0],dit_form_coordinates[135][1],data[6][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[136][0],dit_form_coordinates[136][1],data[6][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[137][0],dit_form_coordinates[137][1],data[6][40])# Duct missing Len
                can.drawString(dit_form_coordinates[138][0],dit_form_coordinates[138][1],data[6][41])#Remarks
            if i==7:
                can.drawString(dit_form_coordinates[139][0],dit_form_coordinates[139][1],'8')
                can.drawString(dit_form_coordinates[140][0],dit_form_coordinates[140][1],  data[7][24])
                can.drawString(dit_form_coordinates[141][0],dit_form_coordinates[141][1],  data[7][25])
                can.drawString(dit_form_coordinates[142][0],dit_form_coordinates[142][1],  data[7][26])
                can.drawString(dit_form_coordinates[143][0],dit_form_coordinates[143][1],data[7][27])
                can.drawString(dit_form_coordinates[144][0],dit_form_coordinates[144][1],data[7][28])
                can.drawString(dit_form_coordinates[145][0],dit_form_coordinates[145][1],data[7][29])# Air Test Result
                can.drawString(dit_form_coordinates[146][0],dit_form_coordinates[146][1],data[7][30])# Sponge Test
                can.drawString(dit_form_coordinates[147][0],dit_form_coordinates[147][1],data[7][31])# Shuttle Test
                can.drawString(dit_form_coordinates[148][0],dit_form_coordinates[148][1],data[7][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[149][0],dit_form_coordinates[149][1],data[7][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[150][0],dit_form_coordinates[150][1],data[7][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[151][0],dit_form_coordinates[151][1],data[7][35])   # Drop in press
                can.drawString(dit_form_coordinates[152][0],dit_form_coordinates[152][1],data[7][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[7][42]+' / '+data[7][43]
                can.drawString(dit_form_coordinates[153][0],dit_form_coordinates[153][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[154][0],dit_form_coordinates[40][1],data[7][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[155][0],dit_form_coordinates[41][1],data[7][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[156][0],dit_form_coordinates[42][1],data[7][40])# Duct missing Len
                can.drawString(dit_form_coordinates[157][0],dit_form_coordinates[43][1],data[7][41])#Remarks
            if i==8:
                can.drawString(dit_form_coordinates[158][0],dit_form_coordinates[158][1],'9')
                can.drawString(dit_form_coordinates[159][0],dit_form_coordinates[159][1],  data[8][24])
                can.drawString(dit_form_coordinates[160][0],dit_form_coordinates[160][1],  data[8][25])
                can.drawString(dit_form_coordinates[161][0],dit_form_coordinates[161][1],  data[8][26])
                can.drawString(dit_form_coordinates[162][0],dit_form_coordinates[162][1],data[8][27])
                can.drawString(dit_form_coordinates[163][0],dit_form_coordinates[163][1],data[8][28])
                can.drawString(dit_form_coordinates[164][0],dit_form_coordinates[164][1],data[8][29])# Air Test Result
                can.drawString(dit_form_coordinates[165][0],dit_form_coordinates[165][1],data[8][30])# Sponge Test
                can.drawString(dit_form_coordinates[166][0],dit_form_coordinates[166][1],data[8][31])# Shuttle Test
                can.drawString(dit_form_coordinates[167][0],dit_form_coordinates[167][1],data[8][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[168][0],dit_form_coordinates[168][1],data[8][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[169][0],dit_form_coordinates[169][1],data[8][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[170][0],dit_form_coordinates[170][1],data[8][35])   # Drop in press
                can.drawString(dit_form_coordinates[171][0],dit_form_coordinates[171][1],data[8][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[8][42]+' / '+data[8][43]
                can.drawString(dit_form_coordinates[172][0],dit_form_coordinates[172][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[173][0],dit_form_coordinates[173][1],data[8][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[174][0],dit_form_coordinates[174][1],data[8][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[175][0],dit_form_coordinates[175][1],data[8][40])# Duct missing Len
                can.drawString(dit_form_coordinates[176][0],dit_form_coordinates[176][1],data[8][41])#Remarks
            if i==9:
                can.drawString(dit_form_coordinates[177][0],dit_form_coordinates[177][1],'10')
                can.drawString(dit_form_coordinates[178][0],dit_form_coordinates[178][1],  data[9][24])
                can.drawString(dit_form_coordinates[179][0],dit_form_coordinates[179][1],  data[9][25])
                can.drawString(dit_form_coordinates[180][0],dit_form_coordinates[180][1],  data[9][26])
                can.drawString(dit_form_coordinates[181][0],dit_form_coordinates[181][1],data[9][27])
                can.drawString(dit_form_coordinates[182][0],dit_form_coordinates[182][1],data[9][28])
                can.drawString(dit_form_coordinates[183][0],dit_form_coordinates[183][1],data[9][29])# Air Test Result
                can.drawString(dit_form_coordinates[184][0],dit_form_coordinates[184][1],data[9][30])# Sponge Test
                can.drawString(dit_form_coordinates[185][0],dit_form_coordinates[185][1],data[9][31])# Shuttle Test
                can.drawString(dit_form_coordinates[186][0],dit_form_coordinates[186][1],data[9][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[187][0],dit_form_coordinates[187][1],data[9][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[188][0],dit_form_coordinates[188][1],data[9][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[189][0],dit_form_coordinates[189][1],data[9][35])   # Drop in press
                can.drawString(dit_form_coordinates[190][0],dit_form_coordinates[190][1],data[9][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[9][42]+' / '+data[9][43]
                can.drawString(dit_form_coordinates[191][0],dit_form_coordinates[191][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[192][0],dit_form_coordinates[192][1],data[9][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[193][0],dit_form_coordinates[193][1],data[9][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[194][0],dit_form_coordinates[194][1],data[9][40])# Duct missing Len
                can.drawString(dit_form_coordinates[195][0],dit_form_coordinates[195][1],data[9][41])#Remarks
            if i==10:
                can.drawString(dit_form_coordinates[196][0],dit_form_coordinates[196][1],'11')
                can.drawString(dit_form_coordinates[197][0],dit_form_coordinates[197][1],  data[10][24])
                can.drawString(dit_form_coordinates[198][0],dit_form_coordinates[198][1],  data[10][25])
                can.drawString(dit_form_coordinates[199][0],dit_form_coordinates[199][1],  data[10][26])
                can.drawString(dit_form_coordinates[200][0],dit_form_coordinates[200][1],data[10][27])
                can.drawString(dit_form_coordinates[201][0],dit_form_coordinates[201][1],data[10][28])
                can.drawString(dit_form_coordinates[202][0],dit_form_coordinates[202][1],data[10][29])# Air Test Result
                can.drawString(dit_form_coordinates[203][0],dit_form_coordinates[203][1],data[10][30])# Sponge Test
                can.drawString(dit_form_coordinates[204][0],dit_form_coordinates[204][1],data[10][31])# Shuttle Test
                can.drawString(dit_form_coordinates[205][0],dit_form_coordinates[205][1],data[10][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[206][0],dit_form_coordinates[206][1],data[10][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[207][0],dit_form_coordinates[207][1],data[10][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[208][0],dit_form_coordinates[208][1],data[10][35])   # Drop in press
                can.drawString(dit_form_coordinates[209][0],dit_form_coordinates[209][1],data[10][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[10][42]+' / '+data[10][43]
                can.drawString(dit_form_coordinates[210][0],dit_form_coordinates[210][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[211][0],dit_form_coordinates[211][1],data[10][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[212][0],dit_form_coordinates[212][1],data[10][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[213][0],dit_form_coordinates[213][1],data[10][40])# Duct missing Len
                can.drawString(dit_form_coordinates[214][0],dit_form_coordinates[214][1],data[10][41])#Remarks
            if i==11:
                can.drawString(dit_form_coordinates[215][0],dit_form_coordinates[215][1],'12')
                can.drawString(dit_form_coordinates[216][0],dit_form_coordinates[216][1],  data[11][24])
                can.drawString(dit_form_coordinates[217][0],dit_form_coordinates[217][1],  data[11][25])
                can.drawString(dit_form_coordinates[218][0],dit_form_coordinates[218][1],  data[11][26])
                can.drawString(dit_form_coordinates[219][0],dit_form_coordinates[219][1],data[11][27])
                can.drawString(dit_form_coordinates[220][0],dit_form_coordinates[220][1],data[11][28])
                can.drawString(dit_form_coordinates[221][0],dit_form_coordinates[221][1],data[11][29])# Air Test Result
                can.drawString(dit_form_coordinates[222][0],dit_form_coordinates[222][1],data[11][30])# Sponge Test
                can.drawString(dit_form_coordinates[223][0],dit_form_coordinates[223][1],data[11][31])# Shuttle Test
                can.drawString(dit_form_coordinates[224][0],dit_form_coordinates[224][1],data[11][32])   # Press applies 5bar 30min
                can.drawString(dit_form_coordinates[225][0],dit_form_coordinates[225][1],data[11][33])   #Press applies 10bar 30min
                can.drawString(dit_form_coordinates[226][0],dit_form_coordinates[226][1],data[11][34])   # Press obs after 10/30 min
                can.drawString(dit_form_coordinates[227][0],dit_form_coordinates[227][1],data[11][35])   # Drop in press
                can.drawString(dit_form_coordinates[228][0],dit_form_coordinates[228][1],data[11][36])# Test REs
                can.setFont('Helvetica-Bold',7)
                cell=data[11][42]+' / '+data[11][43]
                can.drawString(dit_form_coordinates[229][0],dit_form_coordinates[229][1],cell)#Loc of coupler
                
                can.setFont('Helvetica-Bold',10)
                can.drawString(dit_form_coordinates[230][0],dit_form_coordinates[230][1],data[11][38])# MB Duct Missing from
                can.drawString(dit_form_coordinates[231][0],dit_form_coordinates[231][1],data[11][39])# MB Duct Missing To
                can.drawString(dit_form_coordinates[232][0],dit_form_coordinates[232][1],data[11][40])# Duct missing Len
                can.drawString(dit_form_coordinates[233][0],dit_form_coordinates[233][1],data[11][41])#Remarks

            i+=1
        
        
        
        
        
        # # Coordinates
        
        
        can.save()
        
        #move to the beginning of the StringIO buffer
        packet.seek(0)
        
        # create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        cwd=os.getcwd()
        directory='AT_Report/R09-Duct Integrity Test REPORT.pdf'
        path = os.path.join(cwd, directory)
        existing_pdf = PdfFileReader(open(path, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        d="destination"
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y_%m_%d_%H_%M_%S') # this time will be filename
        ind_time=str(ind_time)
        final_directory="Output\PDF/"+ind_time+self.span_id+".pdf"
        final_path=os.path.join(cwd, final_directory)
        outputStream = open(final_path, "wb")
        output.write(outputStream)
        outputStream.close()
        return ind_time        

# def create_connection(db_file):
    # """ create a database connection to the SQLite database
    #     specified by the db_file
    # :param db_file: database file
    # :return: Connection object or None
    # """
    # conn = None
    # try:
    #     conn = sqlite3.connect(db_file)
    # except Error as e:
    #     print(e)

    # return conn

# def make_pdf(data):
    ## Initialising Canvas
    #packet = io.BytesIO()
    #can = canvas.Canvas(packet, pagesize=letter)
    ## print(len(data))
    #hdd_form_coordinates=[[298, 505],[298, 490],[298,476],[298,462],[298,448],[298,434],[298,422],[298,408],
    #[55,350],[120,350],[210,350],[250,350],[300,350],[360,350],[450,350],[540,350],[630,350],[700,350],
    #[55,337],[120,337],[210,337],[250,337],[300,337],[360,337],[450,337],[540,337],[630,337],[700,337],
    #[55,323],[120,323],[210,323],[250,323],[300,323],[360,323],[450,323],[540,323],[630,323],[700,323],
    #[55,310],[120,310],[210,310],[250,310],[300,310],[360,310],[450,310],[540,310],[630,310],[700,310],
    #[55,296],[120,296],[210,296],[250,296],[300,296],[360,296],[450,296],[540,296],[630,296],[700,296],
    #[120,236],[250,236],[540,236],[700,236],[120,222],[250,222],[540,222],[700,222],[120,208],[250,208],
    #[540,208],[700,208],[120,194],[250,194],[540,194],[700,194],[120,180],[250,180],[540,180],[700,180]]
    #
    ## Looping over json data with maximum 5 rows for HDD MB
    #
    #i=0
    ## print(data[i])
    #while(i<len(data) and i<5):
    #    if i==0:
    #        can.drawString(hdd_form_coordinates[0][0],hdd_form_coordinates[0][1], "TCIL") # Name of MSI
    #        can.drawString(hdd_form_coordinates[1][0],hdd_form_coordinates[1][1], "1") # MB Book no
    #        can.drawString(hdd_form_coordinates[2][0],hdd_form_coordinates[2][1],"1")# Sheet No
    #        can.drawString(hdd_form_coordinates[3][0],hdd_form_coordinates[3][1],"GP")# POP type
    #        can.drawString(hdd_form_coordinates[4][0],hdd_form_coordinates[4][1],data[i][18]+"/"+data[i][20]+"/"+data[i][23])# Zone/mandal/GP Name
    #        can.drawString(hdd_form_coordinates[5][0],hdd_form_coordinates[5][1],"")# Ring ID
    #        can.drawString(hdd_form_coordinates[6][0],hdd_form_coordinates[6][1],data[0][21]) # Span ID
    #        can.drawString(hdd_form_coordinates[7][0],hdd_form_coordinates[7][1],"")# ABD Refernce
    #
    #        can.drawString(hdd_form_coordinates[8][0],hdd_form_coordinates[8][1],"1")# Sr no
    #        can.drawString(hdd_form_coordinates[9][0],hdd_form_coordinates[9][1],data[i][24])# Side of road
    #        can.drawString(hdd_form_coordinates[10][0],hdd_form_coordinates[10][1],data[i][25])# Pit ch from
    #        can.drawString(hdd_form_coordinates[11][0],hdd_form_coordinates[11][1],data[i][26])# ch to
    #        can.drawString(hdd_form_coordinates[12][0],hdd_form_coordinates[12][1],data[i][27])# len
    #        can.drawString(hdd_form_coordinates[13][0],hdd_form_coordinates[13][1],data[i][28])# gr as build made
    #        can.drawString(hdd_form_coordinates[14][0],hdd_form_coordinates[14][1],data[i][29])# depth
    #        can.drawString(hdd_form_coordinates[15][0],hdd_form_coordinates[15][1],data[i][30])#dia
    #        can.drawString(hdd_form_coordinates[16][0],hdd_form_coordinates[16][1],data[i][31])# duct
    #        can.drawString(hdd_form_coordinates[17][0],hdd_form_coordinates[17][1],str(data[i][32]))# remark
    #
    #        can.drawString(hdd_form_coordinates[58][0],hdd_form_coordinates[58][1],str(data[i][33]))# start lat
    #        can.drawString(hdd_form_coordinates[59][0],hdd_form_coordinates[59][1],str(data[i][34]))# start long
    #        can.drawString(hdd_form_coordinates[60][0],hdd_form_coordinates[60][1],str(data[i][35]))# end lat
    #        can.drawString(hdd_form_coordinates[61][0],hdd_form_coordinates[61][1],str(data[i][36]))# end long
    #
    #    if i==1:
    #        can.drawString(hdd_form_coordinates[18][0],hdd_form_coordinates[18][1],"2")
    #        can.drawString(hdd_form_coordinates[19][0],hdd_form_coordinates[19][1],data[i][24])
    #        can.drawString(hdd_form_coordinates[20][0],hdd_form_coordinates[20][1],data[i][25])# Pit ch from
    #        can.drawString(hdd_form_coordinates[21][0],hdd_form_coordinates[21][1],data[i][26])# ch to
    #        can.drawString(hdd_form_coordinates[22][0],hdd_form_coordinates[22][1],data[i][27])# len
    #        can.drawString(hdd_form_coordinates[23][0],hdd_form_coordinates[23][1],data[i][28])# gr as build made
    #        can.drawString(hdd_form_coordinates[24][0],hdd_form_coordinates[24][1],data[i][29])# depth
    #        can.drawString(hdd_form_coordinates[25][0],hdd_form_coordinates[25][1],data[i][30])#dia
    #        can.drawString(hdd_form_coordinates[26][0],hdd_form_coordinates[26][1],data[i][31])# duct
    #        can.drawString(hdd_form_coordinates[27][0],hdd_form_coordinates[27][1],str(data[i][32]))# remark
    #
    #        can.drawString(hdd_form_coordinates[62][0],hdd_form_coordinates[62][1],str(data[i][33]))# start lat
    #        can.drawString(hdd_form_coordinates[63][0],hdd_form_coordinates[63][1],str(data[i][34]))# start long
    #        can.drawString(hdd_form_coordinates[64][0],hdd_form_coordinates[64][1],str(data[i][35]))# end lat
    #        can.drawString(hdd_form_coordinates[65][0],hdd_form_coordinates[65][1],str(data[i][36]))# end long
    #
    #    if i==2:
    #        can.drawString(hdd_form_coordinates[28][0],hdd_form_coordinates[28][1],"3")
    #        can.drawString(hdd_form_coordinates[29][0],hdd_form_coordinates[29][1],data[i][24])
    #        can.drawString(hdd_form_coordinates[30][0],hdd_form_coordinates[30][1],data[i][25])# Pit ch from
    #        can.drawString(hdd_form_coordinates[31][0],hdd_form_coordinates[31][1],data[i][26])# ch to
    #        can.drawString(hdd_form_coordinates[32][0],hdd_form_coordinates[32][1],data[i][27])# len
    #        can.drawString(hdd_form_coordinates[33][0],hdd_form_coordinates[33][1],data[i][28])# gr as build made
    #        can.drawString(hdd_form_coordinates[34][0],hdd_form_coordinates[34][1],data[i][29])# depth
    #        can.drawString(hdd_form_coordinates[35][0],hdd_form_coordinates[35][1],data[i][30])#dia
    #        can.drawString(hdd_form_coordinates[36][0],hdd_form_coordinates[36][1],data[i][31])# duct
    #        can.drawString(hdd_form_coordinates[37][0],hdd_form_coordinates[37][1],str(data[i][32]))# remark
    #
    #        can.drawString(hdd_form_coordinates[66][0],hdd_form_coordinates[66][1],str(data[i][33]))# start lat
    #        can.drawString(hdd_form_coordinates[67][0],hdd_form_coordinates[67][1],str(data[i][34]))# start long
    #        can.drawString(hdd_form_coordinates[68][0],hdd_form_coordinates[68][1],str(data[i][35]))# end lat
    #        can.drawString(hdd_form_coordinates[69][0],hdd_form_coordinates[69][1],str(data[i][36]))# end long
    #
    #    if i==3:
    #        can.drawString(hdd_form_coordinates[38][0],hdd_form_coordinates[38][1],"4")
    #        can.drawString(hdd_form_coordinates[39][0],hdd_form_coordinates[39][1],data[i][24])
    #        can.drawString(hdd_form_coordinates[40][0],hdd_form_coordinates[40][1],data[i][25])# Pit ch from
    #        can.drawString(hdd_form_coordinates[41][0],hdd_form_coordinates[41][1],data[i][26])# ch to
    #        can.drawString(hdd_form_coordinates[42][0],hdd_form_coordinates[42][1],data[i][27])# len
    #        can.drawString(hdd_form_coordinates[43][0],hdd_form_coordinates[43][1],data[i][28])# gr as build made
    #        can.drawString(hdd_form_coordinates[44][0],hdd_form_coordinates[44][1],data[i][29])# depth
    #        can.drawString(hdd_form_coordinates[45][0],hdd_form_coordinates[45][1],data[i][30])#dia
    #        can.drawString(hdd_form_coordinates[46][0],hdd_form_coordinates[46][1],data[i][31])# duct
    #        can.drawString(hdd_form_coordinates[47][0],hdd_form_coordinates[47][1],str(data[i][32]))# remark
    #
    #        can.drawString(hdd_form_coordinates[70][0],hdd_form_coordinates[70][1],str(data[i][33]))# start lat
    #        can.drawString(hdd_form_coordinates[71][0],hdd_form_coordinates[71][1],str(data[i][34]))# start long
    #        can.drawString(hdd_form_coordinates[72][0],hdd_form_coordinates[72][1],str(data[i][35]))# end lat
    #        can.drawString(hdd_form_coordinates[73][0],hdd_form_coordinates[73][1],str(data[i][36]))# end long
    #
    #
    #    if i==4:
    #        can.drawString(hdd_form_coordinates[48][0],hdd_form_coordinates[48][1],"5")
    #        can.drawString(hdd_form_coordinates[49][0],hdd_form_coordinates[49][1],data[i][24])
    #        can.drawString(hdd_form_coordinates[50][0],hdd_form_coordinates[50][1],data[i][25])# Pit ch from
    #        can.drawString(hdd_form_coordinates[51][0],hdd_form_coordinates[51][1],data[i][26])# ch to
    #        can.drawString(hdd_form_coordinates[52][0],hdd_form_coordinates[52][1],data[i][27])# len
    #        can.drawString(hdd_form_coordinates[53][0],hdd_form_coordinates[53][1],data[i][28])# gr as build made
    #        can.drawString(hdd_form_coordinates[54][0],hdd_form_coordinates[54][1],data[i][29])# depth
    #        can.drawString(hdd_form_coordinates[55][0],hdd_form_coordinates[55][1],data[i][30])#dia
    #        can.drawString(hdd_form_coordinates[56][0],hdd_form_coordinates[56][1],data[i][31])# duct
    #        can.drawString(hdd_form_coordinates[57][0],hdd_form_coordinates[57][1],str(data[i][32]))# remark
    #
    #        can.drawString(hdd_form_coordinates[74][0],hdd_form_coordinates[74][1],str(data[i][33]))# start lat
    #        can.drawString(hdd_form_coordinates[75][0],hdd_form_coordinates[75][1],str(data[i][34]))# start long
    #        can.drawString(hdd_form_coordinates[76][0],hdd_form_coordinates[76][1],str(data[i][35]))# end lat
    #        can.drawString(hdd_form_coordinates[77][0],hdd_form_coordinates[77][1],str(data[i][36]))# end long
    #    i+=1
    #
    #
    #
    #
    #
    ## # Coordinates
    #
    #
    #can.save()
    #
    ##move to the beginning of the StringIO buffer
    #packet.seek(0)
    #
    ## create a new PDF with Reportlab
    #new_pdf = PdfFileReader(packet)
    ## read your existing PDF
    #existing_pdf = PdfFileReader(open(r"C:\Users\parth.pandey\Desktop\Field Force Forms\AT_Report/R08-HDD REPORT.pdf", "rb"))
    #output = PdfFileWriter()
    ## add the "watermark" (which is the new pdf) on the existing page
    #page = existing_pdf.getPage(0)
    #page.mergePage(new_pdf.getPage(0))
    #output.addPage(page)
    ## finally, write "output" to a real file
    #d="destination"
    #outputStream = open(r"C:\Users\parth.pandey\Desktop\Field Force Forms\Output/"+ind_time+".pdf", "wb")
    #output.write(outputStream)
    #outputStream.close()



def query_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    form=input("Form- ")
    prikey=int(input("Prikey- "))

    cur = conn.cursor()
    zone_name='Warangal'
    command="SELECT * FROM hdd WHERE span_id = \'"+span_id+"\' AND prikey >="+ str(prikey)
    cur.execute(command)
    
    
    rows = cur.fetchall()
    if len(rows)==0:
        print('Nothing to Show')
    else:
        make_pdf(rows)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


# def main():
    #  database = r"data.db"

    # create a database connection
    # conn = create_connection(database)
    # with conn:
    #     print("1. Query task by priority:")
    #     # select_task_by_priority(conn, 1)

    #     print("2. Query all tasks")
    # select_all_tasks(conn)
    # print(conn)


# if __name__ == '__main__':
#     main()


