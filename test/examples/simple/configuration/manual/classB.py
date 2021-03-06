#//----------------------------------------------------------------------
#//   Copyright 2007-2010 Mentor Graphics Corporation
#//   Copyright 2007-2011 Cadence Design Systems, Inc.
#//   Copyright 2010-2011 Synopsys, Inc.
#//   Copyright 2019-2020 Tuomas Poikela (tpoikela)
#//   All Rights Reserved Worldwide
#//
#//   Licensed under the Apache License, Version 2.0 (the
#//   "License"); you may not use this file except in
#//   compliance with the License.  You may obtain a copy of
#//   the License at
#//
#//       http://www.apache.org/licenses/LICENSE-2.0
#//
#//   Unless required by applicable law or agreed to in
#//   writing, software distributed under the License is
#//   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//   CONDITIONS OF ANY KIND, either express or implied.  See
#//   the License for the specific language governing
#//   permissions and limitations under the License.
#//----------------------------------------------------------------------


from uvm import (UVMComponent, UVMConfigDb, sv, uvm_error)
from classC import ClassC


class ClassB(UVMComponent):


    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.debug = 0  # type: int
        self.u1 = None  # type: ClassC

    def build_phase(self, phase):
        super().build_phase(phase)

        _str = []
        if UVMConfigDb.get(self, "", "debug", _str):
            self.debug = _str[0]
        else:
            uvm_error("NO_CONF_MATCH", "Did not get debug")
        UVMConfigDb.set(self, "u1", "v", 0)

        sv.display("%s: In Build: debug = %0d", self.get_full_name(), self.debug)

        self.u1 = ClassC("u1", self)


    def get_type_name(self):
        return "B"

    def do_print(self, printer):
        printer.print_field("debug", self.debug, 1)
