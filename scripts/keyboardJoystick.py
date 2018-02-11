#!/usr/bin/env python

import roslib
roslib.load_manifest('object_detector')
from pynput import keyboard

import rospy
from std_msgs.msg import Int16


class RoboController(object):
    """docstring for RoboController"""

    def __init__(self):
        super(RoboController, self).__init__()
        self.keyboard_command_pub = rospy.Publisher(
            "/vel_cmnd", Int16, queue_size=1)
        # self.image_sub = rospy.Subscriber(
        #     "/raspicam_node/image/compressed", CompressedImage, self.callback, queue_size=1, buff_size=2**24)
        # self.enigine_on_sub = rospy.Subscriber(
        #     "/raspicam_node/image/compressed", CompressedImage, self.callback, queue_size=1, buff_size=2**24)
        self.stop = 0
        self.go_forward = 1
        self.go_backward = 2
        self.turn_right = 3
        self.turn_left = 4
        self.keyboard = keyboard

    def on_press(self, key):

        try:
            if key == self.keyboard.Key.up:
                self.keyboard_command_pub.publish(int(1))

            if key == self.keyboard.Key.down:
                self.keyboard_command_pub.publish(int(2))

            if key == self.keyboard.Key.left:
                self.keyboard_command_pub.publish(int(7))

            if key == self.keyboard.Key.right:
                self.keyboard_command_pub.publish(int(6))
        except AttributeError:
            pass

    def myhook():
        print "shutdown time!"

    def on_release(self, key):

        if key == self.keyboard.Key.esc:
            listener.stop()
            # rospy.on_shutdown(self.myhook)
            return False
        else:
            self.keyboard_command_pub.publish(int(0))

    # def command_publisher(self):


if __name__ == '__main__':
    try:

        ctrl_node = RoboController()
        # ctrl_node.command_publisher()
        rospy.init_node('vel_cmnd')

        with ctrl_node.keyboard.Listener(
                on_press=ctrl_node.on_press,
                on_release=ctrl_node.on_release) as listener:
            listener.join()
        rospy.spin()
        # Collect events until released

    except KeyboardInterrupt:
        listener.stop()
