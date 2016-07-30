__author__ = 'Mansur'
import cx_Freeze

executables = [cx_Freeze.Executable("Drone Wars.py")]

cx_Freeze.setup(
    name = "Liberal Drones",
    options = {"build_exe":{"packages":["pygame"], \
                            "include_files":[
                                "drone.png",
                                "enemy.png",
                                "enemy_dead.png"]
                            }},
    executables = executables)