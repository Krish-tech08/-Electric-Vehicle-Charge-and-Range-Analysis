from flask import Flask, render_template

app = Flask(__name__)

# You'll paste your actual Tableau Public URLs here!
DASHBOARD_URL = "https://public.tableau.com/app/profile/kushagra.verma4013/viz/Book2_17729068481180/Dashboard1?publish=yes"
STORY_URL = "https://public.tableau.com/app/profile/kushagra.verma4013/viz/Book2_17729068481180/StoryofElelcticCarsinIndia?publish=yes"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', tableau_url=DASHBOARD_URL)

@app.route('/story')
def story():
    return render_template('story.html', tableau_url=STORY_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)