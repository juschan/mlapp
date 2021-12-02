# Web Deployment example - Wine dataset

### Procedure to deploy ML models on Heroku.

Ref: [Deploying ML MOdel as a Flask App on Heroku](https://medium.com/analytics-vidhya/deploying-a-machine-learning-model-as-a-flask-app-on-heroku-part-1-b5e194fed16d)

[Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

### Steps
1. Create directory and git init
2. Run python -m venv env  
3. Navigate to env/Scripts and run activate
4. pip install pandas numpy scikit-learn flask gunicorn
5. pip freeze > requirements.txt
6. git add and commit requirements.txt

7. Create the pkl model file using model.py. Remember to create relevant directories (lib/models)
8. Create app.py.
9. Create main.html and store within a new 'template' directory.
10. Do flask run and make sure the web app works

11. Add README.md with documentation
12. Git add/commit these files.
13. Create github repo and push these files to the repo
 

