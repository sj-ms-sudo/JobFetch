import requests
import base64
import argparse
import json
def search(keywords,location,salary,save,results):
    try:
        salary = int(salary)
    except:
        print("Min salary should be a numerical value")
        exit()
    try:
        results = int(results)
    except:
        print("Results should be of numerical value")
        exit()
    API_KEY = 'dc5d993e-9eb3-424a-a4b0-22c0a978a5b4'
    auth_string = f"{API_KEY}:".encode()
    encoded_auth =base64.b64encode(auth_string).decode()
    headers = {'Authorization':f'Basic {encoded_auth}' , 'Content-type': 'application/json'}
    url = f"https://www.reed.co.uk/api/1.0/search/"
    for keyword in keywords:
        params = {'keywords':keyword,'locationName':location,'minimumSalary':salary,'resultsToTake':results}
        try:
            response = requests.get(url,params=params,headers=headers,timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print("Request Timed Out")
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error {e}")
        except requests.exceptions.RequestException as e:
            print(f"Some general error {e}")
        data = response.json()
        print(f"{data['totalResults']} results found matching {keyword}")
        if data['totalResults'] >0:
            for job in data['results']:
                with open(save,'a') as file:
                    file.write(f"Matched :   {keyword}\n")
                    file.write(f"Employer name   :   {job['employerName']}\n")
                    file.write(f"Title   :   {job['jobTitle']}\n")
                    file.write(f"Description :   {job['jobDescription']}\n")
                    file.write(f"URL :   {job['jobUrl']}\n")
                    file.write('-'*50)
        else:
            print(f"No job results for keyword {keyword}")
    print(f"Results saved to {save} ")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find suitable jobs based on keywords , location and minimum salary")
    parser.add_argument("keywords",nargs='+',help="Specify the keywords")
    parser.add_argument("-l","--location",help="Specify the Location")
    parser.add_argument('-sal',"--salary",default=0,help = "Specify the minimum salary , leave if no salary is to be given")
    parser.add_argument('-r',default=100,help = "Specify the maximum number of results matching a keyword ,default is 100")
    parser.add_argument('-s',help = "Specify the file name to save the details")
    args = parser.parse_args()
    search(args.keywords,args.location,args.salary,args.s,args.r)

