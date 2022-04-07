
from edit_pdf import Create_connection, HDD_form, DIT_form
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms import SelectField
from edit_excel import Create_connection_xl, HDD_form_xl
from load_data import Load
from flask import send_file
import os

# database = r"data.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY']='S_U_perS3crEt_KEY#01287'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class hdd(db.Model):
    index=db.Column(db.Integer)
    prikey=db.Column(db.Integer,primary_key=True)
    Key=db.Column(db.Text)
    SurveyDuration=db.Column(db.Text)
    User=db.Column(db.Text)
    UploadTime=db.Column(db.Text)
    SurveyName=db.Column(db.Text)
    _scheduled_start=db.Column(db.Text)
    Version=db.Column(db.Text)
    Complete=db.Column(db.Text)
    SurveyNotes=db.Column(db.Text)
    LocationTrigger=db.Column(db.Text)
    InstanceName=db.Column(db.Text)
    start=db.Column(db.Text)
    end=db.Column(db.Text)
    deviceid=db.Column(db.Text)
    uuid=db.Column(db.Text)
    Package_Name=db.Column(db.Text)
    Zone_Name=db.Column(db.Text)
    District_Name=db.Column(db.Text)
    Mandal_Name=db.Column(db.Text)
    Span_ID=db.Column(db.Text)
    From_GP=db.Column(db.Text)
    To_GP=db.Column(db.Text)
    Side_of_the_road=db.Column(db.Text)
    Chainage_From=db.Column(db.Text)
    Chainage_To=db.Column(db.Text)
    Length=db.Column(db.Text)
    Graph_as_built_made=db.Column(db.Text)
    Depth=db.Column(db.Text)
    Bore_reamer_diameter=db.Column(db.Text)
    Ducts=db.Column(db.Text)
    Remark=db.Column(db.Text)
    start_lat=db.Column(db.Text)
    start_long=db.Column(db.Text)
    end_lat=db.Column(db.Text)
    end_long=db.Column(db.Text)

class blowing(db.Model):
    index=db.Column(db.Integer)
    prikey=db.Column(db.Integer,primary_key=True)
    Key=db.Column(db.Text)
    SurveyDuration=db.Column(db.Text)
    User=db.Column(db.Text)
    UploadTime=db.Column(db.Text)
    SurveyName=db.Column(db.Text)
    _scheduled_start=db.Column(db.Text)
    Version=db.Column(db.Text)
    Complete=db.Column(db.Text)
    SurveyNotes=db.Column(db.Text)
    LocationTrigger=db.Column(db.Text)
    InstanceName=db.Column(db.Text)
    start=db.Column(db.Text)
    end=db.Column(db.Text)
    deviceid=db.Column(db.Text)
    uuid=db.Column(db.Text)
    Package_Name=db.Column(db.Text)
    Zone_Name=db.Column(db.Text)
    District_Name=db.Column(db.Text)
    Mandal_Name=db.Column(db.Text)
    Span_ID=db.Column(db.Text)
    From_GP=db.Column(db.Text)
    To_GP=db.Column(db.Text)
    Chainage_From=db.Column(db.Text)
    Chainage_To=db.Column(db.Text)
    Length=db.Column(db.Text)
    chamber_from=db.Column(db.Text)
    chamber_to=db.Column(db.Text)
    size_of_ofc=db.Column(db.Text)
    ofc_cable_id=db.Column(db.Text)
    cable_len_start=db.Column(db.Text)
    cable_len_end=db.Column(db.Text)
    Total_cable_length=db.Column(db.Text)
    chamber_a_end_reading=db.Column(db.Text)
    chamber_a_entry_reading=db.Column(db.Text)
    chamber_a_end_slack_loop_length=db.Column(db.Text)
    chamber_b_entry_reading=db.Column(db.Text)
    chamber_b_end_reading=db.Column(db.Text)
    chamber_b_end_slack_loop_length=db.Column(db.Text)
    Remarks=db.Column(db.Text)

class dit(db.Model):
    index=db.Column(db.Integer)
    prikey=db.Column(db.Integer,primary_key=True)
    Key=db.Column(db.Text)
    SurveyDuration=db.Column(db.Text)
    User=db.Column(db.Text)
    UploadTime=db.Column(db.Text)
    SurveyName=db.Column(db.Text)
    _scheduled_start=db.Column(db.Text)
    Version=db.Column(db.Text)
    Complete=db.Column(db.Text)
    SurveyNotes=db.Column(db.Text)
    LocationTrigger=db.Column(db.Text)
    InstanceName=db.Column(db.Text)
    start=db.Column(db.Text)
    end=db.Column(db.Text)
    deviceid=db.Column(db.Text)
    uuid=db.Column(db.Text)
    Package_Name=db.Column(db.Text)
    Zone_Name=db.Column(db.Text)
    District_Name=db.Column(db.Text)
    Mandal_Name=db.Column(db.Text)
    Span_ID=db.Column(db.Text)
    From_GP=db.Column(db.Text)
    To_GP=db.Column(db.Text)
    Chainage_From=db.Column(db.Text)
    Chainage_To=db.Column(db.Text)
    Chamber_From=db.Column(db.Text)
    Chamber_To=db.Column(db.Text)
    DuctLength=db.Column(db.Text)
    Air_test_Result=db.Column(db.Text)
    Sponge_test_result=db.Column(db.Text)
    Shuttle_test_result=db.Column(db.Text)
    Pressure_test_5_bar_30_min=db.Column(db.Text)
    Pressure_test_10_bar_10_min=db.Column(db.Text)
    Pressure_obs_10_30_min=db.Column(db.Text)
    Pressure_test_drop_in_pressure=db.Column(db.Text)
    test_result=db.Column(db.Text)
    Location=db.Column(db.Text)
    mb_duct_missing_sec_from=db.Column(db.Text)
    mb_duct_missing_sec_to=db.Column(db.Text)
    mb_duct_missing_section_length=db.Column(db.Text)
    remarks=db.Column(db.Text)
    coupler_lat=db.Column(db.Text)
    coupler_long=db.Column(db.Text)

class drt(db.Model):
    index=db.Column(db.Integer)
    prikey=db.Column(db.Integer,primary_key=True)
    Key=db.Column(db.Text)
    SurveyDuration=db.Column(db.Text)
    User=db.Column(db.Text)
    UploadTime=db.Column(db.Text)
    SurveyName=db.Column(db.Text)
    _scheduled_start=db.Column(db.Text)
    Version=db.Column(db.Text)
    Complete=db.Column(db.Text)
    SurveyNotes=db.Column(db.Text)
    LocationTrigger=db.Column(db.Text)
    InstanceName=db.Column(db.Text)
    start=db.Column(db.Text)
    end=db.Column(db.Text)
    deviceid=db.Column(db.Text)
    uuid=db.Column(db.Text)
    Package_Name=db.Column(db.Text)
    Zone_Name=db.Column(db.Text)
    District_Name=db.Column(db.Text)
    Mandal_Name=db.Column(db.Text)
    Span_ID=db.Column(db.Text)
    From_GP=db.Column(db.Text)
    To_GP=db.Column(db.Text)
    Chamber1_Location=db.Column(db.Text)
    Chamber1_condition=db.Column(db.Text)
    Chamber1_route_marker=db.Column(db.Text)
    Chamber2_Location=db.Column(db.Text)
    Chamber2_condition=db.Column(db.Text)
    Chambe2_route_marker=db.Column(db.Text)
    ch_from=db.Column(db.Text)
    ch_to=db.Column(db.Text)
    Length=db.Column(db.Text)
    Duct_dam_punct_loc=db.Column(db.Text)
    Duct_dam_punct_loc_ch_from=db.Column(db.Text)
    Duct_dam_punct_loc_ch_to=db.Column(db.Text)
    Duct_dam_punct_loc_Length=db.Column(db.Text)
    Duct_miss_loc=db.Column(db.Text)
    Duct_miss_ch_from=db.Column(db.Text)
    Duct_miss_ch_to=db.Column(db.Text)
    Duct_dam_punct_loc_Length=db.Column(db.Text)
    Duct_miss_loc=db.Column(db.Text)
    Duct_miss_ch_from=db.Column(db.Text)
    Duct_miss_ch_to=db.Column(db.Text)
    Duct_miss_ch_Length=db.Column(db.Text)
    Remark=db.Column(db.Text)
    chamber1_lat=db.Column(db.Text)
    chamber1_long=db.Column(db.Text)
    chamber2_lat=db.Column(db.Text)
    chamber2_long=db.Column(db.Text)
    Duct_dam_punct_lat=db.Column(db.Text)
    Duct_dam_punct_long=db.Column(db.Text)
    Duct_miss_lat=db.Column(db.Text)
    Duct_miss_long=db.Column(db.Text)

class tnd(db.Model):
    index=db.Column(db.Integer)
    prikey=db.Column(db.Integer,primary_key=True)
    Key=db.Column(db.Text)
    SurveyDuration=db.Column(db.Text)
    User=db.Column(db.Text)
    UploadTime=db.Column(db.Text)
    SurveyName=db.Column(db.Text)
    _scheduled_start=db.Column(db.Text)
    Version=db.Column(db.Text)
    Complete=db.Column(db.Text)
    SurveyNotes=db.Column(db.Text)
    LocationTrigger=db.Column(db.Text)
    InstanceName=db.Column(db.Text)
    start=db.Column(db.Text)
    end=db.Column(db.Text)
    deviceid=db.Column(db.Text)
    uuid=db.Column(db.Text)
    Package_Name=db.Column(db.Text)
    Zone_Name=db.Column(db.Text)
    District_Name=db.Column(db.Text)
    Mandal_Name=db.Column(db.Text)
    Span_ID=db.Column(db.Text)
    From_GP=db.Column(db.Text)
    To_GP=db.Column(db.Text)
    Chainage_From=db.Column(db.Text)
    Chainage_To=db.Column(db.Text)
    Length=db.Column(db.Text)
    Location=db.Column(db.Text)
    Offset=db.Column(db.Text)
    Depth=db.Column(db.Text)
    Trench_Side=db.Column(db.Text)
    Duct_Laid=db.Column(db.Text)
    Method_Execution=db.Column(db.Text)
    Crossing=db.Column(db.Text)
    Strata_Type=db.Column(db.Text)
    Protection=db.Column(db.Text)
    Protect_Dwc=db.Column(db.Text)
    Protect_Gi=db.Column(db.Text)
    Protect_Rcc=db.Column(db.Text)
    Protect_Pcc=db.Column(db.Text)
    Rcc_Chamber=db.Column(db.Text)
    Rcc_Marker=db.Column(db.Text)
    Remark=db.Column(db.Text)
    from_loc_lat=db.Column(db.Text)
    from_loc_long=db.Column(db.Text)
    to_loc_lat=db.Column(db.Text)
    to_loc_long=db.Column(db.Text)
    

# q=hdd.query.filter_by(index=1.0896).first()
# print(q.end_lat)
# x=db.session.query.filter_by(prikey=1)
# print(x)

@app.route("/",methods=['POST','GET']) # What will be there in home page
def index():
    if request.method=='POST':
        pass
        # span_data= request.form['form1'] # In index.html we have made form's input name-> content
        # print(span_data) # Todo class making a new_task
 
    else:
         # In Todo class database ordering using date
        return render_template('dynamicdrop.html')

@app.route("/load_data",methods=['POST','GET']) # What will be there in home page
def load_Data():
    Load.load_database()
    return render_template('load_data.html')

@app.route("/query",methods=['POST','GET'])
def query():
    
    if request.method=='GET':
        package=request.args['package']
        zone=request.args['zone']
        district=request.args['district']
        mandal = request.args['mandal']
        from_gp=request.args['from_gp']
        to_gp=request.args['to_gp']

        span_id=request.args['span_id']
        form=request.args['form']
        # print(form)
        if form=='hdd':
            span_data=hdd.query.filter_by(Span_ID=span_id).all()
            form='HDD'
        elif form=='dit':
            span_data=dit.query.filter_by(Span_ID=span_id).all()
            form='DIT'
        elif form=='drt':
            span_data=drt.query.filter_by(Span_ID=span_id).all()
            form='DRT'
        elif form=='tnd':
            span_data=tnd.query.filter_by(Span_ID=span_id).all()
            form='T&D'
        elif form=='blowing':
            span_data=blowing.query.filter_by(Span_ID=span_id).all()
            form='Blowing'
        
        # span_data=hdd.query.filter_by(Span_ID=span_id).all()
        return  render_template('index.html',form=form,span_id=span_id,span_data=span_data)

    else:
        prikey=request.form['prikey']
        span_id=request.form['span_id']
        form=request.form['form']
        file_type=request.form['file_type']
        span_id=str(span_id)
        database = r"data.db"
        cwd=os.getcwd()
        if form=='HDD':
            if file_type=='pdf':
                create_conn=Create_connection(database)
                conn=create_conn.create_connection()
                hdd_conn=HDD_form(conn,form,span_id,prikey)
                date_time=hdd_conn.query_tasks()
                final_directory="Output\PDF/"+date_time+span_id+".pdf"
                path=os.path.join(cwd, final_directory)
                return send_file(path,as_attachment=True)
            elif file_type=='excel':
                create_conn=Create_connection_xl(database)
                conn=create_conn.create_connection()
                hdd_conn=HDD_form_xl(conn,form,span_id,prikey)
                date_time=hdd_conn.query_tasks()
                final_directory="Output\Excel/"+date_time+span_id+".xlsx"
                path=os.path.join(cwd, final_directory)
                return send_file(path,as_attachment=True)
        elif form=='DIT':
            if file_type=='pdf':
                create_conn=Create_connection(database)
                conn=create_conn.create_connection()
                hdd_conn=DIT_form(conn,form,span_id,prikey)
                date_time=hdd_conn.query_tasks()
                final_directory="Output\PDF/"+date_time+span_id+".pdf"
                path=os.path.join(cwd, final_directory)
                return send_file(path,as_attachment=True)
            elif file_type=='excel':
                create_conn=Create_connection_xl(database)
                conn=create_conn.create_connection()
                hdd_conn=HDD_form_xl(conn,form,span_id,prikey)
                date_time=hdd_conn.query_tasks()
                final_directory="Output\Excel/"+date_time+span_id+".xlsx"
                path=os.path.join(cwd, final_directory)
                return send_file(path,as_attachment=True)

# @app.route("/output", methods=['GET', 'POST'])
# def output():
#     if request.method=='POST':
#         prikey=request.form['prikey']
#         path=r"C:\Users\parth.pandey\Desktop\Field Force Forms\Output/2022_02_25_11_39_13.pdf"
#     return send_file(path)

if __name__ == '__main__':
    app.run(debug=True)

