import os

Feature_Nas = [
    "Melbourne Aquarium",
    "The Museum Of Australian Chinese History",
    "Australian Centre For The Moving Image (ACMI)",
    "Cooks' Cottage",
    "Koorie Heritage Trust Inc",
    "The Ian Potter Museum Of Art",
    "Fire Services Museum Victoria",
    "Immigration Museum",
    "Victoria Police Museum",
    "Sinclair's Cottage",
    "National Sports Museum",
    "Melbourne Museum",
    "Fox Classic Car Collection",
    "Thoroughbred Racing Gallery",
    "The Ian Potter Centre: NGV Australia",
    "Victorian Arts Centre",
    "Australian Centre for Contemporary Art",
    "Polly Woodside",
    "Old Melbourne Gaol Crime & Justice Experience",
    "Webb Bridge",
    "Crown Entertainment Complex",
    "Melbourne General Cemetery",
    "St Pauls Cathedral",
    "St Patricks Cathedral",
    "The Parish of Christ Church South Yarra",
    "South Yarra Presbyterian Church",
    "St Thomas Aquinas Church",
    "Collins Street Baptist Church",
    "Holy Rosary",
    "Christ Church Kensington",
    "St Alban Anglican Church",
    "Ukranian Catholic Cathedral",
    "St Michaels",
    "Our Lady of Lebanon Church",
    "All Nations Uniting Church",
    "Melbourne Unitarian Church",
    "North Melbourne Uniting",
    "St Johns Lutheran Church",
    "Holy Trinity",
    "Lutheran Trinity Church",
    "St Peter's Eastern Hill",
    "Greek Orthodox Church",
    "St Michael's Uniting Church",
    "Scots Church",
    "Church of Christ",
    "Welsh Presbyterian Church",
    "Romanian Orthodox",
    "St Mary's Anglican Church",
    "St James Church",
    "St Augustines Church",
    "Wesley Church",
    "St Francis Church",
    "IMAX Melbourne",
    "Harbour Town",
    "Railway Good Shed No 2",
    "David Jones",
    "Myer",
    "Bishopscourt",
    "Government House",
    "Channel 7 - Melbourne Broadcast Centre",
    "Central City Studios",
    "Metropolitan Fire Brigade (MFB)",
    "Dallas Brooks Centre",
    "Central Pier",
    "Melbourne Convention Centre",
    "Melbourne Exhibition Centre",
    "Kangan Batman Tafe",
    "Melbourne Magistrates Court",
    "North Melbourne Recreation Centre (Gymnasium)",
    "The Mission To Seafarers Victoria",
    "Carlton Baths",
    "Icehouse",
    "Artplay",
    "Kraft",
    "Lincoln Square",
    "Sandridge Rail Bridge",
    "Westgate Park",
    "Murchinson Square",
    "Macarthur Square",
    "Piazza Italia",
    "Argyle Square",
    "Fitzroy Gardens",
    "Fawkner Park",
    "Flagstaff Gardens",
    "Royal Botanic Gardens",
    "Shrine of Rembrance Reserve",
    "Princes Park",
    "Royal Park",
    "J.J Holland Park",
    "North Melbourne Recreation Reserve",
    "Alexandra Gardens",
    "Riverslide Skate Park",
    "Newmarket Reserve",
    "Point Park",
    "Docklands Park",
    "New Quay",
    "Federation Square",
    "Queen Victoria Gardens",
    "Richmond Football Club",
    "Batman Park",
    "Treasury Gardens",
    "Kings Domain",
    "Carlton Gardens North",
    "Powlett Reserve",
    "Carlton Gardens South",
    "The Melbourne Athenaeum Library",
    "Etihad Stadium",
    "Westpac Centre",
    "City Baths",
    "North Melbourne Recreation Centre (Aquatic)",
    "Margaret Court Arena",
    "Melbourne Park",
    "Rod Laver Arena",
    "AAMI Park",
    "Melbourne Cricket Ground (MCG)",
    "Flemington Racecourse",
    "Visy Park",
    "Carlton Football Club",
    "State Netball Hockey Centre",
    "New Quay Marina",
    "Eureka Skydeck 88",
    "Melbourne Star Observation Wheel",
    "State Coroners Office",
    "Donor Tissue Bank of Victoria",
    "Victorian Insitute of Forensic Medicine",
    "Coronial Services Centre of Victoria",
    "SBS (Special Broadcasting Service)",
    "Former Royal Mint",
    "Parliament House",
    "Australian Red Cross",
    "Old Treasury Building",
    "Melbourne Showgrounds",
    "Riverside Park",
    "Wonderland Park",
    "Melbourne Zoo",
    "Victoria Police",
    "Victoria Police",
    "Victoria Police",
    "North Melbourne Primary School",
    "Kensington Primary School",
    "Carlton Primary School",
    "Carlton Gardens Primary School",
    "Epworth Freemasons Hospital",
    "Epworth Freemasons Hospital : Medical Centre",
    "Melbourne Private Hospital",
    "Melbourne International Shooting Club",
    "Royal Park Golf Course",
    "County Court Melbourne",
    "Melbourne Childrens Court",
    "Conservatory",
    "Commonwealth Law Courts",
    "Shrine of Remembrance",
    "NGV International",
    "Melbourne Recital Centre",
    "Elisabeth Murdoch Hall",
    "Sidney Myer Music Bowl",
    "Melbourne Town Hall",
    "Supreme Court",
    "State Library Victoria",
    "Royal Dental Hospital",
    "Peter Maccallum Cancer Institute",
    "Royal Melbourne Hospital",
    "Alfred Hospital",
    "Royal Childrens Hospital",
    "Royal Womens Hospital",
    "The Royal Victorian Eye & Ear Hospital",
    "North Melbourne Railway Station",
    "Melbourne Central Railway Station",
    "Flinders Street Railway Station",
    "Newmarket Railway Station",
    "Showgrounds Railway Station (Flemington)",
    "Flemington Racecourse Railway Station",
    "Melbourne Central Railway Station",
    "Melbourne Central Railway Station",
    "Melbourne Central Railway Station",
    "Flagstaff Railway Station",
    "Parliament Railway Station",
    "Parliament Railway Station",
    "Parliament Railway Station",
    "Royal Park Railway Station",
    "South Kensington Railway Station",
    "Kensington Railway Station",
    "Jolimont-MCG Railway Station (East Melbourne) - Train stop",
    "Richmond Railway Station (Richmond) - Train stop",
    "Parliament Railway Station",
    "Flagstaff Railway Station",
    "Southern Cross Railway Station",
    "Flemington Bridge Railway Station",
    "Queen Victoria Market",
    "Treasury Reserve",
    "ANZ 'Gothic' Bank",
    "Melbourne Central",
    "Southgate Arts and Leisure Precinct",
    "Council House 2 (CH2)",
    "Freshwater Place",
    "QV Village",
    "Eureka Tower",
    "Melbourne Girls Grammar School",
    "Wesley College",
    "University High School",
    "Melbourne Grammar School",
    "Melbourne Wholesale Fish Market",
    "East Melbourne Synagogue",
    "RMIT University",
    "University of Melbourne",
    "BIO 21 Institute",
    "University of Melbourne (VCA and Music)",
    "La Mama Theatre",
    "Comedy Theatre",
    "Her Majesty's Theatre",
    "Carlton Courthouse Theatre",
    "Athanaeum Theatre",
    "Hamer Hall",
    "MTC Theatre",
    "Malthouse Theatre",
    "Regent Theatre",
    "Princess Theatre",
    "St Martins Youth Arts Centre",
    "State Theatre",
    "Playhouse",
    "FairFax Studio",
    "Port of Melbourne",
    "Melbourne International Karting Complex",
    "Melbourne Visitor Centre",
    "Melbourne Visitor Booth"
]

def getNonRepeatList1(data):
    return list(set(data))


NewFeature = getNonRepeatList1(Feature_Nas)
print(len(NewFeature))

path = "/Users/yunning/DATA/IT/poiTest5/"
# path = "/Users/yunning/Library/Mobile Documents/com~apple~CloudDocs/DATA/UM/2020S2/GEOM90007/assignments/3/code/IV3_TouristMap/images/poiTest/"  # 目标路径

"""os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
filename_list = os.listdir(path)  # 扫描目标路径的文件,将文件名存入列表

a = 0
i = 0
for file in filename_list:
    # if i == 200:
    #     break
    print("i: ", i)
    print("a: ", a)
    used_name = path + filename_list[a]
    # new_name = path + "fig_" + str(i) + ".jpg"
    new_name = path + NewFeature[i] + ".jpg"
    os.rename(used_name, new_name)
    print("%s ==> %s" % (used_name, new_name))
    a += 1
    i += 1


