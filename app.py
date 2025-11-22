#!/usr/bin/env python3
"""
Entry point for deployment
"""
import os
from business_management_system import app

# For gunicorn
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)