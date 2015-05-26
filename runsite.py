import os, sys

# Set build number if not found in os env.
if not os.environ.has_key('BUILD_NUMBER'):
    os.environ['BUILD_NUMBER'] = 'unknown'

from dotcom import app as application

if __name__ == '__main__':
    application.run(debug=application.debug, host='0.0.0.0', port=5000)

