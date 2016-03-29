

udev rules for various cameras under the ownership of the IEEE robotics team.

Basic idea:

- Find information unique to each camera.
- Write a rule that identifies it, and creates a link between that device and /dev/video0 (or wherever it's actually attached)
- Use something else to look at where the symbolic link and parse whatever it's actually pointing.
- examples present
- TODO: Write more detailed guide on how to gather rules and how to sue them.
