import requests
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

urls = [
    "https://en.wikipedia.org/wiki/Computer",
    "https://en.wikipedia.org/wiki/Algorithm",
    "https://en.wikipedia.org/wiki/Data",
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Neural_network",
    "https://en.wikipedia.org/wiki/Database",
    "https://en.wikipedia.org/wiki/Operating_system",
    "https://en.wikipedia.org/wiki/Software",
    "https://en.wikipedia.org/wiki/Programming_language",
    "https://en.wikipedia.org/wiki/Internet",
    "https://en.wikipedia.org/wiki/Network",
    "https://en.wikipedia.org/wiki/Information",
    "https://en.wikipedia.org/wiki/Technology",
    "https://en.wikipedia.org/wiki/Engineering",
    "https://en.wikipedia.org/wiki/Mathematics",
    "https://en.wikipedia.org/wiki/Statistics",
    "https://en.wikipedia.org/wiki/Physics",
    "https://en.wikipedia.org/wiki/Chemistry",
    "https://en.wikipedia.org/wiki/Biology",
    "https://en.wikipedia.org/wiki/Earth",
    "https://en.wikipedia.org/wiki/Europe",
    "https://en.wikipedia.org/wiki/Asia",
    "https://en.wikipedia.org/wiki/Africa",
    "https://en.wikipedia.org/wiki/North_America",
    "https://en.wikipedia.org/wiki/South_America",
    "https://en.wikipedia.org/wiki/Australia",
    "https://en.wikipedia.org/wiki/Oceania",
    "https://en.wikipedia.org/wiki/Science",
    "https://en.wikipedia.org/wiki/Research",
    "https://en.wikipedia.org/wiki/Education",
    "https://en.wikipedia.org/wiki/University",
    "https://en.wikipedia.org/wiki/Student",
    "https://en.wikipedia.org/wiki/Teacher",
    "https://en.wikipedia.org/wiki/Knowledge",
    "https://en.wikipedia.org/wiki/Library",
    "https://en.wikipedia.org/wiki/History",
    "https://en.wikipedia.org/wiki/Philosophy",
    "https://en.wikipedia.org/wiki/Psychology",
    "https://en.wikipedia.org/wiki/Sociology",
    "https://en.wikipedia.org/wiki/Economics",
    "https://en.wikipedia.org/wiki/Politics",
    "https://en.wikipedia.org/wiki/Law",
    "https://en.wikipedia.org/wiki/Government",
    "https://en.wikipedia.org/wiki/Democracy",
    "https://en.wikipedia.org/wiki/Market",
    "https://en.wikipedia.org/wiki/Industry",
    "https://en.wikipedia.org/wiki/Company",
    "https://en.wikipedia.org/wiki/Business",
    "https://en.wikipedia.org/wiki/Management",
    "https://en.wikipedia.org/wiki/Finance",
    "https://en.wikipedia.org/wiki/Investment",
    "https://en.wikipedia.org/wiki/Bank",
    "https://en.wikipedia.org/wiki/Stock_market",
    "https://en.wikipedia.org/wiki/Trade",
    "https://en.wikipedia.org/wiki/Marketing",
    "https://en.wikipedia.org/wiki/Entrepreneurship",
    "https://en.wikipedia.org/wiki/Innovation",
    "https://en.wikipedia.org/wiki/Project_management",
    "https://en.wikipedia.org/wiki/Leadership",
    "https://en.wikipedia.org/wiki/Communication",
    "https://en.wikipedia.org/wiki/Language",
    "https://en.wikipedia.org/wiki/Linguistics",
    "https://en.wikipedia.org/wiki/Literature",
    "https://en.wikipedia.org/wiki/Art",
    "https://en.wikipedia.org/wiki/Music",
    "https://en.wikipedia.org/wiki/Film",
    "https://en.wikipedia.org/wiki/Photography",
    "https://en.wikipedia.org/wiki/Design",
    "https://en.wikipedia.org/wiki/Architecture",
    "https://en.wikipedia.org/wiki/Transportation",
    "https://en.wikipedia.org/wiki/Aviation",
    "https://en.wikipedia.org/wiki/Automobile",
    "https://en.wikipedia.org/wiki/Rail_transport",
    "https://en.wikipedia.org/wiki/Ship",
    "https://en.wikipedia.org/wiki/Energy",
    "https://en.wikipedia.org/wiki/Electricity",
    "https://en.wikipedia.org/wiki/Nuclear_power",
    "https://en.wikipedia.org/wiki/Renewable_energy",
    "https://en.wikipedia.org/wiki/Climate_change",
    "https://en.wikipedia.org/wiki/Environment",
    "https://en.wikipedia.org/wiki/Ecology",
    "https://en.wikipedia.org/wiki/Geography",
    "https://en.wikipedia.org/wiki/Geology",
    "https://en.wikipedia.org/wiki/Astronomy",
    "https://en.wikipedia.org/wiki/Planet",
    "https://en.wikipedia.org/wiki/Solar_System",
    "https://en.wikipedia.org/wiki/Universe",
    "https://en.wikipedia.org/wiki/Space_exploration",
    "https://en.wikipedia.org/wiki/Satellite",
    "https://en.wikipedia.org/wiki/Robotics",
    "https://en.wikipedia.org/wiki/Cybersecurity",
    "https://en.wikipedia.org/wiki/Blockchain",
    "https://en.wikipedia.org/wiki/Cryptocurrency",
    "https://en.wikipedia.org/wiki/Big_data",
    "https://en.wikipedia.org/wiki/Data_science",
    "https://en.wikipedia.org/wiki/Cloud_computing",
    "https://en.wikipedia.org/wiki/Computer_security"
]

os.makedirs("pages", exist_ok=True)

index_file = open("index.txt", "w", encoding="utf-8")

for i, url in enumerate(urls, start=1):

    try:
        response = requests.get(url, headers=headers)

        filename = f"pages/{i}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        index_file.write(f"{i} {url}\n")

        print("Downloaded:", url)

    except Exception as e:
        print("Error:", url)

index_file.close()

print("Finished downloading pages")