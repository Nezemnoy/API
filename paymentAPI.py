import hashlib
import json
import requests

# Secret key from your billing account settings
secret_key = "qwerty0987654"

# Data needed for the signature
wsb_seed = "1242649174"
wsb_storeid = "384256856"
wsb_order_num = "ORDER-12345678"
wsb_test = "1"  # Changed to "1" to denote a test transaction
wsb_currency_id = "BYN"
wsb_total = "100"  # Total amount for the transaction

# Concatenate the values for the signature
signature_raw = f"{wsb_seed}{wsb_storeid}{wsb_order_num}{wsb_test}{wsb_currency_id}{wsb_total}{secret_key}"

# Hash the concatenated string using SHA1
wsb_signature = hashlib.sha1(signature_raw.encode()).hexdigest()

# API endpoint
url = "https://securesandbox.webpay.by/api/v1/payment"

# Headers
headers = {
    'Content-Type': 'application/json',
}

# Data to be sent
data = {
    "wsb_storeid": wsb_storeid,
    "wsb_order_num": wsb_order_num,
    "wsb_currency_id": wsb_currency_id,
    "wsb_version": 2,
    "wsb_seed": wsb_seed,
    "wsb_test": int(wsb_test),  # Ensure this is sent as an integer
    "wsb_invoice_item_name": ["Товар 1"],
    "wsb_invoice_item_quantity": [1],
    "wsb_invoice_item_price": [100],
    "wsb_total": float(wsb_total),  # Ensure this is sent as a float
    "wsb_signature": wsb_signature,
    "wsb_return_url": "http://yoursiteurl.com/success.php",
    "wsb_cancel_return_url": "http://yoursiteurl.com/cancel.php",
    "wsb_notify_url": "http://yoursiteurl.com/notify.php"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print("Status Code:", response.status_code)
print("Response:", response.text)