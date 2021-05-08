from robot_control_class import RobotControl
import math

class ExamControl:
    def __init__(self):
        self.rc = RobotControl();
        self.inf = math.inf;

    def get_laser_readings(self):
        right_reading = self.rc.get_laser(0);
        left_reading = self.rc.get_laser(719);
        return left_reading, right_reading

    def main(self):
        while self.rc.get_laser(0) != self.inf or self.rc.get_laser(719) != self.inf:
               self.rc.move_straight(); 

        self.rc.stop_robot();
