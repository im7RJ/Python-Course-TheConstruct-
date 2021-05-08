from robot_control_class import RobotControl

rc = RobotControl();

a = rc.get_laser(360)

while a > 1.5:
    rc.move_straight();
    print("Current Distance to Wall: ",a)
    a = rc.get_laser(360)   

rc.stop_robot();
rc.turn("counter-clockwise",0.315,4.8)

