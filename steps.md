-  login or create a Jira account

- create a project

- create API token 

- Create a .env document in your root folder and put the Jira token and your email there. The are seceret not to be exposed

- install python-dotenv to load the secret in the .env to the code 

```

```

- Copy the Get all project code from the Jira api documentation. 
1. Change the url to your jira url
2. put your email address
3. load the API token save in the .env file using load_dotenv library

- Load the .env file in t

- run the code and it will bring all the project you have in your Jira account 

- to make it readable, will not print everything to the screen

```
output = json.loads(response.text)
name = output[0]["name"]
```

All these above steps will let you list al your project in your Jira, the code is in `list_project.py`

### To create a ticket(issue) in Jira
- go to the doucmentation again, search for `Issues` and click on `Create issue`. 

- When you check the jira board, to create an issue(tickets); not all fields are required but the api from he documentation is bringing every. so we removed fields that are not necessary

- The fields are
1. Project: name of the project
2. issue type
3. description
4. summary
5. reporter 

- description is important leave it and put your description
- issue type is important. it requires an `id`. to get the ID
 - click on the 3 dots athe right hand side of the board and click `configure board`

 - then check the `url` and copy the digits on it

- under project, when you create your project on jira it will give you a key. for this project it is `ECP`. put `KEY:ECP`.

## Github-Jira integration
- install fask with pip
```
pip install flask
```

sudo apt update
sudo apt install python3-pip -y

18.170.59.54
