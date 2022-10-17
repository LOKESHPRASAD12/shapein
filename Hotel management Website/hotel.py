from flask import Flask,render_template,flash,request,session
import pymysql
import os
import shutil
from PIL import Image
import random
import time
import sys 


app=Flask(__name__)
app.secret_key="super-secret-key"

@app.route("/",methods=['GET','POST'])

def homepage():
	return render_template('home.html')
	session.pop('user')


@app.route("/login_stu",methods=['GET','POST'])
def login_stu():
	return render_template("student_login.html")


@app.route("/buttons",methods=['GET','POST'])
def buttons():
	return render_template("buttons.html")



@app.route("/registration_stu",methods=['GET','POST'])
def registration_stu():
	return render_template("student_registration.html")



@app.route("/registration_student",methods=['GET','POST'])
def registration_student():
	if (request.method=='POST'):
		email1=request.form.get('email1')
		password1=request.form.get('password1')
		name1=request.form.get('name1')
		gen=request.form.get('gen')
		address1=request.form.get('address1')
		occupaton1=request.form.get('occupaton1')
		session['email']='email'




		if email1==""  or name1=="" or gen=="" or address1=="" or occupaton1=="" or password1=="":
			flash('Required all fields and correct field')
			return render_template("student_registration.html")

		elif len(password1)<8:
			flash('password must be atleast 8 characters')
			return render_template("student_registration.html")

		else:
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('select * from students_data')
			rows=cur.fetchall()
			flag=0
			for row in rows:
				if row[0]==email1:
					flag=1


		if flag==1:
			flash('Email already exist')
			return render_template("student_registration.html")
			con.close()
		else:
			cur.execute('insert into students_data values(%s,%s,%s,%s,%s,%s)',(email1,password1,name1,gen,address1,occupaton1))
						
						
			con.commit()
				
			con.close()
			
			flash('Success..... Record has been submitted')
			return render_template("student_login.html")
			session.pop('email')


			
@app.route("/login_student_validation",methods=['GET','POST'])
def login_student_validation():
	global email1,password1
	if (request.method=='POST'):
		email1=request.form.get('email')
		password1=request.form.get('password')	
			
		

	if email1=="" or password1=="":
		flash('All fields are Required')
		return render_template("student_login.html")

	else:
		
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute('select * from students_data')
		rows=cur.fetchall()
		flag=0
		for row in rows:
			if row[0]==email1 and row[1]==password1:
				flag=1
				
			elif row[0]==email1 and row[1]!=password1:
				flag=2


	if flag==1:
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute('select * from owner_info')
		result=cur.fetchall()
		i=random.randint(50000,1000000)
		j=i
		path='static/uploading/'

		if os.path.exists(path):
			shutil.rmtree(path)




		for row in result:
			if os.path.exists(path):
				path1=f'{path}/{i}.jpg'
				image=row[0]
				write_file(image,path1)
				i+=1
			else:
				os.makedirs(path)
				path1=f'{path}/{i}.jpg'
				image=row[0]
				write_file(image,path1)
				i+=1

		return render_template('student_home.html',result=result,enumerate=enumerate,num=j)
		


	elif flag==2:
		flash('Incorrect password')
		return render_template("student_login.html")
	else:
		flash('Email doesn\'t exist')
		return render_template("student_login.html")
	
	con.close()

		
	
@app.route("/logout_student")
def logout_student():
	return render_template("student_login.html")
	



@app.route("/login_owner",methods=['GET','POST'])
def login_owner():
	return render_template("owner_login.html")




@app.route("/registration_owner",methods=['GET','POST'])
def registration_owner():
	return render_template("owner_registration.html")



@app.route("/registration_owner_form",methods=['GET','POST'])
def registration_owner_form():
	if (request.method=='POST'):
		email1=request.form.get('email1')
		password1=request.form.get('password1')
		contact=request.form.get('contact')
		city=request.form.get('city')




		if email1=="" or password1==""  or  city=="" or len(contact)!=int(10):
			flash('Required all fields and correct field')
			return render_template("owner_registration.html")
		elif  len(password1)<8 :
			flash('Password must be atleast 8 characters')
			return render_template("owner_registration.html")
		else:
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('select * from owner_data')
			rows=cur.fetchall()
			flag=0
			for row in rows:
				if row[0]==email1:
					flag=1


		if flag==1:
			flash('Email already exist')
			return render_template("owner_registration.html")
			con.close()
		else:
			cur.execute('insert into owner_data values(%s,%s,%s,%s)',(email1,password1,contact,city))
						
						
			con.commit()
				
			con.close()
			flash('Success..... Record has been submitted')
			return render_template("buttons.html")




@app.route("/login_owner_validation",methods=['GET','POST'])
def login_owner_validation():
	if (request.method=='POST'):
		email1=request.form.get('email')
		password1=request.form.get('password')		
		

	if email1=="" or password1=="":
		flash('All fields are Required')
		return render_template("owner_login.html")

	else:
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute('select * from owner_data')
		rows=cur.fetchall()
		flag=0
		for row in rows:
			if row[0]==email1 and row[1]==password1:
				flag=1

			elif row[0]==email1 and row[1]!=password1:
				flag=2


	if flag==1:
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute('select * from owner_info')
		rows=cur.fetchall()
		for row in rows:
			if email1==row[9] :
				flag=3


		if flag==3:
			flash('your hotel already uploaded , please update or show')
			return render_template("owner_login.html")
		else:
			return render_template('owner_upload.html')




	elif flag==2:
		flash('Incorrect password')
		return render_template("owner_login.html")
	else:
		flash('Email doesn\'t exist')
		return render_template("owner_login.html")
	
	con.close()




# define a function for 
# compressing an image 
def compressMe(file, verbose = False): 
	
	  # Get the path of the file 
	filepath = os.path.join('static/upload/',  
                            file) 
	  
	# open the image 
	picture = Image.open(filepath).convert('RGB') 
	  
	# Save the picture with desired quality 
	# To change the quality of image, 
	# set the quality variable at 
	# your desired level, The more  
	# the value of quality variable  
	# and lesser the compression 
	picture.save('static/upload/'+file,  
				 "JPEG",  
				 optimize = True,  
				 quality = 10) 
	return
  
# Define a main function 
def mainfun(): 
	
	verbose = False
	  
	# checks for verbose flag 
	if (len(sys.argv)>1): 
		
		if (sys.argv[1].lower()=="-v"): 
			verbose = True
					  
	# finds current working dir 
	cwd = 'static/upload'

  
	formats = ('.jpg', '.jpeg') 
	  
	# looping through all the files 
	# in a current directory 
	for file in os.listdir(cwd): 
		
		# If the file format is JPG or JPEG 
		if os.path.splitext(file)[1].lower() in formats: 
			print('compressing', file) 
			compressMe(file, verbose) 
 
	print("Done") 
  



def convertToBinaryData(filename):
	# Convert digital data to binary format
	with open(filename, 'rb') as file:
		binaryData = file.read()
	return binaryData


@app.route("/owner_upload",methods=['GET','POST'])
def owner_upload():
	if (request.method=='POST'):
		path='static/upload/'
		if os.path.exists(path):
			image1=request.files['image1'] 
			image2=request.files['image2']
			image3=request.files['image3']
			image4=request.files['image4']
			hostel_type=request.form.get('hosteltype')
			hostel_name=request.form.get('hostelname')
			owner_name=request.form.get('ownername')
			total_rooms=request.form.get('totalrooms')
			available_rooms=request.form.get('availablerooms')
			email=request.form.get('email')
			contact_no=request.form.get('contactno')
			alternate_no=request.form.get('alternateno')
			fees=request.form.get('fees')
			address=request.form.get('address')
			landmark=request.form.get('landmark')
			city=request.form.get('city')
			pincode=request.form.get('pincode')
			state=request.form.get('state')
			country=request.form.get('country')
			car=request.form.get('car')

	
			
			image1.save(path+image1.filename)
			image2.save(path+image2.filename)
			image3.save(path+image3.filename)
			image4.save(path+image4.filename)


				
			mainfun()
			path1=path+image1.filename
			img1=convertToBinaryData(path1)
			path2=path+image2.filename
			img2=convertToBinaryData(path2)
			path3=path+image3.filename
			img3=convertToBinaryData(path3)
			path4=path+image4.filename
			img4=convertToBinaryData(path4)
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('insert into owner_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(img1,img2,img3,img4,hostel_type,hostel_name,owner_name,total_rooms,available_rooms,email,contact_no,alternate_no,fees,address,landmark,city,pincode,state,country,car))
			con.commit()
			con.close()
			flash('Success..... Record has been submitted')
			return render_template('buttons.html')

		else:
			os.makedirs(path) 
			image1=request.files['image1'] 
			image2=request.files['image2']
			image3=request.files['image3']
			image4=request.files['image4']
			hostel_type=request.form.get('hosteltype')
			hostel_name=request.form.get('hostelname')
			owner_name=request.form.get('ownername')
			total_rooms=request.form.get('totalrooms')
			available_rooms=request.form.get('availablerooms')
			email=request.form.get('email')
			contact_no=request.form.get('contactno')
			alternate_no=request.form.get('alternateno')
			fees=request.form.get('fees')
			address=request.form.get('address')
			landmark=request.form.get('landmark')
			city=request.form.get('city')
			pincode=request.form.get('pincode')
			state=request.form.get('state')
			country=request.form.get('country')
			car=request.form.get('car')

			
			
			image1.save(path+image1.filename)
			image2.save(path+image2.filename)
			image3.save(path+image3.filename)
			image4.save(path+image4.filename)


			mainfun()	
			path1=path+image1.filename
			img1=convertToBinaryData(path1)

			path2=path+image2.filename
			img2=convertToBinaryData(path2)
			
			path3=path+image3.filename
			img3=convertToBinaryData(path3)
			path4=path+image4.filename
			img4=convertToBinaryData(path4)
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('insert into owner_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(img1,img2,img3,img4,hostel_type,hostel_name,owner_name,total_rooms,available_rooms,email,contact_no,alternate_no,fees,address,landmark,city,pincode,state,country,car))
			con.commit()
			con.close()
			flash('Success..... Record has been submitted')
			return render_template('buttons.html')




@app.route("/button",methods=['GET','POST'])
def button():
	return render_template("buttons.html")



@app.route("/owner_data_show",methods=['GET','POST'])
def owner_data_show():
	return render_template("owner_login_with_show.html")


def write_file(data, filename):
	# Convert binary data to proper format and write it on Hard Disk
	with open(filename, 'wb') as file:
		file.write(data)


@app.route("/owner_login_with_show",methods=['GET','POST'])
def owner_login_with_show():
	if (request.method=='POST'):
		email1=""
		hostel_email=""
		password1=""
		email1=request.form.get('email1')
		hostel_email=request.form.get('hostel_email')
		password1=request.form.get('password1')
		

		if email1=="" or password1=="" or hostel_email=="":
			flash('All fields are Required')
			return render_template("owner_login_with_show.html")

		else:
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('select * from owner_data')
			rows=cur.fetchall()
			flag=0
			for row in rows:
				if row[0]==email1 and row[1]==password1:
					flag=1
				elif row[0]==email1 and row[1]!=password1:
					flag=2

			cur.execute("select * from owner_info")
			rows=cur.fetchall()
			flag1=0
			for row in rows:
				if row[9]==hostel_email:
					flag1=4


		if flag1==4 and flag==1:
			
			session['email']='email'
			path='static/uploads'

			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			print(hostel_email)
			cur.execute("select * from owner_info where Email=%s",hostel_email)
			rec=cur.fetchall()
			for row in rec:
				if os.path.exists(path):
					shutil.rmtree(path)
					
					i=random.randint(1000,30000)
					j=random.randint(30001,60000)
					k=random.randint(60001,90000)
					l=random.randint(90001,120000)
					os.mkdir(path,0o777)

					path1=f'{path}/{i}.jpg'
					image=row[0]
					write_file(image,path1)
					

					path2=f'{path}/{j}.jpg'
					image2=row[1]
					write_file(image2,path2)
					

					path3=f'{path}/{k}.jpg'
					image3=row[2]
					write_file(image3,path3)
					

					path4=f'{path}/{l}.jpg'
					image4=row[3]
					write_file(image4,path4)
					

					hostel_type=row[4]
					hostel_name=row[5]
					owner_name=row[6]
					total_rooms=row[7]
					available_rooms=row[8]
					email=row[9]
					contact_no=row[10]
					alternate_no=row[11]
					fees=row[12]
					address=row[13]
					landmark=row[14]
					city=row[15]
					pincode=row[16]
					state=row[17]
					country=row[18]
					car=row[19]
					return render_template("owner_data_show.html",p=i,pp=j,ppp=k,pppp=l,hostel_type=hostel_type,hostel_name=hostel_name,owner_name=owner_name,total_rooms=total_rooms,available_rooms=available_rooms,email=email,contact_no=contact_no,alternate_no=alternate_no,fees=fees,address=address,landmark=landmark,city=city,pincode=pincode,state=state,country=country,car=car)

				else:
					i=random.randint(1000,30000)
					j=random.randint(30001,60000)
					k=random.randint(60001,90000)
					l=random.randint(90001,120000)
					os.makedirs(path)
				
					path1=f'{path}/{i}.jpg'
					image=row[0]
					write_file(image,path1)
					

					path2=f'{path}/{j}.jpg'
					image2=row[1]
					write_file(image2,path2)
					

					path3=f'{path}/{k}.jpg'
					image3=row[2]
					write_file(image3,path3)
					

					path4=f'{path}/{l}.jpg'
					image4=row[3]
					write_file(image4,path4)
					

					hostel_type=row[4]
					hostel_name=row[5]
					owner_name=row[6]
					total_rooms=row[7]
					available_rooms=row[8]
					email=row[9]
					contact_no=row[10]
					alternate_no=row[11]
					fees=row[12]
					address=row[13]
					landmark=row[14]
					city=row[15]
					pincode=row[16]
					state=row[17]
					country=row[18]
					car=row[19]
					return render_template("owner_data_show.html",p=i,pp=j,ppp=k,pppp=l,hostel_type=hostel_type,hostel_name=hostel_name,owner_name=owner_name,total_rooms=total_rooms,available_rooms=available_rooms,email=email,contact_no=contact_no,alternate_no=alternate_no,fees=fees,address=address,landmark=landmark,city=city,pincode=pincode,state=state,country=country,car=car)

		elif flag==2:
			flash('Incorrect password')
			return render_template("owner_login_with_show.html")
		elif flag1==0:
			flash('Hostel Email doesn\'t exist')
			return render_template("owner_login_with_show.html")

		else:
			flash('Your Email doesn\'t exist')
			return render_template("owner_login_with_show.html")
		
		con.close()


@app.route("/logout_from_show",methods=['GET','POST'])
def logout_from_show():
	return render_template("buttons.html")
	session.pop('email')


#*************************************************************

@app.route("/owner_data_update",methods=['GET','POST'])
def owner_data_update():
	return render_template("owner_login_with_update.html")



@app.route("/owner_data_update_validation",methods=['GET','POST'])
def owner_data_update_validation():
	if (request.method=='POST'):
		email1=request.form.get('email1')
		hostel_email=request.form.get('hostel_email')
		password1=request.form.get('password1')		
		

	if email1=="" or password1=="" or hostel_email=="":
		flash('All fields are Required')
		return render_template("owner_login_with_update.html")

	else:
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute('select * from owner_data')
		rows=cur.fetchall()
		flag=0
		for row in rows:
			if row[0]==email1 and row[1]==password1:
				flag=1
			elif row[0]==email1 and row[1]!=password1:
				flag=2

		cur.execute("select * from owner_info")
		rows=cur.fetchall()
		flag1=0
		for row in rows:
			if row[9]==hostel_email:
				flag1=1
	if flag==1 and flag1==1:
		session['email']='email'
		path='static/upload'
		path22='static/upload'
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute("select * from owner_info where Email=%s",hostel_email)
		rec=cur.fetchall()
		for row in rec:
			if os.path.exists(path):
				hostel_type=row[4]
				hostel_name=row[5]
				owner_name=row[6]
				total_rooms=row[7]
				available_rooms=row[8]
				email=row[9]
				contact_no=row[10]
				alternate_no=row[11]
				fees=row[12]
				address=row[13]
				landmark=row[14]
				city=row[15]
				pincode=row[16]
				state=row[17]
				country=row[18]
				car=row[19]
				

			else:
				os.makedirs(path)
				hostel_type=row[4]
				hostel_name=row[5]
				owner_name=row[6]
				total_rooms=row[7]
				available_rooms=row[8]
				email=row[9]
				contact_no=row[10]
				alternate_no=row[11]
				fees=row[12]
				address=row[13]
				landmark=row[14]
				city=row[15]
				pincode=row[16]
				state=row[17]
				country=row[18]
				car=row[19]
		return render_template("owner_data_update.html",hostel_type=hostel_type,hostel_name=hostel_name,owner_name=owner_name,total_rooms=total_rooms,available_rooms=available_rooms,email=email,contact_no=contact_no,alternate_no=alternate_no,fees=fees,address=address,landmark=landmark,city=city,pincode=pincode,state=state,country=country,car=car)

	elif flag==2:
		flash('Incorrect password')
		return render_template("owner_login_with_update.html")
	elif flag1==0:
		flash('Hostel Email doesn\'t exist')
		return render_template("owner_login_with_update.html")

	else:
		flash('Your Email doesn\'t exist')
		return render_template("owner_login_with_update.html")

	 








@app.route("/owner_login_with_update_success",methods=['GET','POST'])
def owner_login_with_update_success():
	if (request.method=='POST'):




		path='static/upload/'
		if os.path.exists(path):
			image1=request.files['image1']
			image2=request.files['image2']
			image3=request.files['image3']
			image4=request.files['image4']
			hostel_type=request.form.get('hosteltype')
			hostel_name=request.form.get('hostelname')
			owner_name=request.form.get('ownername')
			total_rooms=request.form.get('totalrooms')
			available_rooms=request.form.get('availablerooms')
			email=request.form.get('email')
			contact_no=request.form.get('contactno')
			alternate_no=request.form.get('alternateno')
			fees=request.form.get('fees')
			address=request.form.get('address')
			landmark=request.form.get('landmark')
			city=request.form.get('city')
			pincode=request.form.get('pincode')
			state=request.form.get('state')
			country=request.form.get('country')
			car=request.form.get('car')

			image1.save(path+image1.filename)
			image2.save(path+image2.filename)
			image3.save(path+image3.filename)
			image4.save(path+image4.filename)
	
			mainfun()
			path1=path+image1.filename
			img1=convertToBinaryData(path1)
			path2=path+image2.filename
			img2=convertToBinaryData(path2)
			path3=path+image3.filename
			img3=convertToBinaryData(path3)
			path4=path+image4.filename
			img4=convertToBinaryData(path4)

			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('update owner_info set Image1=%s , Image2=%s , Image3=%s , Image4=%s , Hotel_type=%s , Hotel_name=%s , Owner_name=%s , Total_rooms=%s, Available_rooms=%s, Contact_no=%s, Alternate_no=%s, Room_charge=%s, Address=%s, Landmark=%s, City=%s, Pincode=%s, State=%s, Country=%s, Cooler_air_conditioner_refrigerator=%s where Email=%s ',(img1,img2,img3,img4,hostel_type,hostel_name,owner_name,total_rooms,available_rooms,contact_no,alternate_no,fees,address,landmark,city,pincode,state,country,car,email))
			con.commit()
			con.close()
			session.pop('email','none')
			flash('Success..... Record has been submitted')
			return render_template('buttons.html')

		else:
			os.makedirs(path)

			image1=request.files['image1']
			image2=request.files['image2']
			image3=request.files['image3']
			image4=request.files['image4']
			hostel_type=request.form.get('hosteltype')
			hostel_name=request.form.get('hostelname')
			owner_name=request.form.get('ownername')
			total_rooms=request.form.get('totalrooms')
			available_rooms=request.form.get('availablerooms')
			email=request.form.get('email')
			contact_no=request.form.get('contactno')
			alternate_no=request.form.get('alternateno')
			fees=request.form.get('fees')
			address=request.form.get('address')
			landmark=request.form.get('landmark')
			city=request.form.get('city')
			pincode=request.form.get('pincode')
			state=request.form.get('state')
			country=request.form.get('country')
			car=request.form.get('car')

			image1.save(path+image1.filename)
			image2.save(path+image2.filename)
			image3.save(path+image3.filename)
			image4.save(path+image4.filename)
			mainfun()

			path1=path+image1.filename
			img1=convertToBinaryData(path1)
			path2=path+image2.filename
			img2=convertToBinaryData(path2)
			path3=path+image3.filename
			img3=convertToBinaryData(path3)
			path4=path+image4.filename
			img4=convertToBinaryData(path4)

			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('update owner_info set Image1=%s , Image2=%s , Image3=%s , Image4=%s , Hotel_type=%s , Hotel_name=%s , Owner_name=%s , Total_rooms=%s, Available_rooms=%s, Contact_no=%s, Alternate_no=%s, Room_charge=%s, Address=%s, Landmark=%s, City=%s, Pincode=%s, State=%s, Country=%s, Cooler_air_conditioner_refrigerator=%s where Email=%s ',(img1,img2,img3,img4,hostel_type,hostel_name,owner_name,total_rooms,available_rooms,contact_no,alternate_no,fees,address,landmark,city,pincode,state,country,car,email))
			session.pop('value')
			con.commit()
			con.close()
			session.pop('email','none')
			flash('Success..... Record has been submitted')
			return render_template('buttons.html')






@app.route("/search_hostels/<string:hostelname>",methods=['GET','POST'])
def search_hostel(hostelname):
	global m,n,o,p,hostel_type,hostel_name,owner_name,total_rooms,available_rooms,email,contact_no,alternate_no,fees,address,landmark,city,pincode,state,country,car
	if (request.method=='POST'):
		path='static/uploader'
		con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
		cur=con.cursor()
		cur.execute("select * from owner_info where Hotel_name=%s",hostelname)
		row=cur.fetchone()



		if os.path.exists(path):
			shutil.rmtree(path)
			os.makedirs(path)
		else:
			os.makedirs(path)


		m=''
		n=''
		o=''
		p=''
		m=random.randint(120000,150000)
		n=random.randint(150000,180000)
		o=random.randint(180000,210000)
		p=random.randint(210000,240000)


		path1=f'{path}/{m}.jpg'
		image=row[0]
		write_file(image,path1)

		path2=f'{path}/{n}.jpg'
		image2=row[1]
		write_file(image2,path2)
							

		path3=f'{path}/{o}.jpg'
		image3=row[2]
		write_file(image3,path3)
							

		path4=f'{path}/{p}.jpg'
		image4=row[3]
		write_file(image4,path4)

		m=str(m)+'.jpg'
		n=str(n)+'.jpg'
		o=str(o)+'.jpg'
		p=str(p)+'.jpg'
							

		hostel_type=row[4]
		hostel_name=row[5]
		owner_name=row[6]
		total_rooms=row[7]
		available_rooms=row[8]
		email=row[9]
		contact_no=row[10]
		alternate_no=row[11]
		fees=row[12]
		address=row[13]
		landmark=row[14]
		city=row[15]
		pincode=row[16]
		state=row[17]
		country=row[18]
		car=row[19]
	return render_template("hostel.html",p1=m,p2=n,p3=o,p4=p,hostel_type=hostel_type,hostel_name=hostel_name,owner_name=owner_name,total_rooms=total_rooms,available_rooms=available_rooms,email=email,contact_no=contact_no,alternate_no=alternate_no,fees=fees,address=address,landmark=landmark,city=city,pincode=pincode,state=state,country=country,car=car)
	


@app.route("/contactus",methods=['GET','POST'])
def contactus():
	return render_template('contact_us.html')


@app.route("/contact",methods=['GET','POST'])
def contact():
	if (request.method=='POST'):
		email=request.form.get('email')
		name=request.form.get('name')
		contactno=request.form.get('contactno')
		msg=request.form.get('msg')

		if name=="" or email=="" or msg=="":
			flash("Please fill all fields and correct fields")
			return render_template("contact_us.html")
		elif len(contactno)>10 or len(contactno)<10:
			flash("Please fill correct contact number")
			return render_template("contact_us.html")
		else:
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('insert into contact_us values(%s,%s,%s,%s)',(email,name,contactno,msg))
			con.commit()
			con.close()
			return render_template("home.html")



@app.route("/feedback",methods=['GET','POST'])
def feedback():
	return render_template('feedback.html')


@app.route("/feedback_us",methods=['GET','POST'])
def feedback_us():
	if (request.method=='POST'):
		name=request.form.get('name')
		contactno=request.form.get('contactno')
		msg=request.form.get('msg')

		if name=="" or msg=="":
			flash("Please fill all fields and correct fields")
			return render_template("feedback.html")
		elif len(contactno)>10 or len(contactno)<10:
			flash("Please fill correct contact number")
			return render_template("feedback.html")
		else:
			con=pymysql.connect(host='localhost',user='root',password='',database='hotel')
			cur=con.cursor()
			cur.execute('insert into feedback values(%s,%s,%s)',(name,contactno,msg))
			con.commit()
			con.close()
			return render_template("home.html")





@app.route("/about",methods=['GET','POST'])
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True)