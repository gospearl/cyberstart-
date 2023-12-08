
link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!


answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib.request.urlopen(answer)
response = response.read()
print(response.decode('utf-8'))
