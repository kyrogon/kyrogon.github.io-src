from flask import render_template
from . import app, resume

@app.route('/')
def resume_view():
    context = {
        'subject': resume.subject,
        'experience': resume.experience,
        'education': resume.education,
        'social_links': resume.social_links,
        'skill_icons': resume.skill_icons,
        'skillset': resume.skillset,
    }
    return render_template('resume/resume.html', **context)

