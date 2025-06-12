import requests 
 
print("**********SIMILAR SOUNDING WORD FINDER*************")
word = input("Enter a word:")

response = requests.get(f"https://api.datamuse.com/words?sl={word}")
 
content = response.json()
 
if response.status_code == 200:
    # print(content)
    i = 0
    while i < 5:
        print(content[i]["word"])
        i+=1
else:
    print(f"Invalid status code {response.status_code}")