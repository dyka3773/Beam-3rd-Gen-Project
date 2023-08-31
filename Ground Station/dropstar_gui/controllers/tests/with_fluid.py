from flask import render_template


def render_page():
    return render_template('test_pages.j2', title='Test With Fluid', fluid=True)
