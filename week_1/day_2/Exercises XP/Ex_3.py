brand ={
   "name": "Zara ",
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona" ,
    "type_of_clothes": ["men", "women", "children", "home" ],
    "international_competitors":[ "Gap", "H&M"," Benetton" ],
    "number_stores": 7000 ,
    "major_color": 
        {"France":" blue",
         "Spain": "red", 
         "US":[ "pink", "green"]}

}
brand["number_stores"]=2
print(brand)
#solution 1
type_clothes=brand["type_of_clothes"]
print("zara's client are :")
for c in type_clothes:
    print('-', c)
  #solution 2   
print(f"Zara's clients are {",".join(brand.get('type_of_clothes', []))}")

# brand["country_creation"]= "Spain"
brand.setdefault("country_creation", "Spain")
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

#Delete the information about the date of creation.
del brand["creation_date"]

print("the last competitor is : ", brand["international_competitors"][-1])

print("the major clothes colors in the US are : " , brand["major_color"]["US"])
print("Number of key-value pairs:", len(brand))
print("keys of brand are : ",list(brand.keys()))

more_on_zara ={
    "creation_date":1975 ,
    "number_stores" : 10000,
}
brand.update(more_on_zara)

print("number of stores:", brand["number_stores"])