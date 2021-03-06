# -*- coding: utf-8 -*-
# Copyright 2014 OpenMarket Ltd
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

from frozendict import frozendict


def freeze(o):
    if isinstance(o, dict) or isinstance(o, frozendict):
        return frozendict({k: freeze(v) for k, v in o.items()})

    if isinstance(o, basestring):
        return o

    try:
        return tuple([freeze(i) for i in o])
    except TypeError:
        pass

    return o


def unfreeze(o):
    if isinstance(o, frozendict) or isinstance(o, dict):
        return dict({k: unfreeze(v) for k, v in o.items()})

    if isinstance(o, basestring):
        return o

    try:
        return [unfreeze(i) for i in o]
    except TypeError:
        pass

    return o
