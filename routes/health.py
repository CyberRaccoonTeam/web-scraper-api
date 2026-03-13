"""
Health Check Routes - Monitoring endpoint
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, jsonify
from datetime import datetime
import sqlite3

health_bp = Blueprint('health', __name__)

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scraper.db')


@health_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    db_status = 'ok'
    
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute('SELECT 1')
        conn.close()
    except Exception as e:
        db_status = f'error: {str(e)}'
    
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'database': db_status,
        'version': '1.0.0'
    }), 200