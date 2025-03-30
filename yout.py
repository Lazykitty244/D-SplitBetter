import json
import requests

url = "https://ocr.asprise.com/api/v1/receipt"
image = r"C:\Users\asrit\OneDrive - Arizona State University\Personal Proects\Dsplitbetter\cosctcobill.jpg"

res = requests.post(url,
                    data={
                        'api_key': 'TEST',
                        'recognizer': 'auto',
                        'ref_no': 'oct_python_123'
                    },
                    files={
                        'file': open(image, 'rb')
                    })

# Save the JSON response to a file
with open("response1.json", "w") as f:
    json.dump(res.json(), f)
