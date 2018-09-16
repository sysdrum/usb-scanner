#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  check_support_standard.py
#  
#  Copyright 2018 Thomas Castleman <draugeros@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
check = sys.argv[1]
print(check)
list_check = ["045e:0202", "045e:0285", "045e:0285", "045e:0287", "045e:0289", "046d:ca84", "046d:ca88", "05fd:1007", "05fd:107a", "0738:4516", "0738:4522", "0738:4526", "0738:4536", "0738:4556", "0c12:8802", "0c12:8810", "0c12:9902", "0e4c:1097", "0e4c:2390", "0e6f:0003", "0e6f:0005", "0e6f:0006", "0e8f:0201", "0f30:0202", "0f30:8888", "102c:ff0c", "044f:0f07", "0e8f:3008", "045e:028e", "045e:028f", "0738:4716","0738:4726", "0738:4728", "0738:4740", "0738:b726", "0738:f738", "0738:4718", "0738:beef", "0f0d:000a", "f0d:000d", "0f0d:0016", "24c6:5501", "24c6:5303", "162e:beef", "046d:c21d", "046d:c21e", "046d:c21f", "046d:c242", "0738:cb03", "0738:cb02", "0e6f:0201", "0e6f:0213", "0e6f:0401", "12ab:0301", "1430:4748", "1bad:0002", "1bad:0003", "1bad:f016", "1bad:f028", "1bad:f038", "1bad:f901", "1bad:f903", "15e4:3f00", "15e4:3f10", "045e:0291", "045e:0719", "1689:fd00", "1689:fd01", "12ab:0004", "15e4:3f0a", "24c6:5300", "24c6:5500", "24c6:5506", "24c6:5b02", "0738:4540", "0738:6040", "0c12:8809", "12ab:8809", "1430:8888", "044f:b304", "044f:b312", "06a3:ff0c", "054c:0268"]
SENT = 0
for x in list_check:
	if (check == x):
		SENT = 1
		exit(1)
if SENT == 0:
	exit(0)

