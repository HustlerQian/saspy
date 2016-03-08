#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# Configuration names for SAS - python List
# 
#SAS_config_names=['default', 'sasother']
#
SAS_config_names=['default']



# These need path to SASHome and version number - python Dict
# A usual install path is: /opt/sasinside/SASHome/SASFoundation/9.4/sas
# valid keys are:
# 'path'    - path to SASHome i.e.: /opt/sasinside/SASHome
# 'version' - version number that is a subdirectory below SASHome subdirectories
# 'options' - SAS options to include in the start up command line - Python List
#
#
#
default={'path'    : '/opt/sasinside/SASHome',
         'version' : '9.4'
         }

#sasother={'path'    : '/opt/sasinside/SASHome',
#          'options' : ["-autoexec", "/u/sastpw/tkpygit/metis/a.sas", "-set", "Env_var", "Value", "-fullstimer"], 
#          'version' : '9.4',
#          }
