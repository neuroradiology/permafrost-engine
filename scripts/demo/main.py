#
#  This file is part of Permafrost Engine. 
#  Copyright (C) 2018 Eduard Permyakov 
#
#  Permafrost Engine is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Permafrost Engine is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
#  Linking this software statically or dynamically with other modules is making 
#  a combined work based on this software. Thus, the terms and conditions of 
#  the GNU General Public License cover the whole combination. 
#  
#  As a special exception, the copyright holders of Permafrost Engine give 
#  you permission to link Permafrost Engine with independent modules to produce 
#  an executable, regardless of the license terms of these independent 
#  modules, and to copy and distribute the resulting executable under 
#  terms of your choice, provided that you also meet, for each linked 
#  independent module, the terms and conditions of the license of that 
#  module. An independent module is a module which is not derived from 
#  or based on Permafrost Engine. If you modify Permafrost Engine, you may 
#  extend this exception to your version of Permafrost Engine, but you are not 
#  obliged to do so. If you do not wish to do so, delete this exception 
#  statement from your version.
#

import pf
import ui

from constants import *
from units import *

############################################################
# Global configs                                           #
############################################################

pf.set_ambient_light_color([1.0, 1.0, 1.0])
pf.set_emit_light_color([1.0, 1.0, 1.0])
pf.set_emit_light_pos([1024.0, 768.0, 768.0])

############################################################
# Setup map/scene                                          #
############################################################

pf.new_game("assets/maps", "demo.pfmap")
pf.set_map_render_mode(pf.CHUNK_RENDER_MODE_PREBAKED)
scene_objs = pf.load_scene("assets/maps/demo.pfscene")

############################################################
# Setup global events                                      #
############################################################

active_cam_idx = 0
def toggle_camera(user, event):
    mode_for_idx = [1, 0]

    if event[0] == pf.SDL_SCANCODE_C:
        global active_cam_idx
        active_cam_idx = (active_cam_idx + 1) % 2
        pf.activate_camera(active_cam_idx, mode_for_idx[active_cam_idx])

def toggle_sinbad(user, event):
    global scene_objs
    if event[0] == pf.SDL_SCANCODE_V:
        for ent in [obj for obj in scene_objs if isinstance(obj, sinbad.Sinbad)]:
            ent.notify(EVENT_SINBAD_TOGGLE_ANIM, None)


pf.register_event_handler(pf.SDL_KEYDOWN, toggle_camera, None)
pf.register_event_handler(pf.SDL_KEYDOWN, toggle_sinbad, None)

############################################################
# Setup UI                                                 #
############################################################

demo_win = ui.DemoWindow()
demo_win.show()

perf_win = ui.PerfStatsWindow()
perf_win.show()

