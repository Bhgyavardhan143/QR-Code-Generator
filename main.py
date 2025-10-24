import qrcode

#Taking UPI ID as a Input
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on UPI ID and payment app



phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Creating QR Codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)


#Displaying the QR Codes 

phonepe_qr.show()
google_pay_qr.show()