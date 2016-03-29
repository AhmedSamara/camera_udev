
def find_name(symlink):
    # find where symlink is pointing (/dev/vide0, video1, etc)
    cmd = "readlink -f /dev/" + symlink 
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    out = process.communicate()[0]

    #extract ints from name video0, etc
    nums = [int(x) for x in out if x.isdigit()]
    # There should not be more than one digit
    if len(nums) <= 0:
         return -1
    interface_num = nums[0]    
    return interface_num
