import re
url= input("Enter your twitter url: ").strip()
if matches:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url, re.IGNORECASE):
    print("Username is: ", matches.group(1))
 