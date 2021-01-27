# -*- coding: utf-8 -*-
# Copyright 2020- Datastax, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from medusa.service.snapshot.abstract_snapshot_service import AbstractSnapshotService


class CCMSnapshotService(AbstractSnapshotService):

    def create_snapshot(self, *, tag):
        # create the CCM command
        cmd = 'ccm node1 nodetool \"snapshot -t {}\"'.format(tag)
        os.popen(cmd).read()

    def delete_snapshot(self, *, tag):
        # create the CCM command
        cmd = 'ccm node1 nodetool \"clearsnapshot -t {}\"'.format(tag)
        os.popen(cmd).read()
