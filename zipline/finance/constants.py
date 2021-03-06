#
# Copyright 2012 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import timedelta

TRADING_DAYS_IN_YEAR = 250
TRADING_HOURS_IN_DAY = 6
MINUTES_IN_HOUR = 60

ANNUALIZER = {'daily': TRADING_DAYS_IN_YEAR,
              'hourly': TRADING_DAYS_IN_YEAR * TRADING_HOURS_IN_DAY,
              'minute': TRADING_DAYS_IN_YEAR * TRADING_HOURS_IN_DAY *
              MINUTES_IN_HOUR}

FILL_DELAYS = {'daily': timedelta(days=1),
               'minute': timedelta(minutes=1)}
