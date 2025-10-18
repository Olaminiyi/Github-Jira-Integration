# GitHub-Jira Integration

This project demonstrates how to integrate **GitHub** with **Jira** so that a Jira ticket is automatically created when an issue is raised on GitHub and the comment `/jira` is added.  

By setting up this integration, developers and project managers can seamlessly connect GitHub issues with Jira tasks, ensuring better visibility and tracking across teams.  

---

## 🚀 Features
- Create a Jira ticket directly from a GitHub issue by typing `/jira` in the comment.
- Sync GitHub issues with Jira board for better project tracking.
- Uses **Python** for automation scripts.
- Deployed and executed on **AWS EC2** instance.

---

## 🛠️ Tech Stack
- **GitHub** – Issue tracking and source control.
- **Jira** – Project management and task tracking.
- **Python** – For handling the automation logic.
- **AWS EC2** – Hosting and running the integration script.

---

## ⚙️ How It Works
1. A GitHub user raises an issue on a repository.  
2. The user types `/jira` in the issue comment.  
3. The integration script (Python) listens for this event via GitHub Webhooks.  
4. The script connects to Jira’s REST API and creates a corresponding ticket on the Jira board.  
5. Jira ticket ID is sent back as a comment on the GitHub issue for tracking  

---

## 📋 Setup Instructions

### 1. Prerequisites
- Jira account (with API token and project key).  
- GitHub repository with admin access.  
- AWS account (to provision EC2 instance).  
- Python 3.x installed.  

### 2. Configure AWS EC2
- Launch an EC2 instance (Ubuntu recommended).  
- Install Python and required dependencies.  

```
bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 3. Clone the Repository
```
git clone https://github.com/your-username/GitHub-Jira-Integration.git
cd GitHub-Jira-Integration
```

### 4. Install Dependencies
```
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Create a .env file with the following details:

```
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
JIRA_PROJECT_KEY=PROJECTKEY
GITHUB_SECRET=your-github-webhook-secret
```

### 6. Configure GitHub Webhook
- Go to your GitHub repository → Settings → Webhooks → Add Webhook.

- Set the payload URL to your EC2 instance public URL (e.g., http://your-ec2-ip/webhook).

- Choose application/json.

- Select Issue comments event.

- Save.

## 7. Run the Script
```
python app.py
```

✅ Example Workflow

1. Raise a GitHub issue.

2. Add a comment:
```
/jira
```
3. A Jira ticket will be automatically created and linked back to the GitHub issue.

📌 Future Enhancements

- Support for custom Jira fields (priority, labels, etc.).

- Two-way sync (updates from Jira reflected in GitHub).

- Dockerize the application for easier deployment.

🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

📜 License

This project is licensed under the MIT License.

