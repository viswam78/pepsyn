# Copyright 2016 Uri Laserson
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

from pytest import raises

# from Bio.Seq import Seq
from pepsyn.util import site2dna


class TestUtil(object):

    def test_site2dna_enzyme(self):
        assert site2dna('EcoRI') == 'GAATTC'

    def test_bad_site(self):
        with raises(ValueError):
            site2dna('foo')

    def test_manual_seq(self):
        assert site2dna('AGGCG') == 'AGGCG'