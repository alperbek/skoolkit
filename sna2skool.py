#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012 Richard Dymond (rjdymond@gmail.com)
#
# This file is part of SkoolKit.
#
# SkoolKit is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# SkoolKit is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# SkoolKit. If not, see <http://www.gnu.org/licenses/>.

import sys

from skoolkit import sna2skool, usage, error, UsageError, SkoolKitError

try:
    sna2skool.main(sys.argv[1:])
except UsageError as e:
    usage(e.args[0])
except SkoolKitError as e:
    error(e.args[0])
