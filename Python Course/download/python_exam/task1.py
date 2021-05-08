def get_highest_lowest():

 from robot_control_class import RobotControl

 rc = RobotControl();

 a = list(rc.get_laser_full())
 
 
 max = a[0];
 
 for x in a:
    if x == float('inf'):
        continue
    else:  
        if x > max:
           max = x;

 min = a[0];

 for y in a:
    if y == float('inf'):
        continue
    else:    
        if y < min:
           min = y;
  
 d = a.index(max)
 e = a.index(min)
 return d,e
       
