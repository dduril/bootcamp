# -----------------------------------------------
# Python Examples
#
# Binary Files
# -----------------------------------------------

def main():
    buffer_size = 50000
    in_file = ('some_image_file.jpg', 'rb')
    out_file = ('new_image_file.jpg', 'wb')
    buffer = in_file.read(buffer_size)
    while len(buffer):
        out_file.write(buffer)
        print('.', end='') # for purposes of seeing something on the screen
        buffer = in_file.read(buffer_size)
    print("Done")

if __name__ == "__main__": main()
