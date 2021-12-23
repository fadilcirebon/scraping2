import requests
import flask
response = requests.get('https://www.eramuslim.com')
print(response)
def response1():
    if response.status_code == 200:
        print('Connected')
    else:
        print('failed')
def response2():
    if response:
        print('sukses')
    else:
        print('an error has occured')
if __name__ == '__main__':
    response2()
