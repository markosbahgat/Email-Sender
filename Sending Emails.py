import smtplib
import email.message as emi
import filetype

# -----------All user inputs-------------------


user_email = input('Insert Sender email address')
user_password = input("Insert Sender email's password")
the_receiver = input('Enter the receiver email address')
email_subject = input('Enter the subject of your email')
email_body = input("Enter the body content of your email")
file_path = input('enter your attachment file path if there is , if there is not press "Enter" to Skip ....')

# -------------------------------------------------


image_extensions = ['png', 'jpg', 'jpeg', 'svg', 'gif']
video_extensions = ['mp4', 'avi', 'mpeg', 'wmv', 'm4v']
our_main_type = ""

msg = emi.EmailMessage()
msg['To'] = the_receiver
msg['From'] = user_email
msg['Subject'] = email_subject
msg.set_content(email_body)

# Here is an if statement to check if the user has insert right file path or not and if there is an error it will throw an exception
# also it will check if the user has attach a file in the first place if there is no file attached it will continue and send the email anyway


if bool(file_path):
    try:
        our_file_type = filetype.guess(file_path)
        with open(file_path, 'rb') as file:
            our_file_data = file.read()
            my_file_type = our_file_type.extension
            our_file_name = file.name
        if our_file_type.extension in image_extensions:
            our_main_type = "image"
        elif our_file_type.extension in video_extensions:
            our_main_type = "video"
        else:
            our_main_type = "pdf"
        msg.add_attachment(our_file_data, maintype=our_main_type, subtype=my_file_type, filename=our_file_name)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(user_email, user_password)
            smtp.send_message(msg)
    except:
        print("Error happend ...! \n Please Enter A Vaild File Path !!")
else:
    print("you did't attach any files")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user_email, user_password)
        smtp.send_message(msg)
