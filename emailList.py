import requests, json
import googlemaps
import smtplib
from email.message import EmailMessage

address = "10407 new rd north jackson ohio"

def findLatLon(key):
    req = requests.get(f'''
                       https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}
                       ''')
    return json.loads(req.content)["results"][0]["geometry"]["location"]


key = 'AIzaSyBmj9L3n7ngkMiIiJYUjrXffg3XUZcsXqM'

latlon = findLatLon(key)
print(latlon)

lattylonggy = []
lattylonggy.append(str(latlon['lat']))
lattylonggy.append(str(latlon['lng']))

gmaps = googlemaps.Client(key=key)

location = ",".join(lattylonggy)

res = gmaps.places_nearby(location=location, radius=40000)

results = res['results']


nonWebsites = []
for result in results:
    idd = result['place_id']
    
    requestStr = f"https://maps.googleapis.com/maps/api/place/details/json?fields=name%2Cformatted_phone_number%2Cwebsite&place_id={idd}&key={key}"
    details = requests.get(requestStr)
    
    try: 
        json.loads(details.content)["result"]["website"]
    except Exception:
        nonWebsites.append(details.content)
    
    
def sendMessage(message, number):
    #TODO RM
    number = 3305199231
    
    msg = EmailMessage()
    msg['Subject'] = "Business (and therefore personal) Oprotunity."
    msg["From"] = "JonFactor06@gmail.com"
    msg["to"] = number
    msg.set_content(message)
    
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    
    s.login("jonfactor06@gmail.com", "VBBG9DAa1")
    
    s.send_message(msg)
    
    s.quit()

for i in nonWebsites:
    
    # location info
    cur = json.loads(i)["result"]
    
    #is number
    try:
        cur["formatted_phone_number"]
    except Exception:
        continue
    
    name = cur["name"]
    number = cur["formatted_phone_number"]
    
    
    
    # text contents
    
    isDay = False #TODO FIX
    
    openingStatement = f"Hello, {name}\n\n\n"

    businessTypeStatment = f"I understand that {name} currently is lacking a website and from my best knowlage is missing out on a huge, passive stream of free advertisments.\nYour industry can be difficult to manage and build an entire website for.\nThat is why I am inquiring about a business oprotunity if you would just lend me 5 minutes of your time.\n"
    
    benifitsForThem = f"The best way in which the benifits of a website can be communicated is through listing (because there are so many).\n"
    benifitsForThem += "\n1. More Exposure people get to you.\n"
    benifitsForThem += "2. Your business information is out there for the world to see\n"
    benifitsForThem += "3. According to digital.com, ""Before visiting a brick-and-mortar business in person for the first time, 91% of shoppers will look up the business online""\n"
    benifitsForThem += "4. Branding can also be started on a website with inviting graphics of the business's logo and mascots if applicable.\n"
    benifitsForThem += "5. Marketing is expensive, but it does not have to be when it comes to websites.\n"
    benifitsForThem += "6. Not only will a website just improve your marketing budget but it also makes your business have a world wide marketing reach that works for you 24/7, day or night without any employees.\n"
    benifitsForThem +=f"7. A website shows that your business is transparent with its customers and can make users fell a hightened sense of trust, vital for Your business.\n"
    benifitsForThem += "8. Now a days everyone has a website, because users / customers expect to see a website from a modern day business and no business has ran sucessfully by denying its customers what they want, except the government.\n"
    benifitsForThem += "9. Generating sales leads can also be acomplished through an easy intigratable emailing system within the website.\n"
    benifitsForThem +="10. Lastly, You can boast to your friends about owning a plot of land on the ever expanding parry of the world wide web.\n"
 
    benifitsForThem += "\nThe only downside to a website is of course the cost of maintainence and hosting. Servers are however not expensive and the advertisment generated from the website, hugely outweights the cost of a well maintained website experiance.\n"
    
    benifitsForMe = f"\nMoving forward, I belive I should disclose my motivations for working of this project."
    benifitsForMe += "\n1. Every employeer is looking for two things in an employee and that is experiance and experiance, after all if I can't show that I know how to do the job then who can hire me? So I need to work for a reduced rate until people start (/ if) appricating my work and valuing it accordingly."
    benifitsForMe += "\n2. Everyone has to start somewhere, if I don't dedicate myself to projects that are applicable in the real world I can get a detached sense of coding and drift into the habbit of creating meaningless code like, building a project no one will see. this gives me an opprotunity to instead contribute to something."
    benifitsForMe += "\n3. Passive income has been a sort of fallicy in the recent 'get rich quick' economy I have grown up in and this is a valid way to gain semi-passive income (income that i do not have to be working 24/7 on but that for momentary periods need to work on)."
    
    messageBody = f"{businessTypeStatment}\n{benifitsForThem}\n{benifitsForMe}\n"
    
    closingsStatment = "Thank you for your time,\nSincerly Jon\n(please contact me directly at 330-519-9231)"
    
    message = f"{openingStatement}{messageBody}\n\n\n{closingsStatment}"
    
    
    # sending message
    
    print(message)
    
    sendMessage(message, number)
    
    # record sucess / fail