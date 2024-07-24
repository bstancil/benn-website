# benn-website

How to run it:

- Run `source venv/bin/activate` to activate the virtual environment (`deactivate` will turn it off).
- Run `gunicorn --bind 0.0.0.0:8000 wsgi:app`. 


Here's how to deploy this thing:

- Add your changes to git via `git add .` and `git commit -m` like usual.
- Push them to Herkok via `git push heroku main`.
- Push them to Github via `git push origin main`.



https://chatgpt.com/c/7a628905-e1e3-48b1-94b0-2feb451671d3

## Setup

This logs into the EC2 instance:
```
chmod 400 benn-master.pem
ssh -i "benn-master.pem" ubuntu@ec2-35-94-28-233.us-west-2.compute.amazonaws.com
```

This installs the updates, and clones this repo:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx git

cd /home/ubuntu
git clone https://github.com/bstancil/benn-website.git
cd benn-website

sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate

## From the virtual environment
pip install -r requirements.txt
pip install gunicorn
```

## Running a dev environment

1. Log into EC2.
2. Navigate to the benn-website directory.
3. Activate the virtual environment.
4. Run gunicorn.

```
ssh -i "benn-master.pem" ubuntu@ec2-35-94-28-233.us-west-2.compute.amazonaws.com
cd /home/ubuntu/benn-website
source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

From a local terminal:
```
ssh -i "benn-master.pem" -L 8000:localhost:8000 ubuntu@ec2-35-94-28-233.us-west-2.compute.amazonaws.com
```

## Making updates

1. Push updates to Github.
2. From `/benn-website` in EC2, run `git pull`.

