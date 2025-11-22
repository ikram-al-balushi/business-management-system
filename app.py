#!/usr/bin/env python3
"""
Entry point for deployment
"""
from business_management_system import app

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)