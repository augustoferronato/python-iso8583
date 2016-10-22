"""

(C) Copyright 2016 Jose Augusto Ferronato

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *
import sys
import traceback

import os

#os.system(['clear', 'cls'][os.name == 'nt'])

#Uncomment to see the debug
#i2 = ISO8583(debug=True)


i2 = ISO8583()
# Execute a read file from local machine, you can set this to reflect your environment
iso2 = open("iso.txt","r")
lines = iso2.readline()
#iso2 = file.read(iso2)


#Here you can use the script receiving a ASCII has a parameter
#iso2 = raw_input("Enter the ASCII VALUE")


print ('\n\n\n------------------------------------------\n')
print ('This is the ISO <%s> parse it!' % lines)

i2.setIsoContent(lines)
#print ('Bitmap = %s' %i2.getBitmap())
#print ('MTI = %s' %i2.getMTI())

#print ('Bits')
#v3 = i2.getBitsAndValues()
#for v in v3:
	#print ('(1) Bit %s of type %s and value = %s' % (v['bit'],v['type'],v['value']))

# in this case, we need to redefine a bit because default bit 42 is A and in this especification is "N"
# the rest remain, so we use get's to copy original values :)
i2.redefineBit(42, '42', i2.getLargeBitName(42), 'N', i2.getBitLimit(42), i2.getBitValueType(42))
print ('\nBit 42 redefined...\n')

i3 = ISO8583(iso=lines)
print ('Bitmap = %s' % i3.getBitmap())
print ('MTI = %s' % i3.getMTI())

print ('Bits inside')
v4 = i3.getBitsAndValues()
for v in v4:

    print ('(2) Bit %s of type %s and value = %s' % (v['bit'], v['type'], v['value']))

iso2.close()
