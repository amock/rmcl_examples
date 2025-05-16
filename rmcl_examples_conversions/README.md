# RMCL Conversions


So, well-known message types such as `sensor_msgs/PointCloud2` or `sensor_msgs/LaserScan` has to be converted to one of those RMCL messages first, before starting the RMCL nodes.

Reason ...

## RMCL Messages

The localization approaches in RMCL seek to support four main messages that include sensor model and data: 

![RMCL Msgs](.media/rmcl_conversions.png)

|     |      |
|:---:|:-----|
| `ScanStamped` | This message describes a spinning range sensor, such as a Velodyne, by describing both the vertical and horizontal directions by fixed angle increments. This message is analogously desgined to the 2D counterpart [`sensor_msgs/LaserScan`](https://github.com/ros2/common_interfaces/blob/jazzy/sensor_msgs/msg/LaserScan.msg). |
| `PinholeStamped` | A `ScanStamped` message describes a range sensor that can be modeled by Pinhole projection.  |
| `O1DnStamped` | A more flexible description of a range sensor consisting of one measurement origin and a list of arbitrary measurement directions. |
| `OnDnStamped` | Same as O1DnStamped but you can give every measurement direction an own origin.  |

For more details how the actual fields of the messages look like we refer to the message definitions or the docs of the [rmagine](https://github.com/uos/rmagine) library.


## Need for Conversion




