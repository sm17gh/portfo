from flask import Flask, render_template, url_for, request, redirect
import csv
#
# Porfolio Web Server
#
app = Flask(__name__)

@app.route('/')
def sm_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def sm_html_page(page_name):
    return render_template(page_name)

def save_contact_data(data):
	with open('database.csv', newline='', mode='a') as csvdb:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(csvdb, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])	

@app.route('/submit_form', methods=['POST', 'GET'])
def sm_submit_form():
	if request.method == 'POST':
		try:
			request_dict = request.form.to_dict()
			save_contact_data(request_dict)
			return redirect('thankyou.html')
		except:
			return 'Information not saved to database.'
	else:
		return 'Something went wrong. Try again!'