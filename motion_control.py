import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Tb3(Node):
    def __init__(self):
        super().__init__('tb3')
        
        # Create Publisher Node for cmd_vel topic
        # Put your code here

	# Create Subscriber Node for scan topic
	# Put your code here
	
	# Create Subscriber Node for robot_map_pose/odom topic (Vector3)
	# Put your code here

    def scan_callback(self, msg):
        # Example for print message from scan topic
        print(msg.ranges[0])
        
        # Put your code here
    def pose_callback(self, msg):
        # Put your code here
		
		
def main(args=None):
    rclpy.init(args=args)

    tb3 = Tb3()

    rclpy.spin(tb3)  # execute tb3 node
    # blocks until the executor cannot work

    tb3.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
