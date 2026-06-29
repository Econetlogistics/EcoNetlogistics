from flask import Blueprint,jsonify
api=Blueprint('api',__name__)
@api.route('/status')
def status(): return jsonify({'status':'running','application':'Logistics Management System'})
