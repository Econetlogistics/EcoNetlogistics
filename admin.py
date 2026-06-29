from flask import Blueprint,render_template
admin=Blueprint('admin',__name__)
@admin.route('/')
def dashboard(): return render_template('admin.html')
