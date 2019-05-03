# -*- coding: utf-8 -*-
# Copyright 2016 OpenMarket Ltd
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

import logging

from twisted.internet import defer

from synapse.handlers._base import BaseHandler
from synapse.types import ReadReceipt

logger = logging.getLogger(__name__)

class EphemeralEventHandler(BaseHandler):
    def __init__(self, hs):
        super(EphemeralEventHandler, self).__init__(hs)

        self.server_name = hs.config.server_name
        self.store = hs.get_datastore()
        self.hs = hs
        self.federation = hs.get_federation_sender()
        hs.get_federation_registry().register_edu_handler(
            "m.room.ephemeral", self._recv_edu
        )
        self.clock = self.hs.get_clock()
        self.state = hs.get_state_handler()


    @defer.inlineCallbacks
    def _recv_edu(self, origin, content):
        edu_type = content["edu_type"]
        edu_content = content["content"]

        #TODO: Add logic to receive and process EDU

    #TODO Add logic to allow a HS to send EDU events to others (if even possible.)