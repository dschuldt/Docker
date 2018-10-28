#!/bin/sh
if [ -e /var/lib/clamav/main.cvd ]; then
  supervisorctl start clamav    
else
  freshclam && supervisorctl start clamav    
fi  
exit 0
