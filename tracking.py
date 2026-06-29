from flask import Blueprint,render_template
tracking=Blueprint('tracking',__name__)
@tracking.route('/')
def tracker(): return render_template('tracking.html')
