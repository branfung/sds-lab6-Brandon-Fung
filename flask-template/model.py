# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def capitals_output(answers):
    states_capitals = {'FL': 'tallahassee', 'NY': 'albany', 'WA': 'olympia', 'CA': 'sacramento', 'NV': 'carson city'}

    results = dict()
    for state, answer in answers.items():
        results[state] = states_capitals[state] == answer.lower()   
    return results 

def accuracy(answers):
    count = 0
    for value in capitals_output(answers).values():
        if value == True:
            count += 1
    return (count / 5) * 100