import requests, json

# CSO - Databases - Census 2022 - Actual and Percentage Population Change 1926-1922 - RESTful API
# FP002 is the table / dataset
url_beginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_end = "/JSON-stat/2.0/en"

def get_all_as_file(dataset):
    with open("cso.json",'wt') as fp:
        print(json.dumps(get_all(dataset)), file=fp)

def get_all(dataset):
    response = requests.get(url_beginning + dataset + url_end)
    print("url is ", url_beginning + dataset + url_end)
    return response.json()

# function to return the DAO as json with the data summarized by county
def get_formatted(dataset):
    data = get_all(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]

    for dim1 in range (1, sizes[0]):    # 1 - 3 in our case... we want the indexes and the labels.
                                        # this will only run for 1 to sizes[0]-1
        currentid = ids[0]
        print(currentid)

def get_formatted_as_file(dataset):
    pass

if __name__ == "__main__":
    get_formatted("FP002")
    #get_all_as_file("FP002")


# file = open("simple.json",'w') # not good syntax
#with open("simple.json",'w') as file:
#    json.dump(data, file, indent=4)
#json_string = json.dumps(data)
#print(f"string is {json_string}")