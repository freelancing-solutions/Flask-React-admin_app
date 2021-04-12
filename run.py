import os
from admin_app.main import create_admin_app

admin_app = create_admin_app()

if __name__ == '__main__':
    admin_app.run(debug=True, use_reloader=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8081)))

